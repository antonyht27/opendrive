odoo.define('opendrive_base_pos.PaymentScreen', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const PosBoletaPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);
            }

            toggleIsToTiket() {
                // click_ticket
                this.currentOrder.set_to_ticket(!this.currentOrder.is_to_ticket());
                this.render();
            }
        };

    Registries.Component.extend(PaymentScreen, PosBoletaPaymentScreen);

    return PaymentScreen;
});
