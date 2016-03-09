var http = require('http');

var server = http.createServer(function(request, response) {
    response.end("LAAAAAAH");
}).listen(8000);
