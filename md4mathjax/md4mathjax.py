#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import xml.etree.ElementTree as ET

from markdown.treeprocessors import Treeprocessor
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

DEFUALT_MATHJAX_SETTING = r"""
window.MathJax = {}
"""


class MathJaxInlinePattern(InlineProcessor):
    """
    """

    def __init__(self, pattern, extension):
        super().__init__(pattern)
        self.extension = extension

    def handleMatch(self, m, data):
        text = '\\(' + m.group('math') + '\\)'
        self.extension.mathjax_needed = True
        return text, m.start(0), m.end(0)


class MathJaxDisplayPattern(InlineProcessor):
    """
    """

    def __init__(self, pattern, extension):
        super().__init__(pattern)
        self.extension = extension

    def handleMatch(self, m, data):
        text = '$$' + m.group('math') + '$$'
        self.extension.mathjax_needed = True
        return text, m.start(0), m.end(0)



class MathJaxAddJavaScript(Treeprocessor):
    """
    the first version used the Postprocessor class
    but currently the toc extension called it, so here use the
    Treeprocessor do the add job

    Add Mathjax JavaScript
    """

    def __init__(self, extension):
        super().__init__(md=extension.md)
        self.extension = extension

    def run(self, root):
        """
        """
        # If no mathjax was present, then exit
        if not self.extension.mathjax_needed:
            return root

        mathjax_script_settings = ET.Element("script")
        mathjax_script_settings.text = self.extension.getConfig(
            "mathjax_settings")
        root.append(mathjax_script_settings)

        mathjax_script = ET.Element("script")
        mathjax_script.attrib['src'] = self.extension.getConfig("mathjax_src")
        mathjax_script.attrib['id'] = self.extension.getConfig("mathjax_id")
        root.append(mathjax_script)

        # Reset the boolean switch to false
        self.extension.mathjax_needed = False

        return root


class Md4MathjaxExtension(Extension):
    """
    A markdown extension enabling mathjax processing in Markdown
    """

    def __init__(self, **kwargs):
        self.config = {
            "mathjax_src": [
                'https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js',
                "the mathjax srcipt src value"],
            "mathjax_id": ['MathJax-script',
                           'the mathjax script id value'],
            "mathjax_settings": [DEFUALT_MATHJAX_SETTING,
                                 'mathjax settings']
        }
        # mainly set config
        super().__init__(**kwargs)

        # Used as a flag to determine if javascript needs to be injected
        self.mathjax_needed = False

    def reset(self):
        self.mathjax_needed = False

    def extendMarkdown(self, md):
        # later we will use it
        self.md = md

        # Regex to detect mathjax
        mathjax_inline_regex2 = r'\\\((?P<math>.*?)\\\)'

        mathjax_display_regex1 = r'(?<!\$)\$\$(?!\$)' \
                                 r'(?P<math>.+?)' \
                                 r'(?<!\$)\$\$(?!\$)'

        mathjax_display_regex2 = r'\\\[(?P<math>.+?)\\\]'

        # must higher than 180 for before the markdown EscapeInlineProcessor
        md.inlinePatterns.register(
            MathJaxInlinePattern(mathjax_inline_regex2, self),
            'mathjax_inlined2', 183)

        md.inlinePatterns.register(
            MathJaxDisplayPattern(mathjax_display_regex1, self),
            'mathjax_displayed1', 182)

        md.inlinePatterns.register(
            MathJaxDisplayPattern(mathjax_display_regex2, self),
            'mathjax_displayed', 181)

        # InlineProcessor priority is 20, so this one is need lower than 20
        md.treeprocessors.register(MathJaxAddJavaScript(self),
                                   'mathjax_addjavascript', 15)


def makeExtension(**kwargs):
    return Md4MathjaxExtension(**kwargs)
