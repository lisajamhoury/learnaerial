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
		var checked = $('input[type=checkbox]:checked');
		console.log(checked);
	},
};