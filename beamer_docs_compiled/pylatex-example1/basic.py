from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')


if __name__ == '__main__':
    # Basic document
    doc = Document('basic', documentclass="beamer", data=["Rishikesh", "Agrawani"])
    fill_document(doc)

    doc.generate_pdf(clean_tex=False)
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()

    doc.preamble.append(Command('title', 'Awesome Title'))
    doc.preamble.append(Command('author', 'Anonymous author'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False)

    # Add stuff to the document
    with doc.create(Section('A second section')):
        doc.append('Some text.')

    doc.generate_pdf('basic_maketitle2', clean_tex=False)
    tex = doc.dumps()  # The document as string in LaTeX syntax