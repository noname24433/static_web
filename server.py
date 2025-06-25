#!/usr/bin/env python3
"""
Simple HTTP server for serving static files on Render
"""
import os
import http.server
import socketserver
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def guess_type(self, path):
        """Override to ensure correct MIME types"""
        mime_type, encoding = super().guess_type(path)
        
        # Ensure CSS files are served with correct MIME type
        if path.endswith('.css'):
            return 'text/css', encoding
        elif path.endswith('.js'):
            return 'application/javascript', encoding
        elif path.endswith('.html'):
            return 'text/html', encoding
            
        return mime_type, encoding

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 5000))
    
    # Change to the directory containing static files
    web_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(web_dir)
    
    Handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT}")
        httpd.serve_forever()
