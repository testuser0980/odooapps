from odoo import models, fields, api
import requests
from bs4 import BeautifulSoup
import json
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import random

from PIL import Image, ImageDraw, ImageFont
import io
import base64
import random
import os
import os
from odoo import modules


def _generate_initials_image(self, full_name, size=1080):
    # Initials
    parts = full_name.strip().split()
    initials = ''.join([p[0].upper() for p in parts[:2]])

    # Deterministic color (same name = same color)
    seed = sum(ord(c) for c in full_name)
    random.seed(seed)

    bg_color = (
        random.randint(80, 160),
        random.randint(80, 160),
        random.randint(80, 160),
    )

    img = Image.new("RGB", (size, size), bg_color)
    draw = ImageDraw.Draw(img)

    # 🔥 FONT SIZE — BIG & CLEAR
    font_size = int(size * 0.55)  # 55% of canvas

    # ✅ FORCE TRUE TYPE FONT
    font_path = os.path.join(
        modules.get_module_path('trustpilot_reviews'),
        'static', 'src',
        'fonts',
        'Philosopher-Bold.ttf'
    )

    # font_path = ".Philosopher-Bold.ttf"

    if not os.path.exists(font_path):
        raise Exception("Font file not found. Philosopher-Bold is required.")

    font = ImageFont.truetype(font_path, font_size)

    # Center text perfectly
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size - text_width) / 2
    y = (size - text_height) / 2

    draw.text((x, y), initials, fill=(255, 255, 255), font=font)

    # Convert to base64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG", optimize=True)
    return base64.b64encode(buffer.getvalue())


class TrustpilotReviewsConfiguration(models.Model):
    _name = "trustpilot.reviews.configuration"
    _description = "Trustpilot Reviews Configuration"

    trustpilot_review_url = fields.Char(string="Trustpilot Review URL", help="Enter a URL for Trustpilot Review",
                                        required=True)

    trustpilot_review_widget = fields.Char(string="Trustpilot Review Widget")

    def fetch_trustpilot_reviews(self):
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        response = requests.get(self.trustpilot_review_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <script type="application/ld+json">
        scripts = soup.find_all('script', type='application/ld+json')
        data = json.loads(scripts[0].string)['@graph']
        review_data = []
        # Handle cases where data is a list or nested
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get('@type') == 'Review':
                    review_data.append(item)
        reviews = self.env['trustpilot.reviews'].sudo().search([])
        reviews_ids = []
        for review in reviews:
            reviews_ids.append(review.review_id)
        values = []
        for item in review_data:
            review_id = item.get('@id')
            if not review_id or review_id in reviews_ids:
                continue  # Skip if already exists
            values.append({
                'review_id': item['@id'],
                'author_name': item['author']['name'],
                'headline': item['headline'],
                'review_body': item['reviewBody'],
                'date_published': item['datePublished'],
                'best_rating': item['reviewRating']['bestRating'],
                'worst_rating': item['reviewRating']['worstRating'],
                'rating_value': item['reviewRating']['ratingValue'],
                'website_id': False
            })
        for value in values:
            if value['author_name']:
                value['author_image'] = _generate_initials_image(self, value['author_name'])
        self.env['trustpilot.reviews'].create(values)
        return
