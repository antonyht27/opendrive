# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import float_compare, float_is_zero


class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    to_ticket = fields.Boolean('To dte')
    
    def _prepare_invoice_vals(self):
        invoice_vals = super(PosOrder, self)._prepare_invoice_vals()
        if self.to_ticket:
            l10n_latam_document_type_id = self.env.ref('l10n_cl.dc_b_f_dte').id
            invoice_vals.update({'l10n_latam_document_type_id': l10n_latam_document_type_id})
        return invoice_vals

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        res.update({'to_ticket': ui_order['to_ticket'] if "to_ticket" in ui_order else False,})
        return res
