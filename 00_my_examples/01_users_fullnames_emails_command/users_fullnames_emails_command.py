"""
	{
		"createdOn": "19 Feb 2018",
		"aim": "To generate PDF having list of fullnames of all users of DB table",
		"createdBy": "Rishikesh Agrawani"
	}
"""
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import NoEscape
import MySQLdb
import config 

def create_pdf_document(fullnames, emails):
	doc = Document()

	doc.preamble.append(Command("title", "My employees"));
	doc.preamble.append(Command("author", "Rishikesh Agrawani"))
	doc.preamble.append(Command("date", NoEscape( r'\today')))
	doc.append(NoEscape(r"\maketitle")) # Very important line, if not added(details won't be added)

	with doc.create(Section("Users")):
		for subsection_title, data_list in zip(["Full names", "Emails"], [fullnames, emails]):
			with doc.create(Subsection(subsection_title)):
				for data in data_list:
					doc.append(data + "\n")

	doc.generate_pdf("users-details-maketile-activated", clean_tex=False)

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