var GRID = {
  initialize: function() {
    GRID.grid = $('#listings_grid').isotope({
      itemsSelector: 'li',
    });

    //get all the checkboxes
    var checkboxes = $('input[type=checkbox]');

    //when checkbox clicked, we update filters
    checkboxes.on('change', GRID.updateFilters);

    //show and hide more filters 
    var showMore = $('.showmore');
    var showLess = $('.showless');
    var parent = null;

    showMore.click(function(event) {
      event.preventDefault();
      parent = $(this).parents('ul');
      parent.find('.showmore').hide();
      parent.find('.more-filters').show();
    });

    showLess.click(function(event) {
      event.preventDefault();
      parent = $(this).parents('ul');
      parent.find('.more-filters').hide();
      parent.find('.showmore').show();


    });
  },

  updateFilters: function(event) {
    event.preventDefault();

    // Using similar code as above get all checked inside categories
    var checkedCategories = $('.categories input[type=checkbox]:checked');

    // Using similar code as above get all checked inside offerings
    var checkedOfferings = $('.offerings input[type=checkbox]:checked');

    // Using similar code as above get all checked inside cities
    var checkedCities = $('.location input[type=checkbox]:checked');

    // console.log(checkedCategories);
    // console.log(checkedOfferings);
    // console.log(checkedCities);

    // Get the filter names for each group of checked checkboxes

    var categoriesFilterList = GRID.getFilterListFromChecked(checkedCategories);
    var offeringsFilterList = GRID.getFilterListFromChecked(checkedOfferings);
    var citiesFilterList = GRID.getFilterListFromChecked(checkedCities);

    // Add categories and offerings
    var allFilterList = categoriesFilterList.concat(offeringsFilterList);

    // If city filters checked, create one query for each city
    if (citiesFilterList.length) {
      var collectFilters = [];
      var allFilters;

      for (i = 0; i < citiesFilterList.length; i++) {
        var eachCityFilterList = allFilterList.concat(citiesFilterList[i]);
        var eachCityFilter = eachCityFilterList.join('');

        // Create array of filters per city
        collectFilters.push(eachCityFilter);
      }

      // Join filters with comma separation to indicate OR for each city
      allFilters = collectFilters.join(', ');

    } else {
      // Otherwise just join all filters
      allFilters = allFilterList.join('');
    }

    GRID.grid.isotope({
      filter: allFilters
    });

  },

  getFilterListFromChecked: function(checked) {
    // This function accepts an array of input boxes, and returns an array of strings
    // that correspond to the filter that will be used in Isotope
    // Given a list of inputs like this:
    // [<input type="checkbox" data-filter-group="city" data-filter-slug="new-york">, [<input type="checkbox" data-filter-group="city" data-filter-slug="frenchtown">,]
    // We return:
    // ['.city-new-york', '.city-frenchtown']

    // To do this, we must first LOOP through all of the things inside the 'checked' variable
    // USE THIS: http://api.jquery.com/jquery.each/

    // Create a variable that will store your results

    var filterList = [];

    // Now start your LOOP here
    $.each(checked, function(index, value) {

      // Inside your loop, you first make the string
      var filter = '.' + $(value).data('filter-group') + '-' + $(value).data('filter-slug');
      //console.log(filter);
      // Jquery Magic to get the value for data-filter-group and value for data-filter-slug hint: https://api.jquery.com/jquery.data/

      filterList.push(filter);
    });

    return filterList

  }
};