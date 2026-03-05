{
    "name": "Trustpilot Reviews",
    "summary": "Trustpilot Reviews for Website",
    "description": "Trustpilot Reviews for Website",
    "category": "Trustpilot Reviews",
    "sequence": -1,
    "author": "Axiom World",
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
    "installable": True,
    "auto_install": False,
    "application": True
}
