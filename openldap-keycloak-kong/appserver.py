#!/usr/bin/python
import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

host = os.getenv('HOST', '0.0.0.0')
port = int(os.getenv('PORT', 80))

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer((host, port), myHandler)
    print 'Started httpserver on port ' , port
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    