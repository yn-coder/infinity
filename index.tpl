% rebase('base.tpl', title='Page Title')

<h1>Infinite site</h1>

<p>Start here:</p>
<ul>
  % l = '1'
  % n = l
  % for i in range(0,24):
    <li><a href="{{l}}">{{n}}</a></li>
  % l = l + '000'
  % n = n + ' 000'
  % end
</ul>