from sphinx.directives.code import CodeBlock


class PylitFile(CodeBlock):

    def run(self):
        caption = self.options.get('caption')
        if not caption:
            caption = ""
        newcaption = '<<' + caption + '>>=='
        self.options['caption'] = newcaption

        # format the block and return
        return super(PylitFile, self).run()
