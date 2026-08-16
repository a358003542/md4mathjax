#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
对旧有大量 $...$ 的继续支持测试


"""
MARKDOWN = {
    'extensions': [
        'md4mathjax'
    ],
}

import markdown
from md4mathjax import Md4MathjaxExtension

with open('example2.md', encoding='utf8', mode='rt') as f:
    t_string = f.read()

    r_string = markdown.markdown(t_string, extensions=['md4mathjax'],
                                 extension_configs={'md4mathjax': {
                                     'mathjax_settings': r"""
                                     window.MathJax = {
                                          tex: {
                                            inlineMath: {'[+]': [['$', '$']]}
                                          }
                                        };
                                     """
                                 }})


with open('example2.html', encoding='utf8', mode='wt') as f:
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
