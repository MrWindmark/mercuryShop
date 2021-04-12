window.onload = function () {
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    let quantity_arr = [];
    let price_arr = [];

    const TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    // console.info("Forms: ", TOTAL_FORMS);

    const order_quantity_target_element = $('.order_total_quantity');
    const order_cost_target_element = $('.order_total_cost');

    // console.info("order_quantity_target_element", order_quantity_target_element);

    let order_total_quantity_value = parseInt(order_quantity_target_element.text()) || 0;
    // console.info("order_total_quantity_value", order_total_quantity_value);
    let order_total_cost = parseFloat(order_cost_target_element.text().replace(',', '.')) || 0;
    // console.info("order_total_cost", order_total_cost);

    for (let i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        // console.info("_quantity", _quantity);
        // для объекта поля формы данные должны тянуться через val, а не text
        _price = parseFloat($('input[name="orderitems-' + i + '-price"]').val().replace(',', '.'));
        // console.info("_price", _price);
        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }

        if (!order_total_quantity_value) {
            for (let i = 0; i < TOTAL_FORMS; i++) {
                order_total_quantity_value += quantity_arr[i];
                order_total_cost += quantity_arr[i] * price_arr[i];
            }
            order_quantity_target_element.html(order_total_quantity_value.toString());
            order_cost_target_element.html(Number(order_total_cost.toFixed(2)).toString());
        }
    }

    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity;

        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity_value = order_total_quantity_value + delta_quantity;

        order_cost_target_element.html(order_total_cost.toString());
        order_quantity_target_element.html(order_total_quantity_value.toString());
    }

    let order_form = $('.order_form');
    order_form.on('click', 'input[type="number"]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        // console.info("orderitem_num", orderitem_num);
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    });
    order_form.on('click', 'input[type="checkbox"]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
        // console.info("orderitem_num", orderitem_num);
        if (target.checked) {
            delta_quantity = -quantity_arr[orderitem_num];
            console.info("delta_quantity", delta_quantity);
        } else {
            delta_quantity = quantity_arr[orderitem_num];
        }
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });
}