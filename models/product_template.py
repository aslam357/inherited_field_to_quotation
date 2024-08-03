from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(
        'product.brand', 
        string ='Brand'
        )
    product_name_with_brand = fields.Char(
        string = 'Product Name with Brand',
        compute = '_compute_product_name_with_brand',
        store=True
    )

    @api.depends('name', 'brand_id.name')
    def _compute_product_name_with_brand(self):
        for template in self:
            if template.brand_id:
                template.product_name_with_brand = f"{template.name} ({template.brand_id.name})"
            else:
                template.product_name_with_brand = template.name
