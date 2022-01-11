#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import xml.etree.ElementTree as etree
from markdown.postprocessors import Postprocessor
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
from jinja2 import Template


class MathJaxInlinePattern(InlineProcessor):
    """
    """

    def __init__(self, pattern, tag, extension):
        super().__init__(pattern)
        self.extension = extension
        self.tag = tag

    def handleMatch(self, m, data):
        el = etree.Element(self.tag)
        el.set('class', self.extension.getConfig('tag_class'))

        if self.tag == 'div':
            el.text = '$$' + m.group('math') + '$$'
        else:
            el.text = '$' + m.group('math') + '$'

        self.extension.mathjax_needed = True

        return el, m.start(0), m.end(0)


class MathJaxAddJavaScript(Postprocessor):
    """
    Add Mathjax JavaScript
    """

    def __init__(self, extension):
        super().__init__(md=extension.md)
        self.extension = extension

    def run(self, text):
        # If no mathjax was present, then exit
        if not self.extension.mathjax_needed:
            return text

        # Reset the boolean switch to false
        self.extension.mathjax_needed = False

        return text + '\n' + self.process_mathjax_script()

    def process_mathjax_script(self):
        """
        Load the mathjax script template from file, and render with the settings
        """
        jinja_env = {
            "SRC": self.extension.getConfig('mathjax_src')
        }

        # Read the mathjax javascript template from file
        template_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'mathjax_javascript_template')
        with open(template_file, 'r') as mathjax_script_template:
            mathjax_template = mathjax_script_template.read()

        template = Template(mathjax_template)

        return template.render(**jinja_env)


class Md4MathjaxExtension(Extension):
    """
    A markdown extension enabling mathjax processing in Markdown
    """

    def __init__(self, **kwargs):
        self.config = {
            "auto_insert": [True,
                            'You may insert yourself in another way?'],
            "tag_class": ["math",
                          "The class of the tag in which math is wrapped"],
            "mathjax_src": [
                'https://cdn.jsdelivr.net/npm/mathjax@3.2.0/es5/tex-mml-chtml.js',
                "the mathjax src value"]
        }
        # mainly set config
        super().__init__(**kwargs)

        # Used as a flag to determine if javascript needs to be injected
        self.mathjax_needed = False

    def extendMarkdown(self, md):
        # later we will use it
        self.md = md

        # Regex to detect mathjax
        mathjax_inline_regex1 = r'(?<!\$)\$(?!\$)' \
                                r'(?P<math>.+?)' \
                                r'(?<!\$)\$(?!\$)'
        mathjax_inline_regex2 = r'\\\((?P<math>.*?)\\\)'

        mathjax_display_regex1 = r'(?<!\$)\$\$(?!\$)' \
                                 r'(?P<math>.+?)' \
                                 r'(?<!\$)\$\$(?!\$)'

        mathjax_display_regex2 = r'\\\[(?P<math>.+?)\\\]'

        md.inlinePatterns.register(
            MathJaxInlinePattern(mathjax_inline_regex1, 'span', self),
            'mathjax_inlined1', 184)

        # must higher than 180 for before the markdown EscapeInlineProcessor
        # and must lower than mathjax_inlined1
        md.inlinePatterns.register(
            MathJaxInlinePattern(mathjax_inline_regex2, 'span', self),
            'mathjax_inlined2', 183)

        md.inlinePatterns.register(
            MathJaxInlinePattern(mathjax_display_regex1, 'div', self),
            'mathjax_displayed1', 182)

        # must higher than 180 for before the markdown EscapeInlineProcessor
        # and must lower than mathjax_inlined1
        md.inlinePatterns.register(
            MathJaxInlinePattern(mathjax_display_regex2, 'div', self),
            'mathjax_displayed', 181)

        md.postprocessors.register(MathJaxAddJavaScript(self),
                                   'mathjax_addjavascript', 0)


def makeExtension(**kwargs):
    return Md4MathjaxExtension(**kwargs)
