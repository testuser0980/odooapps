import re
from odoo import models, fields, api
from .ai_generate_response import generate_text


class TrustpilotReviews(models.Model):
    _name = "trustpilot.reviews"
    _description = "Trustpilot Reviews"
    _rec_name = 'author_name'

    sequence = fields.Integer(string="Sequence")
    review_id = fields.Char(string="Review Id")
    author_name = fields.Char(string="Author Name")
    headline = fields.Char(string="Headline", translate=True)
    review_body = fields.Char(string="Review", translate=True)
    date_published = fields.Char(string="Date Published")
    best_rating = fields.Float(string="Best Rating")
    worst_rating = fields.Float(string="Worst Rating")
    rating_value = fields.Float(string="Rating Value")
    website_id = fields.Many2one('website', string="Website")
    author_image = fields.Image(string="Author Image")

    def cron_generate_reviews_translations_with_ai(self):
        reviews = self.env['trustpilot.reviews'].sudo().search([], limit=40)
        if reviews:
            for review in reviews:
                self.generate_review_translations_with_ai(review)

    def generate_review_translations_with_ai(self, review=None):
        langs = self.env['res.lang'].search([('active', '=', True), ('code', '!=', 'en_US')]).mapped('code')
        for lang in langs:
            prompt = (
                f"Please provide translations for: Headline={self.headline or review.headline}, Review Body"
                f"={self.review_body or review.review_body} into "
                f"{lang}. Please don't change keywords: Headline,Review Body.")
            response = generate_text(self, prompt)
            match_headline = re.search(r'Headline\s*[:=]\s*(.*)', response)
            headline = match_headline.group(1).strip() if match_headline else ""
            match_review_body = re.search(r'Review Body\s*[:=]\s*(.*)', response)
            review_body = match_review_body.group(1).strip() if match_review_body else ""
            translatable_record = self.with_context(lang=lang).sudo() or review.with_context(lang=lang).sudo()
            translatable_record.write({
                'headline': headline,
                'review_body': review_body
            })
