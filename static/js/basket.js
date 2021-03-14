window.onload = function () {
    $(".basket_block").on('click', 'input[type="number"]', function () {
        const target_href = event.target;

        $.ajax({
            url: "/basket/edit/" + target_href.name + "/" + target_href.value,
            success: function (data) {
                $('.basket_block').html(data.result);
            },
        });
        event.preventDefault();
    })
}