from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Docker App</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    padding: 50px;
                    background: #667eea;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <h1>My First Dockerized App!</h1>
            <p>Current time: {datetime.now()}</p>
            <p>Running inside a Docker container</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print('Server running on port 8080...')
    server.serve_forever()
