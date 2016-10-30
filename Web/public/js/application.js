
$( document ).ready( function () {


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

	    $.ajax({
	        url: "/run",
	        type: 'POST',
	        data: {
	        	imgBase64: data
	        },
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
        
		var xhr = new XMLHttpRequest();
		xhr.upload.addEventListener('progress', uploadProgress, false);
		xhr.onreadystatechange = stateChange;
		xhr.open('POST', '/run');
		xhr.setRequestHeader('X-FILE-NAME', file.name);
		xhr.send(file);

		function uploadProgress(event) {
		    var percent = parseInt(event.loaded / event.total * 100);
		   $(area).text('Загрузка: ' + percent + '%');
		}

		function stateChange(event) {
		    if (event.target.readyState == 4) {
		        if (event.target.status == 200) {
		            $(area).text('Загрузка успешно завершена!');
		        } else {
		            $(area).text('Произошла ошибка!');
		            $(area).addClass('error');
		        }
		    }
		}
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
	        	$("#window_FileUpload").hide();
	        	$("#Result").removeClass("deactive");
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
	})
/*
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

*/

});