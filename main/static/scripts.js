function lidarComCheckbox(checkbox, url) {
	$(document).ready(function() {
		$(checkbox).change(function() {
			$.ajax({
				url: url,
				type: 'POST',
				data: {
					'checkbox_funcao': $(this).is(':checked')
				},
				success: function(response) {
					console.log(response);
				},
				error: function(error) {
					console.log(error);
				}
			});
		});
	});
}