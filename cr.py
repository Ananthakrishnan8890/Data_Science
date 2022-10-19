import os

print("""
<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
 <meta name="Author" content="Made by 'tree'">
 <meta name="GENERATOR" content="$Version: $ tree v2.0.4 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
 <title>Directory Tree</title>
 <style type="text/css">
  BODY { font-family : monospace, sans-serif;  color: black;}
  P { font-family : monospace, sans-serif; color: black; margin:0px; padding: 0px;}
  A:visited { text-decoration : none; margin : 0px; padding : 0px;}
  A:link    { text-decoration : none; margin : 0px; padding : 0px;}
  A:hover   { text-decoration: underline; background-color : yellow; margin : 0px; padding : 0px;}
  A:active  { margin : 0px; padding : 0px;}
  .VERSION { font-size: small; font-family : arial, sans-serif; }
  .NORM  { color: black;  }
  .FIFO  { color: purple; }
  .CHAR  { color: yellow; }
  .DIR   { color: blue;   }
  .BLOCK { color: yellow; }
  .LINK  { color: aqua;   }
  .SOCK  { color: fuchsia;}
  .EXEC  { color: green;  }
 </style>
</head>
<body>
	<h1>Directory Tree</h1><p>
	<a href=".">.</a><br>
""")
b='cr.py'
c='cr.cmd'
d='.gitattributes'
e='.git'
f='index.html'
g='.gitignore'

for x in os.listdir():
    y=x.replace(" ","%20")
    if (x==b)|(x==c)|(x==d)|(x==e)|(x==f)|(x==g):
        continue
    else:
        print("|--<a href='./",y,"'>",x,"</a><br>",sep='')

print("""
<hr>
	<p class="VERSION">
		 tree v2.0.4 © 1996 - 2022 by Steve Baker and Thomas Moore <br>
		 HTML output hacked and copyleft © 1998 by Francesc Rocher <br>
		 JSON output hacked and copyleft © 2014 by Florian Sesser <br>
		 Charsets / OS/2 support © 2001 by Kyosuke Tokoro
	</p>
</body>
</html>
""")
