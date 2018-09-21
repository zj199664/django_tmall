$(function () {
    let delete_url = '/car/delete/';
    let update_url = '/car/update/';
//    通过id获取的选择如果有多个只会选择第一个
    $('.car_btn').click(function () {
        let $btn = $(this);
        $.post(delete_url, {car_id: $(this).attr('car_id')}, function (result) {
            //    当数据库删除了数据就删除该条数据
            if (result.status === 200) {
                $btn.parents('tr').remove()
            }
        })
    });
    $('.add').click(function () {
        let $car_id = $('.car_btn').attr('car_id');
        let $input = $(this).prev('input');
        let value = parseInt($input.val()) < parseInt($input.attr('max'))
            ? parseInt($input.val()) + 1
            : parseInt($input.attr('max'));
        if (parseInt($input.val()) < parseInt($input.attr('max'))) {
            $.post(update_url, {'ac': 1, 'car_id': $car_id}, function (result) {
                if (result.status === 200) {
                    $input.val(value)
                }
            })
        }
    });
    $('.sub').click(function () {
        // alert($(this).parent().find(':input[type=text]').val())
        let $car_id = $('.car_btn').attr('car_id');
        let $input = $(this).next('input');
        let value = $input.val() > 1
            ? $input.val() - 1
            : 1;
        $.post(update_url, {ac: 2, 'car_id': $car_id}, function (result) {
            if (result.status === 200) {
                $input.val(value);
                $('#sum_price').attr()
            }
        })
    })
});
