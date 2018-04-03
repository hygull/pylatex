# PyLaTex

### System configurations for this

* Windows 10 pro, 64-
bit
* Python 2.7.14 :: Anaconda, Inc.

### INTERNET Connectivity

While running some of these examples you may be asked for the installations. So make sure you have proper INTERNET connectivity.

You can see the Screenshots inside **images** folder, how it the code is asking for `sty` files, [click here](./images/) to go.

### Download guide

You can click on this [link](https://repo.continuum.io/archive/Anaconda2-5.1.0-Windows-x86_64.exe) to direct download the `Python 2.7.14 :: Anaconda, Inc.`, do not forget to check while installation if it asks for updating/adding environment variable `PATH`.

See beautiful documentation at [https://jeltef.github.io/PyLaTeX/latest/](https://jeltef.github.io/PyLaTeX/latest/).

### Let me start now 

In Windows, I tried to run basic example given in the documentation. I got errors regarding file path.

The error was something like the below one.

```bash
D:\projects\Python\PyLaTex>python basic_example.py
Traceback (most recent call last):
  File "basic_example.py", line 31, in <module>
    doc.generate_pdf(clean_tex=False)
  File "C:\AnacondaPython2.5.0.1\lib\site-packages\pylatex\document.py", line 310, in generate_pdf
    raise(os_error)
WindowsError: [Error 2] The system cannot find the file specified
```

I searched the solution and got it in stackoverflow at [https://stackoverflow.com/questions/40039763/pylatex-error-when-generate-pdf-file-no-such-file-or-directory](https://stackoverflow.com/questions/40039763/pylatex-error-when-generate-pdf-file-no-such-file-or-directory).


Based on the above link I found that I have to install latexmk to overcome the issue.

Then I searched `latexmk on windows install python` and clicked on 1st link [http://mg.readthedocs.io/latexmk.html](http://mg.readthedocs.io/latexmk.html)

In this documentation I saw that I will need to install 2 more things `strawberry perl` and `miktex` on windows.

I downloaded and installed `basic-miktex-2.9.6615-x64.exe` from [http://strawberryperl.com/](http://strawberryperl.com/), this is [direct download link](http://strawberryperl.com/download/5.24.3.1/strawberry-perl-5.24.3.1-64bit.msi).

Then I downloaded and installed the 2nd and final requirement from [https://miktex.org/download](https://miktex.org/download), this is [direct download link](https://miktex.org/download/ctan/systems/win32/miktex/setup/windows-x64/basic-miktex-2.9.6615-x64.exe).

Now I fired the `GIT BASH` (you can use `cmd`) and ran `basic_example.py`.

### basic_example.py

```python
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
    doc = Document('basic')
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
```

### On Terminal

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/01_basic_example (master)
$ ls
basic_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/01_basic_example (master)
$ python basic_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/01_basic_example (master)
$ ls
basic.pdf  basic_example.py     basic_maketitle.tex   basic_maketitle2.tex
basic.tex  basic_maketitle.pdf  basic_maketitle2.pdf

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/01_basic_example (master)
$
``` 

I succeeded. 

Great!!!

Let us look at the below example copied from [https://jeltef.github.io/PyLaTeX/latest/examples/complex_report.html](https://jeltef.github.io/PyLaTeX/latest/examples/complex_report.html)

I have downloaded `programmer.jpg` and `sample-logo.jpg` and placed in the same folder where the python code is.

```python
import os

from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape


def generate_unique():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options)

    # Generating first page style
    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                         pos='c')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__),
                                     'sample-logo.jpg')
            logo_wrapper.append(StandAloneGraphic(image_options="width=120px",
                                filename=logo_file))

    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                 pos='c', align='r')) as title_wrapper:
            title_wrapper.append(LargeText(bold("Bank Account Statement")))
            title_wrapper.append(LineBreak())
            title_wrapper.append(MediumText(bold("Date")))

    # Add footer
    with first_page.create(Foot("C")) as footer:
        message = "Important message please read"
        with footer.create(Tabularx(
                "X X X X",
                width_argument=NoEscape(r"\textwidth"))) as footer_table:

            footer_table.add_row(
                [MultiColumn(4, align='l', data=TextColor("blue", message))])
            footer_table.add_hline(color="blue")
            footer_table.add_empty_row()

            branch_address = MiniPage(
                width=NoEscape(r"0.25\textwidth"),
                pos='t')
            branch_address.append("960 - 22nd street east")
            branch_address.append("\n")
            branch_address.append("Saskatoon, SK")

            document_details = MiniPage(width=NoEscape(r"0.25\textwidth"),
                                        pos='t', align='r')
            document_details.append("1000")
            document_details.append(LineBreak())
            document_details.append(simple_page_number())

            footer_table.add_row([branch_address, branch_address,
                                  branch_address, document_details])

    doc.preamble.append(first_page)
    # End first page style

    # Add customer information
    with doc.create(Tabu("X[l] X[r]")) as first_page_table:
        customer = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='h')
        customer.append("Verna Volcano")
        customer.append("\n")
        customer.append("For some Person")
        customer.append("\n")
        customer.append("Address1")
        customer.append("\n")
        customer.append("Address2")
        customer.append("\n")
        customer.append("Address3")

        # Add branch information
        branch = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!',
                          align='r')
        branch.append("Branch no.")
        branch.append(LineBreak())
        branch.append(bold("1181..."))
        branch.append(LineBreak())
        branch.append(bold("TIB Cheque"))

        first_page_table.add_row([customer, branch])
        first_page_table.add_empty_row()

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")

    # Add statement table
    with doc.create(LongTabu("X[l] X[2l] X[r] X[r] X[r]",
                             row_height=1.5)) as data_table:
        data_table.add_row(["date",
                            "description",
                            "debits($)",
                            "credits($)",
                            "balance($)"],
                           mapper=bold,
                           color="lightgray")
        data_table.add_empty_row()
        data_table.add_hline()
        row = ["2016-JUN-01", "Test", "$100", "$1000", "-$900"]
        for i in range(30):
            if (i % 2) == 0:
                data_table.add_row(row, color="lightgray")
            else:
                data_table.add_row(row)

    doc.append(NewPage())

    # Add cheque images
    with doc.create(LongTabu("X[c] X[c]")) as cheque_table:
        cheque_file = os.path.join(os.path.dirname(__file__),
                                   'programmer.jpg')
        cheque = StandAloneGraphic(cheque_file, image_options="width=200px")
        for i in range(0, 20):
            cheque_table.add_row([cheque, cheque])

    doc.generate_pdf("complex_report", clean_tex=False)

