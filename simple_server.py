from http.server import HTTPServer, SimpleHTTPRequestHandler

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 20219), SimpleHTTPRequestHandler)
    server.serve_forever()