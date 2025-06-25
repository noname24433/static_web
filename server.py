#!/usr/bin/env python3
import os
import http.server
import socketserver
import mimetypes

# Ensure CSS files are served with correct MIME type
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 5000))
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
