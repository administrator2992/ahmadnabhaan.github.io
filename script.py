import http.server
import socketserver
import traceback
import sys

PORT = 9090
DIRECTORY = "output"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    try: 
        httpd.allow_reuse_address = True
        httpd.serve_forever()
    except:
        httpd.server_close()
    

# def shutdown():
#     global httpd
#     global please_die
#     print("Shutting down")

#     try:
#         please_die.wait() # how do you do? 
#         httpd.shutdown() # Stop the serve_forever
#         httpd.server_close() # Close also the socket.
#     except Exception:
#         traceback.print_exc(file=sys.stdout)