# -*- coding: utf-8 -*-
from pylatex import Document, Section, Subsection, Command, Package
from pylatex.utils import italic, NoEscape

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('ِش سثؤفهخى')):
        doc.append('إخع ساخعمي شمصشغس سحثشن فاث فقعفا')
        doc.append(italic('فشمهؤ ؤخىفثىفس شقث شمسخ ىهؤث'))

        with doc.create(Subsection('آثص ٍعلاسثؤفهخى')):
            doc.append('بشةخعس ؤقشئغ ؤاشقشؤفثقس: $&#{}')


if __name__ == '__main__':
    # Basic document
    doc = Document('basic')
    # doc.packages.add(Package('grffile', options=['encoding', 'filenameencoding=utf8']))
    fill_document(doc)

    doc.generate_pdf(clean_tex=False, compiler="xelatex")
    doc.generate_tex()

    # Document with `\maketitle` command activated
    doc = Document()
    # doc.packages.add(Package('grffile', options=['encoding', 'filenameencoding=utf8']))

    doc.preamble.append(Command('title', 'لأخخي ةخقىهىل ٍهق'))
    doc.preamble.append(Command('author', 'ٌهساهنثسا ِلقشصشىه'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))

    fill_document(doc)

    doc.generate_pdf('basic_maketitle', clean_tex=False, compiler="xelatex")

    # Add stuff to the document
    with doc.create(Section('A second section')):
        doc.append('Some text.')

    doc.generate_pdf('basic_maketitle2', clean_tex=False, compiler="xelatex")
    tex = doc.dumps()  # The document as string in LaTeX syntax
