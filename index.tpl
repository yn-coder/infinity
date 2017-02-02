% rebase('base.tpl', title='Page Title')

<h1>Infinite site</h1>

<p>Start here:</p>
<ul>
  % for item in list:
    <li><a href="{{item}}">{{item}}</a></li>
  % end
</ul>