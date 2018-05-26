from setuptools import setup, find_packages

setup (
    name='GraphvizLexer',
    packages=find_packages(),
    entry_points =
    """
    [pygments.lexers]
    GraphvizLexer = graphviz.lexer:GraphvizLexer
    """,
)
