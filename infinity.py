from bottle import route, run, template, error, default_app

def format_link( s_url, s_name ):
    return '<a href="' + s_url + '">' + s_name + '</a>'

FOOTER_HTML = '<hr><p>' + format_link( '/', 'Index' ) + '</p><p>' + format_link( 'https://github.com/yn-coder/infinity', 'Source code on GitHub' ) + '</p>'

# index page
@route('/')
def index():
    return '<h1>Infinite site</h1><p>Start ' + format_link( '1', 'at 1' ) + '</p>' + FOOTER_HTML

# 404 page
@error(404)
def error404(error):
    return 'Nothing here, sorry' + FOOTER_HTML

# List of internet urls for integer. Add new url here
URL_LIST = ( ( 'https://www.google.com/search?q={{i}}' , 'in Google' ),
             ( 'https://www.wolframalpha.com/input/?i={{i}}' , 'on WolframAlpha' ),
             ( 'https://duckduckgo.com/?q={{i}}' , 'in DuckDuckGo' ),
             ( 'https://en.wikipedia.org/w/index.php?search={{i}}' , 'in Wikipedia' ),
 )
 
# page for integers
@route('/<code>')
def pages(code):
    try:
        i = int(code)
        next = i + 1
        
        # format list of links
        links = ''
        for ue in URL_LIST:
            links = links + '<li>' + format_link( ue[0], ue[1] ) + '</li>'
        # format page
        s = template('<h1>Code: {{i}}</h1>' +
                     '<p>Something interesting about <strong>{{i}}</strong>:</p><ul>' +
                     links +
                     '</ul>' +
                     '<h1>Next</h1><p>' + format_link( '{{next}}', 'Next {{next}}' ) + '</p>', i = i, next = next )
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