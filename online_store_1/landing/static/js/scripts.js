$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(product_id, number, is_delete){
        var data = {};
        data.product_id = product_id;
        data.number = number;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
        console.log(data)

        if (is_delete) {
            data["is_delete"] = true
        }
        console.log("TEST")
        console.log(data)


        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_number);
                if (data.products_total_number || data.products_total_number == 0){
                    $('#basket_total_number').text("("+data.products_total_number+")");
                }
                $('.basket-items ul').html("");
                $.each(data.list_of_all_positions, function(_, value){
                    $('.basket-items ul').append('<li>' + value.product_name + ', ' + value.number + 'шт. ' + 'по ' + value.product_price + 'руб   ' + 
                    '<a class="delete-item" href="#" data-product_id="'+value.id+'">x</a>' + '</li>')
                })
            },
            error: function() {
                console.log("ERROR")
            }
        });
    };

    form.on('submit', function(e){
        e.preventDefault();
        var number = $('#number').val();
        console.log(number);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketUpdating(product_id, number, is_delete=false);


        
    });

    $('.basket-conteiner').on('click', function(e){
        e.preventDefault();
        $('.basket-items').toggleClass('d-none');
    });

    $('.basket-conteiner').mouseover(function(){
        $('.basket-items').removeClass('d-none');
    });

    $('.basket-conteiner').mouseout(function(){
        $('.basket-items').addClass('d-none');
      });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id")
        number = 0
        console.log(number)
        basketUpdating(product_id, number, is_delete=true);
        $(this).closest('li').remove();
    });

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function(){
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount)
        $('#total_order_amount').text(parseFloat(total_order_amount).toFixed(2));
    };

    $(document).on('change', '.product-in-basket-number', function(){
        console.log('change');
        var current_number = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_number * current_price).toFixed(2);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);
        calculatingBasketAmount();
    });
    

    calculatingBasketAmount();
});