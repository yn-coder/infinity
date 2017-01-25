from bottle import route, run, template, error, default_app

FOOTER_HTML = '<hr><p><a href="/">Index</a></p><p><a href="https://github.com/yn-coder/infinity">Source code on GitHub</a></p>'

@route('/')
def index():
    return '<h1>Infinite site</h1><p>Start <a href="1">at 1</a></p>' + FOOTER_HTML

@error(404)
def error404(error):
    return 'Nothing here, sorry' + FOOTER_HTML
    
GOOGLE_URL = '<li><a href="https://www.google.com/search?q={{i}}">in Google</a></li>'
WOLFRAM_ALPHA_URL = '<li><a href="https://www.wolframalpha.com/input/?i={{i}}">on WolframAlpha</a></li>'
DUCKDUCKGO_URL = '<li><a href="https://duckduckgo.com/?q={{i}}">in DuckDuckGo</a></li>'
WIKI_URL = '<li><a href="https://en.wikipedia.org/w/index.php?search={{i}}">in Wikipedia</a></li>'

@route('/<code>')
def pages(code):
    try:
        i = int(code)
        next = i + 1
        s = template('<h1>Code: {{i}}</h1>' +
                     '<p>Something interesting about <strong>{{i}}</strong>:</p><ul>' +
                     GOOGLE_URL +
                     WOLFRAM_ALPHA_URL +                     
                     DUCKDUCKGO_URL +
                     WIKI_URL +
                     '</ul>' +
                     '<h1>Next</h1><p><a href="{{next}}">Next {{next}}</a></p>', i = i, next = next )        
    except:
        #abort(404)
        s = template('{{code}} not an integer', code=code)

    return s + FOOTER_HTML

if __name__ == "__main__":
    # Interactive mode
    print('debug')
    FOOTER_HTML = FOOTER_HTML + '<hr><strong>DEBUG</strong>'
    run(host='localhost', port=8080, reloader=True)
else: 
    # production mode
    application = default_app()