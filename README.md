# md4mathjax
this is a python-markdown extension. basicly learning from the pelican plugin render-math. and i think inside its code, the mathjax extension split would be better.

原插件做了很多额外的工作，但现在mathjax对于数学公式写法上的支持已经很强大了，很多额外的工作都是没有必要的了。

本插件做的两个工作一就是检测markdown文档里面是否有数学公式，如果有则插入mathjax的js支持代码。

本插件还有一个工作就是因为markdown的EscapeInlineProcessor机制存在， `\(...\)` `\[...\)` 这两个写法会被安全处理为`(...) [...]`，按照markdown文档转义字符设计，这是没有问题的，应该不会变动了。本插件通过正则判定某段确实是数学字符，行 `\(...\)` 会更改为 `\\(...\\)` ，而 `\[...\]` 会被更改为 `$$...$$`。

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
### mathjax_src
default: `https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js`


### mathjax_id
default: `MathJax-script`

### mathjax_settings
default:

```
DEFUALT_MATHJAX_SETTING = r"""
window.MathJax = {}
"""
```

In python assign this value do not forget the prefix `r` .


## CHANGELOG
### 0.2.0
程序处理流程进一步简化，不再用span或者div封装，只专注于解决因为转义而出现的问题和mathjax相关js代码的自动注入。

不再对 `$...$` 这样的写法默认支持，这样的写法也不是很推荐，如果之前有大量的文档采用了这种写法，那么配置需要做如下更改：

```
{'md4mathjax': {
    'mathjax_settings': r"""
    window.MathJax = {
              tex: {
                inlineMath: {'[+]': [['$', '$']]}
              }
            };
         """
     }}
```
来继续保持对 `$...$` 原来写法的支持。

原来默认增加了对 `mhchem` 的支持，现在默认没有增加了，你需要按照mathjax官方文档的说明，增加这样的配置：

```
window.MathJax = {
  loader: {load: ['[tex]/mhchem']},
  tex: {packages: {'[+]': ['mhchem']}}
};
```

然后现在默认源使用的mathjax的V4版本。


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