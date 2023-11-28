$(document).ready(() => {
  $('.filters .amenities .popover li input').change(() => {
    const amenityNames = [];

    $('.filters .amenities .popover li input').each(function () {
      const amenityName = $(this).attr('data-name');
      if ($(this).is(':checked')) {
        amenityNames.push(amenityName);
      }
    });

    const h4Element = $('.filters .amenities h4');

    if (amenityNames.length > 0) {
      h4Element.text(amenityNames.join(', '));
    } else {
      h4Element.html('&nbsp;');
    }
  });

  $.get("http://localhost:5001/api/v1/status/", (data) => {
    if (data.status === 'OK') {
      $('header #api_status').addClass('available');
    } else {
      $('header #api_status').removeClass('available');
    }
  });

  $.ajax({
    url: 'http://localhost:5001/api/v1/places_search/',
    type: 'post',
    dataType: 'json',
    contentType: 'application/json',
    success: function (places) {
      places.forEach(place => {
        const placeArticle = $('<article></article>').appendTo('section.places');
        const titleBooks = $('<div class="title-box"></div>').appendTo(placeArticle);
        const placeName = $('<h2></h2>').text(place.name).appendTo(titleBooks);
        const priceByNight = $('<div class="price-by-night"></div>').text(place.price_by_night).appendTo(titleBooks);

        const information = $('<div class="information"></div>').appendTo(placeArticle);
        const maxGuest = $('<div class="max-guest"></div>').html('<i class="fa-solid fa-users"></i><br>' + place.max_guest).appendTo(information);
        const numberRooms = $('<div class="number-rooms"></div>').html('<i class="fa-solid fa-bed"></i><br>' + place.number_rooms).appendTo(information);
        const numberBathrooms = $('<div class="number-bathrooms"></div>').html('<i class="fa-solid fa-bath"></i><br>' + place.number_bathrooms).appendTo(information);

        const description = $('<div class="description"></div>').html('<h4>Description:</h4>' + place.description).appendTo(placeArticle);
      });
    },
    data: '{}'
  });
});
