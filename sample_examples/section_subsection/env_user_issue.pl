#!usr/bin/perl

use strict;
use warnings;

my $logname = $ENV{ LOGNAME };
print "\$logname = $logname\n";

my $user = $ENV{ USER };
print "\$user = $user\n";

my $pwuid = getpwuid( $< );
print "\$pwuid = $pwuid\n";

# rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Python/pylatex/trial_examples/section_subsection (master)
# $ python section_subsection.py
# Use of uninitialized value $ENV{"USER"} in concatenation (.) or string at C:\Program Files\MikTeX2.9\scripts\latexmk\perl\latexmk.pl line 761.
# Latexmk: -interaction=nonstopmode bad option

# Latexmk: Bad options specified
# Use
#    latexmk -help
# to get usage information

# Traceback (most recent call last):
#   File "section_subsection.py", line 24, in <module>
#     doc.generate_pdf(clean_tex=False)
#   File "C:\AnacondaPython2.5.0.1\lib\site-packages\pylatex\document.py", line 269, in generate_pdf
#     stderr=subprocess.STDOUT)
#   File "C:\AnacondaPython2.5.0.1\lib\subprocess.py", line 219, in check_output
#     raise CalledProcessError(retcode, cmd, output=output)
# subprocess.CalledProcessError: Command '[u'latexmk', u'--pdf', u'--interaction=nonstopmode', u'basic.tex']' returned non-zero exit status 10
