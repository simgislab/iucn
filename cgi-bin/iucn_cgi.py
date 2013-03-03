#!/usr/bin/env python
import cgitb ; cgitb.enable()
import cgi

form = cgi.FieldStorage()

print "Content-Type: text/plain\n" 
# note the extra blank line terminate the headers
print form.getvalue("iucncode")
