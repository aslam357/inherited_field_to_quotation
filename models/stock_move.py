from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    product_name_with_brand = fields.Char(
        string = 'Product Brand',
        compute = '_compute_product_name_with_brand',
        store = True
    )

    @api.depends('product_id')
    def _compute_product_name_with_brand(self):
        for move in self:
            move.product_name_with_brand = move.product_id.brand_id.name if move.product_id else ''


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    picking_priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], 
        string = 'Priority', 
        default = 'medium'
        )
