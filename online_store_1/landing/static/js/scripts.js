$(document).ready(function() {
    var form = $('#form_buying_product');
    console.log(form);
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


        var data = {};
        data.product_id = product_id;
        data.number = number;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");
        console.log(data)
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_number);
                if (data.products_total_number){
                    $('#basket_total_number').text("("+data.products_total_number+")");
                }
            },
            error: function() {
                console.log("ERROR")
            }
        });


        $('.basket-items ul').append('<li>' + product_name + ', ' + number + 'шт. ' + 'по ' + product_price + 'руб   ' + 
            '<a class="delete-item" href="#">x</a>' + '</li>')


    })

    $('.basket-conteiner').on('click', function(e){
        e.preventDefault();
        $('.basket-items').toggleClass('d-none');
    });

    $('.basket-conteiner').mouseover(function(){
        $('.basket-items').removeClass('d-none');
    });

    //$('.basket-conteiner').mouseout(function(){
    //    $('.basket-items').addClass('d-none');
    //  });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        $(this).closest('li').remove();
    })
    
});