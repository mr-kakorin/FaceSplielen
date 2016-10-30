var app = require('express')();
var path = require('path');
var fs = require('fs');
var bodyParser = require('body-parser');
var spawn = require('child_process').spawn;
var upload = require('multer')({
	dest: path.resolve( __filename+'/../../../Destination/uploads' ),
	limits: {
		fileSize: 2*1024*1024
	}
});
var vision = require('@google-cloud/vision')({
	projectId: 'facespielen',
	keyFilename: path.resolve(__filename+'/../keyfile.json')
});

app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(bodyParser.json({limit: '50mb'}));

app.get( '/' , function ( req , res ) {
	console.log( __filename+'/../public/idex.html');
	res.sendFile( path.resolve( __filename + '/../../public/index.html' ) );
});

app.post ( '/run', upload.single('file'), function ( req, res ) {

	console.log('Загрузка файла: ', req.file.path);

	vision.detectFaces( 
		path.resolve( __filename+'/../../../Destination/uploads/'+req.file.filename ),
		function ( err, faces ) {
			if (err) {
				console.log('Ошибка определения лиц: ', err);
			} else {

				console.log('Лица определены.');

				fs.writeFile( 
					path.resolve( __filename+'/../../../Destination/json/'+req.file.filename ),
					JSON.stringify(faces),
					function (err) {

						if (err) {
							console.log( 'Ошибка записи JSON-файла: ', err );
						} else if (false) {

							var proccess = spawn(
								'python',
								[path.resolve(__filename+'/../../../Source/FaceTransform/FaceTransform/FS_engine.py'), req.file.filename]
								);

							process.stdout.on('data', function (data) {

								console.log('Python процесс вернул: ', data);
							});

							process.stderr.on('data', function (data) {
							  console.log("Python ошибка:", data);
							});

							process.on('close', function (code) {
								console.log('Python процесс завершен с кодом ', code);

								res.send({
									success: true
								});	
							});
						} else {

							res.send({
								success: true,
								filename: req.file.filename
							});
						}
					}
				);
			}
		}
	);
});

app.post ( '/run_base64', function ( req, res ) {

	var name='img'+(new Date()).getTime();
	fs.writeFile(path.resolve(__filename+'/../../../Destination/uploads/'+name), req.body.imgBase64, 'base64', function (err) {
		if (err) res.send('error'); else {
			vision.detectFaces( 
				path.resolve( __filename+'/../../../Destination/uploads/'+name ),
				function ( err, faces ) {
					if (err) {
						console.log('Ошибка определения лиц: ', err);
					} else {

						console.log('Лица определены.');

						fs.writeFile( 
							path.resolve( __filename+'/../../../Destination/json/'+name ),
							JSON.stringify(faces),
							function (err) {

								if (err) {
									console.log( 'Ошибка записи JSON-файла: ', err );
								} else if (false) {

									var proccess = spawn(
										'python',
										[path.resolve(__filename+'/../../../Source/FaceTransform/FaceTransform/FS_engine.py'), name]
										);

									process.stdout.on('data', function (data) {

										console.log('Python процесс вернул: ', data);
									});

									process.stderr.on('data', function (data) {
									  console.log("Python ошибка:", data);
									});

									process.on('close', function (code) {
										console.log('Python процесс завершен с кодом ', code);

										res.send({
											success: true
										});	
									});
								} else {

									res.send({
										success: true,
										filename: name
									});
								}
							}
						);
					}
				}
			);			
		}
	})


});

app.get('/result', function (req, res) {
	var filename = req.query.filename;

	res.sendFile(path.resolve(__filename+'/../../../Destination/uploads/'+filename));
});

app.listen( 8097, function () {
	console.log( 'Server started!' );
});