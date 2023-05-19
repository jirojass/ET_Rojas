$(document).ready(function () {
    var url = 'https://api.thecatapi.com/v1/images/search?limit=10';
    var images = [];

    $.ajax({
        url: url,
        type: 'GET',
        success: function (data) {
            for (var i = 0; i < data.length; i++) {
                var img = new Image();
                img.src = data[i].url;
                images.push(img);
            }
            for (var i = 0; i < images.length; i++) {
                var img = $('<img>').addClass('d-block w-100').attr({ 'src': images[i].src, 'alt': '...', 'data-type': 'image' });
                var item = $('<div>').addClass('carousel-item').attr('data-slide-number', i);

                if (i == 0) item.addClass('active');
                item.append(img);
                $('.carousel-inner').append(item);
            }
        },
        error: function () {
            console.log('Error cargando imagenes!');
        }
    });
});