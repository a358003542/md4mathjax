# md4mathjax
this is a python-markdown extension. basicly learning from the pelican plugin render-math. and i think inside its code, the mathjax extension split would be better.

This Extension is writing in the Python-Markdown Recommend way, so basically it's usage can reference the Python-Markdown Extension Usage document. 

本插件在写法是Python-Markdown的统一写法，因此使用可以参看Python-Markdown的插件使用文档。

原插件做了很多额外的工作，但现在mathjax对于数学公式写法上的支持已经很强大了，很多额外的工作都是没有必要的了。

本插件做的两个工作一就是检测markdown文档里面是否有数学公式，如果有则插入下面这段js代码。

```jinja
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [["$$", "$$"], ['\\[', '\\]']],
    packages: {
      '[+]': ['mhchem']
    }
  },
  loader: {
    load: ['[tex]/mhchem']
  },
}
</script>

<script id="MathJax-script" async src="{{SRC}}"></script>
```
这段代码用jinja2封装的，也就是后面可以进行更多的调配来提供对外参数接口。并没有在参数上额外封装，而直接是mathjax的配置，所以使用者直接参看mathjax文档即可。

本插件还有一个工作就是将检测到的数学公式封装进 `class=math` 的span或者div环境中。这给后续css调配提供了便利。

此外因为markdown的EscapeInlineProcessor机制存在，如果不进行处理 `\(...\)` `\[...\)` 这两个写法都会出错的，本插件经过处理将数学公式统一转为 `$...$` 和 `$$ ... $$` 这样的形式了。

很简单直观的一个插件，同时又完成了必要的工作。tests文件夹下可以有输出html文件参考。

## Usage
插件

## 参数
- auto_insert 默认True 是否根据文章有否数学公式来添加mathjax
- tag_class  默认 math
- mathjax_src 默认 https://cdn.jsdelivr.net/npm/mathjax@3.2.0/es5/tex-mml-chtml.js

## CHANGELOG
### 0.1.0
初步编写完成

pelican上使用：

```
MARKDOWN = {
    'extensions': [
        'md4mathjax'
    ],
}
```

