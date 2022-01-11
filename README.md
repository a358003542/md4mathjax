# md4mathjax
this is a python-markdown extension. basicly learning from the pelican plugin render-math. and i think inside its code, the mathjax extension split would be better.

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

