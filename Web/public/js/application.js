
$( document ).ready( function () {

	console.log("Web page is ready!");

	// Перехват субмита форма
	$("#MainForm").submit( function (event) {

		console.log("Submit form!");

		var formData = new FormData($(this)[0]);
	    $.ajax({
	        url: "/run",
	        type: 'POST',
	        data: formData,
	        async: false,
	        success: function (data) {
	            console.log(data)
			    var img = new Image();
			    img.src="/result?filename="+data.filename;
			    img.onload = function () {
			        $("#Result").append($(img));
			    }
	        },
	        cache: false,
	        contentType: false,
	        processData: false
	    });

		return false;
	});

});