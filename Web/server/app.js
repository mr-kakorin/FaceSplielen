var app = require('express')();
var path = require('path');
var fs = require('fs');
var bodyParser = require('body-parser');
var spawn = require('child_process').spawn;
var upload = require('multer')({
	dest: path.resolve( __filename+'/../../Destination/uploads' ),
	limits: {
		fileSize: 2*1024*1024
	}
});
var vision = require('@google-cloud/vision')({
	projectId: 'facespielen',
	keyFilename: path.resolve(__filename+'/keyfile.json')
});

app.get( '/' , function ( req , res ) {
	res.sendFile( path.resolve( __filename + '/../public/index.html' ) );
});

app.post ( '/run', upload.single("photo"), function ( req, res ) {

	console.log('Загрузка файла: ', req.file.path);

	vision.detectFaces( 
		path.resolve( __filename+'/../../Destination/uploads/'+req.file.filename ),
		function ( err, faces ) {
			if (err) {
				console.log('Ошибка определения лиц: ', err);
			} else {

				console.log('Лица определены.');

				fs.writeFile( 
					path.resolve( __filename+'/../../Destination/json/'+req.file.filename ),
					JSON.stringify(faces),
					function (err) {

						if (err) {
							console.log( 'Ошибка записи JSON-файла: ', err );
						} else if (false) {

							var proccess = spawn(
								'python',
								[path.resolve(__filename+'/../../Source/FaceTransform/FaceTransform/FS_engine.py'), req.file.filename]
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

app.get('/result', function (req, res) {
	var filename = req.query.filename;

	res.sendFile(path.resolve(__filename+'/../../Destination/uploads/'+filename));
});

app.listen( 8097, function () {
	console.log( 'Server started!' );
});