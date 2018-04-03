"""
	{
		"createdOn": "19 Feb 2018",
		"aim": "To generate PDF having list of users of DB table(tabular form presentation)",
		"createdBy": "Rishikesh Agrawani"
	}
"""
from pylatex import Document, LongTabu
from pylatex.utils import NoEscape, bold
import MySQLdb
import config 

def create_pdf_document(rows):
	geometry_options = {
		"head": "30pt",
		"bottom": "0.5in",
		"margin": "0.6in",
		"includeheadfoot": True
	}
	doc = Document(geometry_options=geometry_options)

	with doc.create(LongTabu("X[l] X[2l] X[r] X[r]", row_height=1.5)) as my_table:
		my_table.add_row(["Full name", "Email", "Contact", "Address"], \
						 mapper=bold, color="pink"
						)
		my_table.add_empty_row()
		my_table.add_hline();

		for index, row in enumerate(rows):
			data_list = [row[1], row[2], row[3], row[4]]

			if (index % 2 == 0):
				my_table.add_row(data_list, color="gray");
			else:
				my_table.add_row(data_list, color="lightgray");

	doc.generate_pdf("users-details", clean_tex=False)

# start
try:
	connection_config = [config.HOST, config.USER, config.PASSWORD, config.DATABASE]

	db = MySQLdb.connect(*connection_config)
	cursor = db.cursor()

	query = "SELECT * FROM `users`";

	cursor.execute(query)
	rows = cursor.fetchall()

	row1 = None
	shore = "+-" + "-"*30 + "-+"
	for row in rows:
		if not row1:
			row1 = row
		print shore
		print "| %-30s |" % row[2]

	print shore

	print str(len(row1)) + " columns"
except Exception as err:
	print "Error:- ", err
else:
	print "Successfully fetched users from MySQL DATABASE"
	print "Creating PDF"
	create_pdf_document(rows)
	print "Pdf creation done"
finally:
	db.close()
# end