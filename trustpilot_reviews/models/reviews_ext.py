from odoo import models, fields


class ReviewsExt(models.Model):
    _inherit = "rating.rating"

    website_id = fields.Many2one('website', string="Website")
