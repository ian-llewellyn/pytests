## Server does this
def start_response_func(status, response_headers, exc_info=None):
    print status
    for header in response_headers:
        print header[0], header[1]

environ_dict = {"DISPLAY": "0", "PYTHONPATH": "/usr/lib64/python2.6"}

## Django does this
class ApplicationObject():
    def __call__(self, environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ["1\n", "2\n", "3\n", "4\n", "5\n"]

application = ApplicationObject()

## Server does this
print application(environ_dict, start_response_func)
