





#  [Creating a minimal Python application server forexperimenting](/en/blog/2016/02/17/minimal-python-wsgi-application-server/)

![Creating a minimal Python application server for experimenting](/static/devportal_uploaded/1fa616fb-1c41-480a-a504-4412353b1af3-uploads/zinnia/wsgi-snake.png)

I often find myself wanting to play around with a tiny Python web application
with native Python without installing any extra modules - the Python
developer's equivalent of creating an `index.html` and opening it in the
browser [just to play around withmarkup](http://www.yourhtmlsource.com/myfirstsite/myfirstpage.html).

For example, today I found myself wanting to inspect how the [Google APIClient Library for Python](https://developers.google.com/api-client-library/python/) handles requests, and a simple application server was all I
needed.

In these situations, the following minimal WSGI application, using the built-
in [wsgiref library](https://docs.python.org/2/library/wsgiref.html) is just
the ticket:

from wsgiref.simple_server import make_server

    
    def application(env, start_response):
        """
        A basic WSGI application
        """
    
        http_status = '200 OK'
        response_headers = [('Content-Type', 'text/html')]
        response_text = "Hello World"
    
        start_response(http_status, response_headers)
        return [response_text]
    
    if __name__ == "__main__":
        make_server('', 8000, application).serve_forever()

Put this in a file - e.g. `wsgi.py` - and run it with:

(I've also saved this [as aGist](https://gist.github.com/nottrobin/8c12c9921aeb885dbe07)).

This provides you with a very raw way of parsing HTTP requests. All the HTTP
variables come in as items in the `env` dictionary:

    
    def application(env, start_response):
        # To get the requested path
        # (the /index.html in http://example.com/index.html)
        path = env['PATH_INFO']
        
        # To get any query parameters
        # (the foo=bar in http://example.com/index.html?foo=bar)
        qs = env['QUERY_STRING']

What I often do from here is use [ipdb](https://pypi.python.org/pypi/ipdb) to
inspect incoming requests, or directly manipulate the response headers or
content.

Alternatively, if you're looking for something slightly more full-featured
(but still very lightweight) [tryFlask](http://flask.pocoo.org/docs/0.10/quickstart/).

(Also posted [over onrobinwinslow.uk](https://robinwinslow.uk/2016/02/14/simplest-wsgi-application/)).

[Robin Winslow](/en/blog/authors/nottrobin/)

Feb. 17, 2016

Filed under: [django](/en/blog/tags/django/) [python](/en/blog/tags/python/)
[webapps](/en/blog/tags/webapps/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





