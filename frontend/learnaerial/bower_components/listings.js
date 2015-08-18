var GRID = {
	initialize: function() {
		GRID.grid = $('#listings_grid').isotope({
			itemsSelector: 'li',
		});

		//get all the checkboxes
		var checkboxes = $('input[type=checkbox]');

		//when checkbox clicked, we update filters
		checkboxes.on('change', GRID.updateFilters);
	},

	updateFilters: function(event) {
		event.preventDefault();

		// var checked = $('input[type=checkbox]:checked');

		// Using similar code as above get all checked inside categories
		// var checkedCategories = $(................................);

		// Using similar code as above get all checked inside offerings
		// var checkedOfferings = $(......................................);

		// Using similar code as above get all checked inside cities
		// var checkedCities = $(.......................................);

		// Get the filter names for each group of checked checkboxes

		// var categoriesFilterList = GRID.getFilterListFromChecked(checkedCategories);
		// var offeringsFilterList = GRID.getFilterListFromChecked(checkedOfferings);
		// var citiesFilterList = GRID.getFilterListFromChecked(checkedCities);


		// NOOOOOOW here is the hard bit
		// We need every possible combination of each of the items in all three arrays above
		// Soooo let's say we ahve
		// ['.taco', '.burrito']  AND we have ['.spicy', '.mild'] AND ['.small', '.large']
		// We need to turn it into:
		// ['.taco.spicy.small', '.taco.spicy.large', '.taco.mild.small', '.taco.mild.large', '.burrito.spicy.small', ..... ETC ETC ETC ... ]
		// Sooo most people recommend using recursion for that, but it might be a bit too complicated for you to grasp
		// (see http://stackoverflow.com/questions/4331092/finding-all-combinations-of-javascript-array-values)

		// Imma stop here because I need to do work now ... but hopefully you can get a bit further.
	},

	getFilterListFromChecked: function(checked) {
		// This function accepts an array of input boxes, and returns an array of strings
		// that correspond to the filter that will be used in Isotope
		// Given an list of inputs like this:
		// [<input type="checkbox" data-filter-group="city" data-filter-slug="new-york">, [<input type="checkbox" data-filter-group="city" data-filter-slug="frenchtown">,]
		// We return:
		// ['.city-new-york', '.city-frenchtown']

		// To do this, we must first LOOP through all of the things inside the 'checked' variable
		// USE THIS: http://api.jquery.com/jquery.each/

		// Create a variable that will store your results

		var filterList = [];

		// Now start your LOOP here
		{
			// Inside your loop, you push first make the string
			// var filter = '.' + $() + '-' + $() // Jquery Magic to get the value for data-filter-group and value for data-filter-slug hint: https://api.jquery.com/jquery.data/
			// filterList.push(filter) // here filter should look something like '.city-new-york'
		}

		return filterList

	}
};
