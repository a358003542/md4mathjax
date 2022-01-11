#!/usr/bin/env python
# -*-coding:utf-8-*-

import markdown

t_string = r"""

$inline1$

\(inline2\)

$$block-inline-1$$

\[block-inline-2\]

$$
block-1
$$

"""

r_string = markdown.markdown(t_string, extensions=['md4mathjax'])

print(r_string)