from sphinx.directives.code import CodeBlock
from .DataStore import DataStore


class PylitCodeBlock(CodeBlock):

    def run(self):
        caption = self.options.get('caption')
        if not caption:
            caption = ""
        newcaption = '<<' + caption + '>>=='
        self.options['caption'] = newcaption

        # store this block if needed
        ds = DataStore()
        docname = self.env.docname
        lineno = self.lineno
        content = '\n'.join(self.content)
        ds.add_code_block('code', caption, docname, lineno, content)

        # format the block and return
        return super(PylitCodeBlock, self).run()