generate_unique()
```

I have given my own image file names in the copied code(You only need to change in 2 places), I got this by just at the error logs.

Finally I succeeded as the following shows.

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/02_complex_example (master)
$ python complex_report.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/02_complex_example (master)
$ ls
complex_report.pdf  complex_report.py  complex_report.tex  programmer.jpg  sample-logo.jpg
```

### Example1 - generating PDF report containing all users present in DB table

You can check my **Python MySQL database connectivity** repository  at [https://github.com/hygull/python-mysql](https://github.com/hygull/python-mysql).

As I have configured my MySQL database according to that for this project.

`config.py`

```python
HOST = "127.0.0.1"

PORT = "3306"

USER = "rishikesh"

PASSWORD = "rishikesh@321"

DATABASE = "nodejs"

```

`00_users_fullnames_emails.py`

```python
"""
    {
        "createdOn": "19 Feb 2018",
        "aim": "To generate PDF having list of fullnames of all users of DB table",
        "createdBy": "Rishikesh Agrawani"
    }
"""
from pylatex import Document, Section, Subsection

import MySQLdb
import config

def create_pdf_document(fullnames, emails):
    doc = Document("users-details")

    with doc.create(Section("Users")):
        for subsection_title, data_list in zip(["Full names", "Emails"], [fullnames, emails]):
            with doc.create(Subsection(subsection_title)):
                for data in data_list:
                    doc.append(data + "\n")

    doc.generate_pdf(clean_tex=False)

try:
    connection_config = [config.HOST, config.USER, config.PASSWORD, config.DATABASE]

    db = MySQLdb.connect(*connection_config)
    cursor = db.cursor()

    query = "SELECT * FROM `users`";

    cursor.execute(query)
    rows = cursor.fetchall()

    row1 = None
    shore = "+-" + "-"*30 + "-+"
    fullnames = []
    emails = list()
    for row in rows:
        if not row1:
            row1 = row
        print shore
        print "| %-30s |" % row[2]
        fullnames.append(row[1])
        emails.append(row[2])
    print shore

    print str(len(row1)) + " columns"
except Exception as err:
    print "Error:- ", err
else:
    print "Successfully fetched users from MySQL DATABASE"
    print "Creating PDF"
    create_pdf_document(fullnames, emails)
    print "Pdf creation done"
finally:
    db.close()

```

**Output on GIT bash**

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/00_my_examples/00_users_fullnames_emails (master)
$ python users_fullnames_emails.py
+--------------------------------+
| rob.pike@gmail.com             |
+--------------------------------+
| robert.griesemer@gmail.com     |
+--------------------------------+
| ken.thompson@gmail.com         |
+--------------------------------+
| tkinter.tk@gmail.com           |
+--------------------------------+
| mysql.db@gmail.com             |
+--------------------------------+
| hemkesh.agrawani@gmail.com     |
+--------------------------------+
8 columns
Successfully fetched users from MySQL DATABASE
Creating PDF
Pdf creation done

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/00_my_examples/00_users_fullnames_emails (master)
$
```

You can check this generated PDF by clicking [here](./00_my_examples/01_users_fullnames_emails/users-details.pdf).

### More

You can check the PDFs in this repo by clicking on [this](./02_complex_example/complex_report.pdf).

Enjoy more examples by visiting on this [link](https://jeltef.github.io/PyLaTeX/latest/examples.html#).


### References

[Matplotlib, figure, dpi(dot per inch) keyword argument](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html)

[Matplotlib tight_layout()'s usage best documentation](https://matplotlib.org/users/tight_layout_guide.html)

pdflatex command - [pdflatex MYPAPER.tex && bibtex MYPAPER.aux && pdflatex MYPAPER.tex && pdflatex MYPAPER.tex](
https://tex.stackexchange.com/questions/43325/citations-not-showing-up-in-text-and-bibiography)

latexmk command - [latexmk -pdf](http://mg.readthedocs.io/latexmk.html)

[GhostScript](https://www.ghostscript.com/download/gsdnld.html) - Ghostscript is an interpreter for the PostScript page description language used by laser printers

[GSView](http://pages.cs.wisc.edu/~ghost/gsview/get50.htm) - GSview is a graphical interface for Ghostscript under MS-Windows. I compiled my latex files without the installation of these two things. I need to check it as here the GSView is for manipulating PDF documents.

