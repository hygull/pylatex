"""
	{
		"createdOn": "21 Feb 2018",
		"aim": "To generate PDF having a bar chart image containg the marks details",
		"createdBy": "Rishikesh Agrawani"
		"referenceLinks": [
			"https://pythonspot.com/matplotlib-bar-chart/",
			"https://jeltef.github.io/PyLaTeX/latest/examples/matplotlib_ex.html"
		]
	}
"""
from pylatex import Document, Figure
from pylatex.utils import NoEscape
import matplotlib
matplotlib.use("Agg") # If you want to see the plot generated (just comment this line)
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import MySQLdb
import config 

def create_pdf_document(rows):
	subjects = ["Mathematics", "Physics", "Chemistry"]
	index = np.arange(3)
	colors = ["r", "g", "b", "c", "m", "y", "k"]

	# creating plot
	fig, ax = plt.subplots()
	bar_width = 0.30
	opacity = 0.8
	color_index = 0

	for row in rows:
		plt.bar(index, [row[2], row[3], row[4]], bar_width,
	                 alpha=opacity,
	                 color=colors[randint(0, len(colors) - 1)],
	                 # color=colors[color_index % len(colors)],
	                 label=(row[1].strip().split()[0]).strip())
		color_index += 1
		index = index + bar_width

	plt.xlabel('Students')
	plt.ylabel('Scores')
	plt.title('BAR CHART - Scores of Mathematics students')

	index = np.arange(3) # if this line will not be here (X labels will shift towards right)
	plt.xticks(index, subjects)
	plt.legend()
	 
	plt.tight_layout()
	plt.show()

	# creating pdf
	geometry_options = {"left": "1cm", "right": "1cm"}
	doc = Document("maths_students_scores", geometry_options=geometry_options)

	with doc.create(Figure(position="htbp")) as plot:
		plot.add_plot(width=NoEscape(r"0.8\textwidth"), dpi=300)
		plot.add_caption("Scores of Mathematics students")

	doc.generate_pdf(clean_tex=False)


# start
try:
	connection_config = [config.HOST, config.USER, config.PASSWORD, config.DATABASE]

	db = MySQLdb.connect(*connection_config)
	cursor = db.cursor()

	query = "SELECT * FROM `maths_students`;";

	cursor.execute(query)
	rows = cursor.fetchall()

	# row1 = None
	# shore = "+-" + "-"*30 + "-+"
	# for row in rows:
	# 	if not row1:
	# 		row1 = row
	# 	print shore
	# 	print "| %-30s |" % row[1]

	# print shore

	# print str(len(row1)) + " columns"
except Exception as err:
	print "Error:- ", err
else:
	print "Successfully fetched students from MySQL DATABASE"
	print "Creating PDF"
	create_pdf_document(rows)
	print "Pdf creation done"
finally:
	db.close()
# end