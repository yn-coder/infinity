from bottle import route, run, template, error, default_app

def format_link( s_url, s_name ):
    return '<a href="' + s_url + '">' + s_name + '</a>'

FOOTER_HTML = '<hr><p>' + format_link( '/', 'Index' ) + '</p><p>' + format_link( 'https://github.com/yn-coder/infinity', 'Source code on GitHub' ) + '</p>'

# index page
@route('/')
def index():

#################плохой код

    s = '1'
    list = [ s, ]
    for i in range( 0, 19 ):
        s = s + '000'
        list.append( s )
    return template( 'index', list=list )

# 404 page
@error(404)
def error404(error):
    return template( '404' )

# List of internet urls for integer. Add new url here
URL_LIST = ( ( 'https://www.google.com/search?q={{i}}' , 'in Google' ),
             ( 'https://www.wolframalpha.com/input/?i={{i}}' , 'on WolframAlpha' ),
             ( 'http://www.sympygamma.com/input/?i={{i}}' , 'on SymPyGamma' ),
             ( 'https://duckduckgo.com/?q={{i}}' , 'in DuckDuckGo' ),
             ( 'https://en.wikipedia.org/w/index.php?search={{i}}' , 'in Wikipedia' ),
 )
 
# page for integers
@route('/<code>')
def pages(code):
    try:
        i = int(code)
        next = i + 1
        prev = i - 1
        
        # format list of links
        links = ''
        for ue in URL_LIST:
            links = links + '<li>' + format_link( ue[0], ue[1] ) + '</li>'
        # format page
        #'<h1>Number: {{i}}</h1>' +
        #             '<p>Something interesting about <strong>{{i}}</strong>:</p><ul>' +
        #             links +
        #             '</ul>' +
        #             '<h1>Neighbors</h1><p>' + format_link( '{{next}}', 'Next {{next}}' ) + '</p>', 
        #s = template( 'page', i = i, next = next )
        return template( 'page', i = i, next = next, prev = prev )
    except:
        #abort(404)
        #s = template('{{code}} not an integer', code=code)
        return template( 'page_not_int', code = code )

    #return s + FOOTER_HTML

if __name__ == "__main__":
    # Interactive mode
    print('debug')
    FOOTER_HTML = FOOTER_HTML + '<hr><strong>DEBUG</strong>'
    run(host='localhost', port=8080, reloader=True, debug=True)
else: 
    # production mode
    application = default_app()