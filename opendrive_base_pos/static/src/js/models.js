odoo.define('opendrive_base_pos.models', function (require) {
"use strict";

var models = require('point_of_sale.models');


var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function(attributes,options) {
            _super_order.initialize.apply(this, arguments);
            this.to_ticket = false;
            this.save_to_db();
        },

        init_from_JSON: function(json) {
            _super_order.init_from_JSON.apply(this,arguments);
            this.to_ticket = false;
        },

        export_as_JSON: function() {
            var json = _super_order.export_as_JSON.apply(this,arguments);
            json.to_ticket = this.to_ticket ? this.to_ticket : false;
            return json;
        },

        /* ---- Ticket --- */
        set_to_ticket: function(to_ticket) {
            this.assert_editable();
            this.to_ticket = to_ticket;
        },
        is_to_ticket: function(){
            return this.to_ticket;
        },

    });

});
