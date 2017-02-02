% rebase('base.tpl', title=str(i) + ' - ')

<h1>Infinite site, page about {{i}}</h1>

<p>Something interesting about <code>{{i}}</code>:</p>

<ul><li><a href="https://www.google.com/search?q={{i}}">in Google</a></li>
<li><a href="https://www.wolframalpha.com/input/?i={{i}}">on WolframAlpha</a></li>
<li><a href="http://www.sympygamma.com/input/?i={{i}}">on SymPyGamma</a></li>
<li><a href="https://duckduckgo.com/?q={{i}}">in DuckDuckGo</a></li>
<li><a href="https://en.wikipedia.org/w/index.php?search={{i}}">in Wikipedia</a></li></ul>

<h1>Neighbors</h1>
<p><a href="{{prev}}">Prev {{prev}}</a></p>
<p><a href="{{next}}">Next {{next}}</a></p>