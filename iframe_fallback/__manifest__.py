{
    "name": "Iframe Fallback",
    "description": "This module will fix the issues related to http to https requests for Iframe Fallback.",
    "summary": "This module will fix the issues related to http to https requests for Iframe",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "category": "Website/Iframe",
    "depends": ["website"],
    "assets": {
        "web.assets_backend": [
            "iframe_fallback/static/src/js/iframe_fallback.js"
        ]
    },
    "images": ['static/description/banner.png'],
    "installable": True,
    "auto_install": False,
    "application": True,
}
