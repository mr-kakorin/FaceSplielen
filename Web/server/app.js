var app = require('express')();
var path = require('path');
var fs = require('fs');
var upload = require('multer')({
	dest: path.resolve( '../../Destination/uploads' ),
	limits: {
		fileSize: 2*1024*1024
	}
});
var vision = require('@google-cloud/vision')({
	projectId: 'facespielen',
	keyFilename: path.resolve('keyfile.json')
});

app.get( '/' , function ( req , res ) {
	res.sendFile( path.resolve( '../public/index.html' ) );
});

app.post ( '/run', upload.single("photo"), function ( req, res ) {

	console.log('Загрузка файла: ', req.file.path);

	vision.detectFaces( 
		path.resolve( '../../Destination/uploads/'+req.file.filename ),
		function ( err, faces ) {
			if (err) {
				console.log('Ошибка определения лиц: ', err);
			} else {

				console.log('Лица определены.');

				fs.writeFile( 
					path.resolve( '../../Destination/json/'+req.file.filename ),
					JSON.stringify(faces),
					function (err) {

						if (err) {
							console.log( 'Ошибка записи JSON-файла: ', err );
						} else {

							res.send({
								success: true
							});
						}
					}
				);
			}
		}
	);
});

app.listen( 8097, function () {
	console.log( 'Server started!' );
});