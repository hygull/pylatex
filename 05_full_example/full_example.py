import numpy as np

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os

if __name__ == '__main__':
    image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')

    geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometry_options)

    with doc.create(Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        with doc.create(Subsection('Math that is incorrect')):
            doc.append(Math(data=['2*3', '=', 9]))

        with doc.create(Subsection('Table of something')):
            with doc.create(Tabular('rc|cl')) as table:
                table.add_hline()
                table.add_row((1, 2, 3, 4))
                table.add_hline(1, 2)
                table.add_empty_row()
                table.add_row((4, 5, 6, 7))

    a = np.array([[100, 10, 20]]).T
    M = np.matrix([[2, 3, 4],
                   [0, 0, 1],
                   [0, 0, 2]])

    with doc.create(Section('The fancy stuff')):
        with doc.create(Subsection('Correct matrix equations')):
            doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

        with doc.create(Subsection('Alignat math environment')):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                agn.append(r'\frac{a}{b} &= 0 \\')
                agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

        with doc.create(Subsection('Beautiful graphs')):
            with doc.create(TikZ()):
                plot_options = 'height=4cm, width=6cm, grid=major'
                with doc.create(Axis(options=plot_options)) as plot:
                    plot.append(Plot(name='model', func='-x^5 - 242'))

                    coordinates = [
                        (-4.77778, 2027.60977),
                        (-3.55556, 347.84069),
                        (-2.33333, 22.58953),
                        (-1.11111, -493.50066),
                        (0.11111, 46.66082),
                        (1.33333, -205.56286),
                        (2.55556, -341.40638),
                        (3.77778, -1169.24780),
                        (5.00000, -3269.56775),
                    ]

                    plot.append(Plot(name='estimate', coordinates=coordinates))

        with doc.create(Subsection('Cute kitten pictures')):
            with doc.create(Figure(position='h!')) as kitten_pic:
                kitten_pic.add_image(image_filename, width='120px')
                kitten_pic.add_caption('Look it\'s on its back')

    doc.generate_pdf('full', clean_tex=False)


# I got error when I ran the above code. 
# To fix this I downloaded jpg image and saved it as kitten.jpg
# Finally it worked

"""
...
...
...
  'LaTeX Warning: File `kitten.jpg' not found on input line 110.'
Latexmk: Missing input file: 'kitten.jpg' from line
  'LaTeX Warning: File `kitten.jpg' not found on input line 110.'
Latexmk: References changed.
Latexmk: References changed.
Latexmk: Log file says output to 'full.pdf'
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'full.log' for details
Latexmk: Use the -f option to force complete processing,
 unless error was exceeding maximum runs of latex/pdflatex.
=== TeX engine is 'pdfTeX'
Latexmk: Errors, so I did not complete making targets

Traceback (most recent call last):
  File "full_example.py", line 68, in <module>
    doc.generate_pdf('full', clean_tex=False)
  File "C:\AnacondaPython2.5.0.1\lib\site-packages\pylatex\document.py", line 264, in generate_pdf
    stderr=subprocess.STDOUT)
  File "C:\AnacondaPython2.5.0.1\lib\subprocess.py", line 219, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '[u'latexmk', u'--pdf', u'--interaction=nonstopmode', u'full.tex']' returned non-zero exit status 12

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/05_full_example (master)
$ python full_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/05_full_example (master)
$ ls
full.pdf  full.tex  full_example.py  kitten.jpg


"""