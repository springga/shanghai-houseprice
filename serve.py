"""Serve content in the current directory over HTTPS."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import sys
import webbrowser

port = 2342

httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)

webbrowser.open("http://localhost:{}/xiaoqu.html".format(port))
print("[Ctrl+C to quit]")
httpd.serve_forever()
