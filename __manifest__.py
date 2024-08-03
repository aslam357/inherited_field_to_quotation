{
    'name': 'add_product',
    'version': '1.0',
    'summary': 'Extend product and sale.order models with brand information.',
    'depends': ['base', 'sale_management', 'product','sale', 'stock',],  
    'data': [
                 'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
