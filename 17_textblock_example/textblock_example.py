from pylatex import Document, MiniPage, TextBlock, MediumText, HugeText, \
    SmallText, VerticalSpace, HorizontalSpace
from pylatex.utils import bold

geometry_options = {"margin": "0.5in"}
doc = Document(indent=False, geometry_options=geometry_options)
doc.change_length("\TPHorizModule", "1mm")
doc.change_length("\TPVertModule", "1mm")

with doc.create(MiniPage(width=r"\textwidth")) as page:
    with page.create(TextBlock(100, 0, 0)):
        page.append("**** Ten Thousand Dollars")

    with page.create(TextBlock(100, 0, 30)):
        page.append("COMPANY NAME")
        page.append("\nSTREET, ADDRESS")
        page.append("\nCITY, POSTAL CODE")

    with page.create(TextBlock(100, 150, 40)):
        page.append(HugeText(bold("VOID")))

    with page.create(TextBlock(80, 150, 0)):
        page.append("DATE")
        page.append(MediumText(bold("2016 06 07\n")))
        page.append(HorizontalSpace("10mm"))
        page.append(SmallText("Y/A M/M D/J"))

    with page.create(TextBlock(70, 150, 30)):
        page.append(MediumText(bold("$***** 10,000.00")))

    page.append(VerticalSpace("100mm"))

doc.generate_pdf("textblock", clean_tex=False)


"""
Asked for 1 installation when I ran the code
"""

"""
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex (master)
$ cd 17_textblock_example/

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/17_textblock_example (master)
$ python textblock_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/17_textblock_example (master)
$ ls
textblock.pdf  textblock.tex  textblock_example.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/PyLaTex/17_textblock_example (master)
$

"""