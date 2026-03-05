{
    "name": "Advanced Website Snippet Styling",
    "summary": "Easily add multiple CSS classes, custom IDs, and inline styles to Sections, Divs, and Images in Odoo Website snippets — no coding required. Gain full control over frontend design with a developer-friendly and upgrade-safe solution.",
    "description": """
        This module makes it easy to add multiple CSS Classes, IDs, and Custom Styles to any Section, Div, or Image tag in Odoo Website snippets — without touching code.
        Using a simple and intuitive interface, website administrators and designers can fully customize snippet elements directly from the editor. This provides greater design flexibility, cleaner layouts, and faster website customization while keeping the system fully upgrade-safe.
        The module is ideal for developers, designers, and agencies who want advanced styling control in Odoo’s website builder while maintaining best practices.
        Key Features:
        Add multiple CSS classes to any snippet element
        Assign custom HTML IDs for precise targeting
        Apply inline custom styles directly from the UI
        Supports Section, Div, and Image (IMG) tags
        No coding required – works seamlessly with Odoo Website Editor
        Fully compatible with Odoo Website Snippets
        Developer-friendly and upgrade-safe
        Improves design flexibility and frontend customization
        Use Cases:
        Advanced UI/UX customization
        Custom animations and JavaScript targeting
        SEO-friendly element targeting
        Cleaner CSS management
        Faster website styling without theme modification
        KEYWORDS:
        Odoo Website Custom CSS | Odoo Snippet Customization | Odoo Add CSS Classes | Odoo Website Styling Module | Odoo Custom HTML ID | Odoo Website Builder | Odoo Frontend Customization | Odoo Snippet Styling | Odoo Website Developer Tools | Odoo Custom Design Module | Add multiple CSS classes in Odoo website | Customize Odoo website snippets without coding | Odoo module for custom styles and IDs | Advanced website styling for Odoo
    """,
    "category": "Website/Advanced Snippet Styling",
    "sequence": -1,
    "version": "19.0.1.0.0",
    "license": "OPL-1",
    "depends": ['website'],
    "assets": {
        'website.website_builder_assets': [
            "advanced_website_snippet_styling/static/src/builder/plugins/options/**"
        ]
    },
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'price': 5,
    'currency': 'EUR',
    "installable": True,
    "auto-install": False,
    "application": True,
}
