$(function() {
	$(document).on('click', '.dropdown ul li', function() {
			var text = $(this).text();
			$(this).closest('.dropdown').find('button.dropdown-toggle .value').text(text);
	});

	$(document).on('click', '#button-search', function() {
		year = $("#select-year").text()
		category = $("#select-category").text()
		runtime = $("#select-runtime").text()
		movietype = $("#select-movietype").text()
		rating = $("#select-rating").text()

		$.ajax({
			url: "/api/search",
			type: 'GET',
			cache: false,
			data: {year: year, category: category, runtime: runtime, movietype: movietype, rating: rating},
		}).done(function(result){
				$('#search-result').html("");
				$('#search-result').css("min-height","500px");
				$('html, body').scrollTop( $(document).height() );

				$(result).hide().appendTo('#search-result').fadeIn(2000);

				//$('html, body').scrollTop( $(document).height() );
				//$('#search-result').html(result)
				
		}).fail(function (){
				alert('Ajax error happened.')
		});

	});
	// Zkusim stesti
	$('#lucky li').on('click', function() {
		var text = $(this).text();
		$('#lucky .value').data('value', text);
});
	$('#lucky li').on('click', function() {
		year = 2011
		category = $('#lucky .value').data('value')
		runtime = "vše"
		movietype = "film"
		rating = ">=5"

		$.ajax({
			url: "/api/search",
			type: 'GET',
			cache: false,
			data: {year: year, category: category, runtime: runtime, movietype: movietype, rating: rating},
		}).done(function(result){
				$('#search-result').html("");
				$('#search-result').css("min-height","500px");
				$('html, body').scrollTop( $(document).height() );

				$(result).hide().appendTo('#search-result').fadeIn(2000);

				//$('html, body').scrollTop( $(document).height() );
				//$('#search-result').html(result)
				
		}).fail(function (){
				alert('Ajax error happened.')
		});

	});


});