$(document).ready(() => {
  const filteredAmenitiesNames = [];
  const filteredStatesNames = [];
  const filteredCitiesNames = [];

  const filteredAmenitiesIds = [];
  const filtereddStatesIds = [];
  const filteredCitiesIds = [];
  const data = {
    amenities: filteredAmenitiesIds,
    states: filtereddStatesIds,
    cities: filteredCitiesIds
  };

  $('.filters .amenities .popover li input').change(function () {
    $('.filters .amenities .popover li input').each(function () {
      listenToCheckBox(this, filteredAmenitiesNames, filteredAmenitiesIds);
    });

    const h4Element = $('.filters .amenities h4');
    updateH4Text(h4Element, filteredAmenitiesNames);
  });

  $('.filters .locations .popover li h2 input').change(function () {
    $('.filters .locations .popover li h2 input').each(function () {
      listenToCheckBox(this, filteredStatesNames, filtereddStatesIds);

      const h4Element = $('.filters .locations h4');
      updateH4Text(h4Element, filteredStatesNames.concat(filteredCitiesNames));
    });
  });

  $('.filters .locations .popover li ul input').change(function () {
    $('.filters .locations .popover li ul input').each(function () {
      listenToCheckBox(this, filteredCitiesNames, filteredCitiesIds);

      const h4Element = $('.filters .locations h4');
      updateH4Text(h4Element, filteredStatesNames.concat(filteredCitiesNames));
    });
  });

  function listenToCheckBox (checkbox, filteredNames, filteredIds) {
    const choosenName = $(checkbox).attr('data-name');
    const choosenId = $(checkbox).attr('data-id');

    if ($(checkbox).is(':checked')) {
      if (!filteredNames.includes(choosenName)) filteredNames.push(choosenName);
      if (!filteredIds.includes(choosenId)) filteredIds.push(choosenId);
    } else {
      const nameIndex = filteredNames.indexOf(choosenName);
      if (nameIndex !== -1) filteredNames.splice(nameIndex, 1);

      const idIndex = filteredIds.indexOf(choosenId);
      if (idIndex !== -1) filteredIds.splice(idIndex, 1);
    }
  }

  function updateH4Text (h4Element, filteredNames) {
    if (filteredNames.length > 0) {
      h4Element.text(filteredNames.join(', '));
    } else {
      h4Element.html('&nbsp;');
    }
  }

  $.get('http://localhost:5001/api/v1/status/', (data) => {
    if (data.status === 'OK') {
      $('header #api_status').addClass('available');
    } else {
      $('header #api_status').removeClass('available');
    }
  });

  requestPlacesUsingPost();

  $('button').click(() => {
    requestPlacesUsingPost();
  });

  function requestPlacesUsingPost () {
    console.log(filteredAmenitiesIds);
    $.ajax({
      url: 'http://localhost:5001/api/v1/places_search/',
      type: 'post',
      dataType: 'json',
      contentType: 'application/json',
      success: function (places) {
        $('section.places article').remove();

        places.forEach(place => {
          const placeArticle = $('<article></article>').appendTo('section.places');
          const titleBooks = $('<div class="title-box"></div>').appendTo(placeArticle);
          $('<h2></h2>').text(place.name).appendTo(titleBooks);
          $('<div class="price-by-night"></div>').text(place.price_by_night).appendTo(titleBooks);

          const information = $('<div class="information"></div>').appendTo(placeArticle);
          $('<div class="max-guest"></div>').html('<i class="fa-solid fa-users"></i><br>' + place.max_guest).appendTo(information);
          $('<div class="number-rooms"></div>').html('<i class="fa-solid fa-bed"></i><br>' + place.number_rooms).appendTo(information);
          $('<div class="number-bathrooms"></div>').html('<i class="fa-solid fa-bath"></i><br>' + place.number_bathrooms).appendTo(information);

          $('<div class="description"></div>').html('<h4>Description:</h4>' + place.description).appendTo(placeArticle);
        });
      },
      data: JSON.stringify(data)
    });
  }
});
