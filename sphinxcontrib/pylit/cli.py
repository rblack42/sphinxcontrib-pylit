import click


def about_me(your_name):
    return "The wise {} loves Python.".format(your_name)


class ExampleClass:
    """An example docstring for a class definition."""

    def __init__(self, name):
        self.name = name

    def about_self(self):
        return "I am a very smart {} object.".format(self.name)


@click.command()
@click.argument('name')
def cli(name):
    cls = ExampleClass(name)
    print(cls.about_self())
