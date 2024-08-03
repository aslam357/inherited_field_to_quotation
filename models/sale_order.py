from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _compute_product_name_with_brand(self):
        for line in self.order_line:
            if line.product_id:
                line.product_name_with_brand = f"{line.product_id.name} - {line.product_id.product_tmpl_id.product_brand_id.name or ''}"

    product_name_with_brand = fields.Char(
        string = 'Product Name with Brand',
        compute = '_compute_product_name_with_brand'
    )
