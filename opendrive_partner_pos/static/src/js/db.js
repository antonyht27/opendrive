odoo.define("opendrive_partner_pos.DB", function (require) {
    "use strict";

    var PosDB = require("point_of_sale.DB");

    PosDB.include({
        _partner_search_string: function (partner) {
            var str =  this._super(partner);
            if(partner.l10n_cl_activity_description){
                str += '|' + partner.l10n_cl_activity_description;
            }
            return str;
        },
    });
});