# -*- coding: utf-8 -*-
{
    'name': 'Opendrive DTE Base POS',
    'summary': """ tipo de documento para la factura desde el POS """,
    'description': """ Se agrega un boton adicional para seleccionar el tipo de documento para la factura creada desde el POS.
                    Si no se selecciona es (33) factura electronica por defecto""",
    'author': 'Antony H / Opendrive Ltda',
    'website': 'https://www.opendrive.cl',
    'category': 'Sales/Point of Sale',
    'version': '15.0.1.0.0',
    'depends': ['point_of_sale', 'l10n_latam_invoice_document', 'l10n_cl'],
    'data': [],
    'assets': {
        'point_of_sale.assets': [
            'opendrive_base_pos/static/src/js/Screens/PaymentScreen.js',
            'opendrive_base_pos/static/src/js/models.js',
        ],
        'web.assets_qweb': [
            'opendrive_base_pos/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
