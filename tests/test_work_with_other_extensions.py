#!/usr/bin/env python
# -*-coding:utf-8-*-


import markdown

t_string = r"""


## t1

### t2

$inline1$

\(inline2\)

$$block-inline-1$$

\[block-inline-2\]

$$
block-1
$$

这里显示如何插入脚注[^1]


[^1]: 这是一个脚注。
"""

r_string = markdown.markdown(t_string, extensions=['footnotes', 'toc','md4mathjax'])

print(r_string)