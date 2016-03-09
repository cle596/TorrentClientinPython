//e

var http = require('http');

var server = http.createServer(function(request, response) {
    console.log(request.headers);
    response.write("hey");
    console.log(response);
    response.end();
}).listen(8000);
