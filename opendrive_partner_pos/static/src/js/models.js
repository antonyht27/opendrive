odoo.define("opendrive_partner_pos.models", function (require) {
  "use strict";

  var models = require("point_of_sale.models");

  // Load the products used for creating program reward lines.
  var existing_models = models.PosModel.prototype.models;
  var partner_index = _.findIndex(existing_models, function (model) {
    return model.model === "res.partner";
  });

  var partner_model = existing_models[partner_index];
  models.load_models([
    {
      fields: partner_model.fields.push('l10n_cl_activity_description'),
    },
  ]);

});
