from pylatex import Document, Section, Figure, SubFigure, NoEscape
import os

if __name__ == '__main__':
    doc = Document(default_filepath='subfigures')
    image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')

    with doc.create(Section('Showing subfigures')):
        with doc.create(Figure(position='h!')) as kittens:
            with doc.create(SubFigure(
                    position='b',
                    width=NoEscape(r'0.45\linewidth'))) as left_kitten:

                left_kitten.add_image(image_filename,
                                      width=NoEscape(r'\linewidth'))
                left_kitten.add_caption('Kitten on the left')
            with doc.create(SubFigure(
                    position='b',
                    width=NoEscape(r'0.45\linewidth'))) as right_kitten:

                right_kitten.add_image(image_filename,
                                       width=NoEscape(r'\linewidth'))
                right_kitten.add_caption('Kitten on the right')
            kittens.add_caption("Two kittens")

    doc.generate_pdf(clean_tex=False)

"""
I was not having kitten.jpg in the current folder
So got the error
I downloaded kitten.jpg and ran again, it worked
"""

"""
Latexmk: References changed.
Latexmk: Log file says output to 'subfigures.pdf'
Collected error summary (may duplicate other messages):
  pdflatex: Command for 'pdflatex' gave return code 1
      Refer to 'subfigures.log' for details
Latexmk: Use the -f option to force complete processing,
 unless error was exceeding maximum runs of latex/pdflatex.
=== TeX engine is 'pdfTeX'
Latexmk: Errors, so I did not complete making targets

Traceback (most recent call last):
  File "subfigure_example.py", line 26, in <module>
    doc.generate_pdf(clean_tex=False)
  File "C:\AnacondaPython2.5.0.1\lib\site-packages\pylatex\document.py", line 264, in generate_pdf
    stderr=subprocess.STDOUT)
  File "C:\AnacondaPython2.5.0.1\lib\subprocess.py", line 219, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '[u'latexmk', u'--pdf', u'--interaction=nonstopmode', u'subfigures.tex']' returned non-zero exit status 12

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/15_subfigure_example (master)
$ python subfigure_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/15_subfigure_example (master)
$ ls
kitten.jpg  subfigure_example.py  subfigures.pdf  subfigures.tex

"""