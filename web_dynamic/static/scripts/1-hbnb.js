$(document).ready(function () {
  // Creates an empty object called "newdict"
  const newdict = {};

  // Sets up an event listener that triggers when any checkbox input element
  // on the page changes
  $('input:checkbox').change(function () {

    // Checks if the checkbox that was just changed is currently checked
    if ($(this).is(':checked')) {

      // Adds a new key-value pair to the "newdict" object, where the key is the
      // value of the "data-name" attribute of the checkbox and the value is the
      // value of the "data-id" attribute of the checkbox.
      newdict[$(this).attr('data-name')] = $(this).attr('data-id');
    } else {

      // Removes the corresponding key-value pair from the "newdict" object if
      // the checkbox is unchecked.
      delete newdict[$(this).attr('data-name')];
    }

    // Creates an empty array called "list"
    const list = [];

    // Iterates over the "newdict" object using the $.each() method. For each
    // key-value pair in the object, the function passed to $.each() pushes the
    // key onto the "list" array.
    $.each(newdict, function (index, value) {
      list.push(index);
    });

    // Updates the text inside an HTML element with class "amenities h4" to
    // show the list of selected checkboxes.
    if (list.length === 0) {

      // If there are no checkboxes selected (i.e. the "list" array is empty),
      // then the text is set to a non-breaking space.
      $('.amenities h4').html('&nbsp');
    } else {

      // Otherwise, the text is set to a comma-separated string of the keys in
      // the "newdict" object.
      $('.amenities h4').text(list.join(', '));
    }
  });
});
