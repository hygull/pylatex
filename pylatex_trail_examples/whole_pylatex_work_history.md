# Start - Latex compiler not found

```bash
Directory of E:\RishikeshAgrawani\projects\Python3\PyLaTeX\pylatex

12-03-2018  10:47    <DIR>          .
12-03-2018  10:47    <DIR>          ..
12-03-2018  10:47             1,368 01_basic.py
               1 File(s)          1,368 bytes
               2 Dir(s)  230,405,738,496 bytes free

(pylatex) E:\RishikeshAgrawani\projects\Python3\PyLaTeX\pylatex>python 01_basic.py
Traceback (most recent call last):
  File "01_basic.py", line 24, in <module>
    doc.generate_pdf(clean_tex=False)
  File "C:\Anaconda5.1Python2.7\lib\site-packages\pylatex\document.py", line 317, in generate_pdf
    u'or make sure you have latexmk or pdfLaTex installed.'
pylatex.errors.CompilerError: No LaTex compiler was found
Either specify a LaTex compiler or make sure you have latexmk or pdfLaTex installed.
```

## When you will try to run the online available examples

## 1

```
basic.py => latexmk.pl, lastpage.lty
```

## 2

```
basic_inheritance.py => NA
```

## 3

```
complex_report.py => tabu.sty, ragged2e.sty, xcolor.sty, colortbl.sty, fancyhdr.sty, supp-pdf.mkii
```

You may need to download images & change the name of logos etc. on `complex_report.py` to fix issues like below.

```
Latexmk: Missing input file: 'chequeexample.png' from line
  'LaTeX Warning: File `chequeexample.png' not found on input line 177.'

Latexmk: Missing input file: 'sample-logo.png' from line
  'LaTeX Warning: File `sample-logo.png' not found on input line 177.'
```

### 4

