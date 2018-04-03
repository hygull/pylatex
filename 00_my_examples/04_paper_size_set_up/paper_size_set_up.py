"""
	{
		"createdOn": "27 Feb 2018",
		"aim": "Setting paper size using PyLaTex, Usage of Paragraph etc.",
		"createdBy": "Rishikesh Agrawani",
		"link_for_arised_issue_on_github": "https://github.com/JelteF/PyLaTeX/issues/209",
	}
"""
from pylatex import Document, LargeText
from pylatex.section import Paragraph;
from pylatex.utils import bold

geometry_options = {
	"head": "0.5pt",
	"margin": "0.5in",
	"bottom": "0.5in",
	"includeheadfoot": True
}

# documnet_options = ["a4paper"] can also be used to set the paper size
doc = Document("paragraph", indent=True, geometry_options=geometry_options, document_options="a4paper");

text1 = """At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id.""";

text2 = """quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis olor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessit atibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.""";

text3 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duisaute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla ariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum""";

with doc.create(Paragraph("")):
	doc.append(LargeText( bold("Dear Malinikesh,")));

with doc.create(Paragraph("Paragraph1")):
	doc.append(text1);

with doc.create(Paragraph("Paragraph2")):
	doc.append(text2);

with doc.create(Paragraph("")):
	doc.append(text3);

doc.generate_pdf(clean_tex=False)