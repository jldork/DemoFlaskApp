
$(document).ready(function () {
    $('form').on('submit', function (e) {
        e.preventDefault();
    });
    $('input').on('keyup', function (e) {
        $.post('/score', e.target.value, function(data){
            $('.percentile').text(data)
        })
    })
});