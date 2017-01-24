from bottle import route, run, template, error, default_app

FOOTER_HTML = '<hr><p><a href="/">Index</a></p><p><a href="https://github.com/yn-coder/infinity">Source code on GitHub</a></p>'

@route('/')
def index():
    return '<h1>Infinite site</h1><p>Start <a href="1">at 1</a></p>' + FOOTER_HTML

@error(404)
def error404(error):
    return 'Nothing here, sorry' + FOOTER_HTML
    
GOOGLE_URL = '<p><a href="https://www.google.com/search?q={{i}}">Some interesting about {{i}} in Google</a></p>'
WOLFRAM_ALPHA_URL = '<p><a href="https://www.wolframalpha.com/input/?i={{i}}">Some interesting about {{i}} on WolframAlpha</a></p>'
DUCKDUCKGO_URL = '<p><a href="https://duckduckgo.com/?q={{i}}">Some interesting about {{i}} in DuckDuckGo</a></p>'
WIKI_URL = '<p><a href="https://en.wikipedia.org/w/index.php?search={{i}}">Some interesting about {{i}} in Wikipedia</a>'

@route('/<code>')
def pages(code):
    try:
        i = int(code)
        next = i + 1
        s = template('<h1>Code: {{i}}</h1>' +
                     GOOGLE_URL +
                     WOLFRAM_ALPHA_URL +                     
                     DUCKDUCKGO_URL +
                     WIKI_URL +
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