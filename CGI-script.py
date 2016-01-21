#!/usr/bin/env python
import os, json, cgi
print "Content-type: text/html"
print
print "<HTML><BODY><h1>Hello, this is dog</h1>"
print "<FORM method = 'POST'><INPUT name = 'x'></FORM>"
form = cgi.FieldStorage()
print "<P>X was: " + cgi.escape(str(form.getvalue('x')))
print "</BODY></HTML>"
