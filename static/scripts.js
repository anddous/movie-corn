$(function() {
	$(document).on('click', '.dropdown ul li', function() {
			var text = $(this).text();
			$(this).closest('.dropdown').find('button.dropdown-toggle .value').text(text);
	});

	$(document).on('click', '#button-search', function() {
		year = $("#select-year").text()
		//category = $("#select-category").text()
		//length = $("#select-year").text()
		//type = $("#select-year").text()

		$.ajax({
			url: "/api/search",
			type: 'GET',
			cache: false,
			data: {year: year},
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