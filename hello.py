def parse_query(query):
    return '\n'.join(query.split('&'))


def wsgi_hello(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = parse_query(environ['QUERY_STRING'])

    start_response(status, headers)
    return [body]
