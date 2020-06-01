from sphinx.directives.code import CodeBlock


class PylitCodeBlock(CodeBlock):

    def run(self):
        caption = self.options.get('caption')
        newcaption = '<<' + caption + '>>=='
        self.options['caption'] = newcaption

        return super(PylitCodeBlock, self).run()
