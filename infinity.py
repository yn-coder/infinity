from bottle import route, run, template, error, default_app
import markdown
import os

# index page
@route('/')
def index():
    return template( 'index' )

# 404 page
@error(404)
def error404(error):
    return template( '404' )

# page for integers
@route('/<code>')
def pages(code):
    try:
        i = int(code)
        next = i + 1
        prev = i - 1

        try:            
            f = open( os.path.join( 'int', code, '.md' ), 'r')
            md_html = markdown.markdown( f.read() )
        except:
            md_html = 'fail'

        return template( 'page', i = i, next = next, prev = prev, md_html = md_html )
    except:
        #abort(404)
        return template( 'page_not_int', code = code )

if __name__ == "__main__":
    if os.environ.get('PYTHON_DEBUG') == '1':
        # Interactive mode
        print('debug')
        run(host='localhost', port=8080, reloader=True, debug=True)
    else:
        # production mode
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
