$(document).ready(function () {
  // Creates an empty object called "amenityIDs"
  const amenityIDs = {};

  // Constructs the URL for the API
  const apiurl = 'http://' + window.location.hostname;

  // Sets up an event listener that triggers when any checkbox
  // input element on the page is clicked
  $('input[type="checkbox"]').click(function () {

    // Updates the "amenityIDs" object when a checkbox is clicked
    if ($(this).is(':checked')) {

      // Adds a new key-value pair to the "amenityIDs" object, where
      // the key is the value of the "data-name" attribute of the checkbox
      // and the value is the value of the "data-id" attribute of the checkbox.
      amenityIDs[$(this).attr('data-name')] = $(this).attr('data-id');
    } else {

      // Removes the corresponding key-value pair from the "amenityIDs"
      // object if the checkbox is unchecked.
      delete amenityIDs[$(this).attr('data-name')];
    }

    // Creates an empty array called "list"
    const list = [];

    // Iterates over the "amenityIDs" object using the $.each() method.
    // For each key-value pair in the object, the function passed to $.each()
    // pushes the key onto the "list" array.
    $.each(amenityIDs, function (index, place) {
      list.push(index);
    });

    // Updates the text inside an HTML element with class "amenities h4"
    // to show the list of selected checkboxes.
    if (list.length === 0) {

      // If there are no checkboxes selected (i.e. the "list" array is empty),
      // then the text is set to a non-breaking space.
      $('.amenities h4').html('&nbsp');
    } else {

      // Otherwise, the text is set to a comma-separated string of the
      // keys in the "amenityIDs" object.
      $('.amenities h4').text(list.join(', '));
    }
  });

  // Sends a GET request to the API to check its status
  $.get(apiurl + ':5001/api/v1/status/', function (data) {

    // If the API responds with a status of 'OK', adds the
    // class 'available' to an HTML element with ID 'api_status'
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {

      // Otherwise, removes the class 'available' from the same element
      $('div#api_status').removeClass('available');
    }
  });

  // Sends a POST request to the API to retrieve data and appends
  // it to the HTML element with class 'places'
  $.ajax({
    type: 'POST',
    contentType: 'application/json',
    url: apiurl + ':5001/api/v1/places_search/',
    data: JSON.stringify({}),
    success: function (data) {
      $.each(data, function (index, place) {
        $('section.places').append('<article><div class="title_box"><h2>' + place.name + '</h2><div class="price_by_night">$' + place.price_by_night + '</div></div><div class="information"><div class="max_guest">' + place.max_guest + ' Guest(s)</div><div class="number_rooms">' + place.number_rooms + ' Bedroom(s)</div><div class="number_bathrooms">' + place.number_bathrooms + ' Bathroom(s)</div></div><div class="description">' + place.description + '</div></article>');
      });
    },
