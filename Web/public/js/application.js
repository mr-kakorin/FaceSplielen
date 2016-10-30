
$( document ).ready( function () {

	var ShowResults = function (id) {
		$('.windows').hide();
		$("#Result").show();
		$("#Result").removeClass('deactive');

		var source = new Image();
		source.src = '/result?type=uploads&filename='+id;

		var result = new Image();
		result.src = '/result?type=results&filename='+id+'.jpg';

		$('#SourcePhoto').append($(source));
		$("#ResPhoto").append($(result));

		$.get('/result?type=result&filename='+id).then(function(data) {
			console.log(data);
		}).then(function() {

		});
	}

	$("#ClickCamera").click( function () {
		// Grab elements, create settings, etc.
		var video = document.getElementById('video');

		// Get access to the camera!
		navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;
		if(navigator.getUserMedia) {
		    // Not adding `{ audio: true }` since we only want video now
		    navigator.getUserMedia({video: true}, function (stream){
		    	video.src = window.URL.createObjectURL(stream);
		    	video.play();
		    }, function () {

		    });
		} else {
			console.log('false video', navigator.mediaDevices, navigator.getUserMedia);
		}
	});
	$("#SnapPhoto").click(function () {
		var video = document.getElementById('video');
		var photo = document.getElementById('photo').getContext('2d');
		$("#dphoto").show();
		photo.drawImage(video, 0, 0, 580, 480);
		$(video).hide();
		$('#SnapPhoto').text("Отправить фото").addClass("SEND_PHOTO");
	});

	$("body").on('click', '.SEND_PHOTO', function () {
		var photo = document.getElementById('photo');
		var data = photo.toDataURL();
		console.log(data);

	    $.ajax({
	        url: "/run_base64",
	        type: 'POST',
	        data: {
	        	imgBase64: data
	        },
	        success: function (data) {
	        	ShowResults(data.filename);
	        }
	    });		
	});

	$("body").on("click", ".btn_route", function (evt) {
		var route = $(evt.target).attr('route');
		console.log(route);


		$('.windows').hide(400);
		$('#window_'+route).show(400);
	});

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
	        	ShowResults(data.filename);
	        },
	        cache: false,
	        contentType: false,
	        processData: false
	    });

		return false;
	});

	$('.myUploader .simform').click(function () {
		console.log('ok');
		$('.myUploader input[type=file]').trigger('click');
		return false;
	});

	$('.myUploader .simform').on("dragenter dragstart dragend dragleave dragover drag drop", function (e) {
	    e.preventDefault();
	});

	var area = $('.myUploader .simform').get(0);
	area.ondragover = function () {
		$(area).addClass('hover');
		console.log('ondragover');
	}
	area.ondragleave = function () {
		$(area).removeClass('hover');
	}
	area.ondrop = function (event) {
		console.log('DROP');
		$(area).removeClass('hover');
		var file = event.dataTransfer.files[0];
		console.log(file)
        
		var formData = new FormData();
		formData.append("file", file);
	    $.ajax({
	        url: "/run",
	        type: 'POST',
	        data: formData,
	        async: false,
	        success: function (data) {
	        	ShowResults(data.filename);
	        },
	        cache: false,
	        contentType: false,
	        processData: false
	    });
	}

	$("#InputFile").change( function (evt) {
		console.log("Change!");
		var formData = new FormData($("#UploadFileForm")[0]);
	    $.ajax({
	        url: "/run",
	        type: 'POST',
	        data: formData,
	        async: false,
	        success: function (data) {
	        	ShowResults(data.filename);
	        },
	        cache: false,
	        contentType: false,
	        processData: false
	    });

		return false;
	})

});