from bottle import route, run, template, error

@route('/')
def index():
    return '<h1>Infinite site</h1><p><a href="1">1</a></p>'

@error(404)
def error404(error):
    return 'Nothing here, sorry'
    
@route('/<code>')
def index(code):
    try:
        i = int(code)
        next = i + 1
        #s = '%i %i' % (i,i)
        s = '<h1>Code: %i</h1><p><a href="%i">%i</a></p>' % (i, next, next )
    except:
        #abort(404)
        s = template('{{code}} not an integer', code=code)

    return s + '<p><a href="/">Index</a></p>'

run(host='localhost', port=8080, reloader=True)