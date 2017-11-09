#!/usr/bin/python2


import cgi

print "content-type: text/html"
print

count=cgi.FormContent()['c'][0]


i=0

print "<form action=final.py>"
while i<=int(count):
	print "Enter your Ip{0} <input type='text' name='n{0}' />".format(i)
	print "<br />"	
	i=i+1


print "<input type='submit' />"

print "</form>"
