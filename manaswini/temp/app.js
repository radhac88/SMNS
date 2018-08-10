/*
	Response header info:
	Access-Control-Allow-Origin:*
	Content-Type:text/json
	X-Powered-By:nodejs
*/

var http 	= require('http');
var fs 		= require('fs');
var port 	= "1111" ;

http.createServer(function(request, response) {
 
    response.writeHead(200, {
        'Content-Type': 'text/json',
		'Access-Control-Allow-Origin': '*',
		'X-Powered-By':'nodejs'
    });


    fs.readFile('show_data.json', function(err, content){
        response.write(content);
        response.end();
    });

}).listen(port);

console.log("Listening on port " + port );