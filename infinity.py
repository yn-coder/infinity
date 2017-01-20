from bottle import route, run, template, error

@route('/')
def index():
    return '<h1>Infinite site</h1><p>Start at <a href="1">1</a></p>'

@error(404)
def error404(error):
    return 'Nothing here, sorry'
    
@route('/<code>')
def index(code):
    try:
        i = int(code)
        next = i + 1
        #s = '%i %i' % (i,i)
        s = template('<h1>Code: {{i}}</h1><p><a href="https://www.google.com/search?q={{i}}">Some interesting about {{i}} in Google</a></p><p><a href="https://www.wolframalpha.com/input/?i={{i}}">Some interesting about {{i}} on WolframAlpha</a></p><h1>Next</h1><p><a href="{{next}}">Next {{next}}</a></p>', i = i, next = next )
    except:
        #abort(404)
        s = template('{{code}} not an integer', code=code)

    return s + '<hr><p><a href="/">Index</a></p>'

run(host='localhost', port=8080, reloader=True)