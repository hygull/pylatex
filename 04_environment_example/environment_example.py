from pylatex.base_classes import Environment
from pylatex.package import Package
from pylatex import Document, Section
from pylatex.utils import NoEscape


class AllTT(Environment):
    """A class to wrap LaTeX's alltt environment."""

    packages = [Package('alltt')]
    escape = False
    content_separator = "\n"

# Create a new document
doc = Document()
with doc.create(Section('Wrapping Latex Environments')):
    doc.append(NoEscape(
        r"""
        The following is a demonstration of a custom \LaTeX{}
        command with a couple of parameters.
        """))

    # Put some data inside the AllTT environment
    with doc.create(AllTT()):
        verbatim = ("This is verbatim, alltt, text.\n\n\n"
                    "Setting \\underline{escape} to \\underline{False} "
                    "ensures that text in the environment is not\n"
                    "subject to escaping...\n\n\n"
                    "Setting \\underline{content_separator} "
                    "ensures that line endings are broken in\n"
                    "the latex just as they are in the input text.\n"
                    "alltt supports math: \\(x^2=10\\)")
        doc.append(verbatim)

    doc.append("This is back to normal text...")

# Generate pdf
doc.generate_pdf('environment_ex', clean_tex=False)


"""
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/04_environment_example (master)
$ ls
environment_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/04_environment_example (master)
$ python environment_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/04_environment_example (master)
$ ls
environment_ex.pdf  environment_ex.tex  environment_example.py


"""