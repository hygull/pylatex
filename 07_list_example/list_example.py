# Test for list structures in PyLaTeX.
# More info @ http://en.wikibooks.org/wiki/LaTeX/List_Structures
from pylatex import Document, Section, Itemize, Enumerate, Description, \
    Command, NoEscape

if __name__ == '__main__':
    doc = Document()

    # create a bulleted "itemize" list like the below:
    # \begin{itemize}
    #   \item The first item
    #   \item The second item
    #   \item The third etc \ldots
    # \end{itemize}

    with doc.create(Section('"Itemize" list')):
        with doc.create(Itemize()) as itemize:
            itemize.add_item("the first item")
            itemize.add_item("the second item")
            itemize.add_item("the third etc")
            # you can append to existing items
            itemize.append(Command("ldots"))

    # create a numbered "enumerate" list like the below:
    # \begin{enumerate}[label=\alph*),start=20]
    #   \item The first item
    #   \item The second item
    #   \item The third etc \ldots
    # \end{enumerate}

    with doc.create(Section('"Enumerate" list')):
        with doc.create(Enumerate(enumeration_symbol=r"\alph*)",
                                  options={'start': 20})) as enum:
            enum.add_item("the first item")
            enum.add_item("the second item")
            enum.add_item(NoEscape("the third etc \\ldots"))

    # create a labelled "description" list like the below:
    # \begin{description}
    #   \item[First] The first item
    #   \item[Second] The second item
    #   \item[Third] The third etc \ldots
    # \end{description}

    with doc.create(Section('"Description" list')):
        with doc.create(Description()) as desc:
            desc.add_item("First", "The first item")
            desc.add_item("Second", "The second item")
            desc.add_item("Third", NoEscape("The third etc \\ldots"))

    doc.generate_pdf('lists', clean_tex=False)

"""
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/07_list_example (master)
$ python list_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/07_list_example (master)
$ ls
list_example.py  lists.pdf  lists.tex

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/07_list_example (master)
$
"""