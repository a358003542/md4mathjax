# md4mathjax
this is a python-markdown extension. basicly learning from the pelican plugin render-math. and i think inside its code, the mathjax extension split would be better.

原插件做了很多额外的工作，但现在mathjax对于数学公式写法上的支持已经很强大了，很多额外的工作都是没有必要的了。

本插件做的两个工作一就是检测markdown文档里面是否有数学公式，如果有则插入下面这段js代码。

本插件还有一个工作就是将检测到的数学公式封装进 `class=math` 的span或者div环境中。这给后续css调配提供了便利。

此外因为markdown的EscapeInlineProcessor机制存在，如果不进行处理 `\(...\)` `\[...\)` 这两个写法都会出错的，本插件经过处理将数学公式统一转为 `$...$` 和 `$$ ... $$` 这样的形式了。

很简单直观的一个插件，同时又完成了必要的工作。tests文件夹下可以有输出html文件参考。

## Usage
This Extension is writing in the Python-Markdown Recommend way, so basically it's usage can reference the Python-Markdown Extension Usage document. 

本插件在写法是Python-Markdown的统一写法，因此使用可以参看Python-Markdown的插件使用文档。

### in pelican

```
MARKDOWN = {
    'extensions': [
        'md4mathjax'
    ],
}
```

## 参数
### auto_insert 
default True 

是否根据文章有否数学公式来添加mathjax

based on the markdown file does have the math equations to decide whether add the mathjax
script

### tag_class  
default math

like 
```
<div class="math">$\pi$</div>
```

### mathjax_src
default https://cdn.jsdelivr.net/npm/mathjax@3.2.0/es5/tex-mml-chtml.js

### mathjax_id
default MathJax-script

### mathjax_settings

default 

```
DEFUALT_MATHJAX_SETTING = r"""
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
"""
```

In python assign this value do not forget the prefix `r` .


## CHANGELOG
### 0.1.3
fix escape issue.

### 0.1.2
README 

### 0.1.1
解决了和toc插件不兼容的问题。

fixed a problem which is conflicted with the toc extension

### 0.1.0
初步编写完成

project started