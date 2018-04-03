# pylatex

## Installation

```
pip install pylatex
```


## Before installation of MikTeX

```
(pylatex) G:\RishikeshAgrawani\ProjectsWin7\Python3\PyLaTeX\pylatex\01_basic>python 01
Traceback (most recent call last):
  File "01_basic.py", line 24, in <module>
    doc.generate_pdf(clean_tex=False)
  File "C:\Anaconda2.5.0.1\lib\site-packages\pylatex\document.py", line 317, in genera
    u'or make sure you have latexmk or pdfLaTex installed.'
pylatex.errors.CompilerError: No LaTex compiler was found
Either specify a LaTex compiler or make sure you have latexmk or pdfLaTex installed.
```

## After installation of MikTeX2.9.6615

You can see below it is looking for "perl.exe"

```
(C:\Anaconda2.5.0.1) G:\RishikeshAgrawani\ProjectsWin7\Python3\PyLaTeX\pylatex\01_basic>python 01_basic.py
latexmk: The script engine could not be found.
latexmk: Data: scriptEngine="perl.exe"

Traceback (most recent call last):
  File "01_basic.py", line 24, in <module>
    doc.generate_pdf(clean_tex=False)
  File "C:\Anaconda2.5.0.1\lib\site-packages\pylatex\document.py", line 269, in generate_pdf
    stderr=subprocess.STDOUT)
  File "C:\Anaconda2.5.0.1\lib\subprocess.py", line 219, in check_output
    raise CalledProcessError(retcode, cmd, output=output)
subprocess.CalledProcessError: Command '[u'latexmk', u'--pdf', u'--interaction=nonstopmode', u'basic.tex']' returned non-zero exit
 status 1
 ```

## After installation of STAWBERRY PERL 5.26.1.1 (Works fine)

```
(C:\Anaconda2.5.0.1) G:\RishikeshAgrawani\ProjectsWin7\Python3\PyLaTeX\pylatex\01_basic>python 01_basic.py
```

