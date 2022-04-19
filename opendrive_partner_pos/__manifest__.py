# -*- coding: utf-8 -*-
{
    'name': 'Opendrive DTE partner POS',
    'summary': """ DTE partner POS """,
    'description': """ Se agrega el Campo Giro en el detalle del cliente deesde el POS """,
    'author': 'Antony H / Opendrive Ltda',
    'website': 'https://www.opendrive.cl',
    'category': 'Sales/Point of Sale',
    'version': '15.0.1.0.0',
    'depends': ['point_of_sale', 'l10n_cl_edi'],
    'data': [],
    'assets': {
        'point_of_sale.assets': [
            'opendrive_partner_pos/static/src/js/db.js',
            'opendrive_partner_pos/static/src/js/models.js',
        ],
        'web.assets_qweb': [
            'opendrive_partner_pos/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
