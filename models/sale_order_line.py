from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_name_with_brand = fields.Many2one(
        'product.brand',
        string = 'Product Brand',
        related = 'product_id.brand_id',
        store = True
    )

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.product_name_with_brand = self.product_id.brand_id
        else:
            self.product_name_with_brand = False
