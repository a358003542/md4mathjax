#!/usr/bin/env python
# -*-coding:utf-8-*-


import markdown
from md4mathjax import Md4MathjaxExtension

with open('example.md', encoding='utf8', mode='rt') as f:
    t_string = f.read()

    r_string = markdown.markdown(t_string, extensions=[Md4MathjaxExtension()])

with open('example.html', encoding='utf8', mode='wt') as f:
    html = """
    <!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>MathJax example</title>
</head>
<body>
{content}
</body>
</html>""".format(content=r_string)

    print(html, file=f)
