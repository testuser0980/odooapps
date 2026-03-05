{
    "name": "Trustpilot Reviews",
    "summary": "Fetch, display, and AI-translate your Trustpilot reviews on your Odoo website with 3 beautiful snippet styles.",
    "description": """
        Automatically import your Trustpilot business reviews into Odoo with a single click — no API key required.
        Display them on any website page using 3 ready-made drag-and-drop snippet styles powered by Owl Carousel:
        Style 01 — full-width card with image and side-by-side content layout,
        Style 02 — centered minimal card with italic quote and uppercase reviewer name,
        Style 03 — bordered card with circular author avatar and Tomorrow-font typography.
        Auto-generate personalized initials-based author avatars, assign reviews per website, control display
        order with drag-and-drop sequencing, and translate review content into all active languages using
        Odoo's built-in AI engine (OLG API). Perfect for businesses that want to showcase real customer
        trust directly on their Odoo website.
    """,
    "category": "Trustpilot Reviews",
    "sequence": -1,
    "website_url": "https://axiomworld.net",
    "license": "LGPL-3",
    "version": "18.0.1.0",
    "depends": ["crm", "website", "website_sale"],
    "data": ["security/ir.model.access.csv", "data/data.xml", "templates/dynamic_snippets.xml",
             "templates/templates.xml", "views/trustpilot_reviews.xml", "views/menus.xml",
             "templates/extra_snippet_options.xml"],
    "assets": {
        'website.assets_wysiwyg': [
            ('include', 'web._assets_helpers'),
            "trustpilot_reviews/static/src/dynamic_snippet_options/website_ratings/options.js",
        ],
        "web.assets_frontend": [
            # "trustpilot_reviews/static/src/owl_components/**",
            "trustpilot_reviews/static/src/libs/**",
            "trustpilot_reviews/static/src/scss/**",
            "trustpilot_reviews/static/src/js/**",
        ]
    },
    "images": ["icon.png", "banner.png"],
    "price": "30",
    "currency": "EUR",
    "installable": True,
    "auto_install": False,
    "application": True
}
