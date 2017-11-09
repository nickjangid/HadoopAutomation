#!/usr/bin/python2
import cgi
print "content-type: text/html" 
#print

#print cgi.FormContent()
userName=cgi.FormContent()['x'][0]
password=cgi.FormContent()['p'][0]
#print "userName"
#print " password"

auser="dd"
apass="dd"

if userName == auser and password == apass:

	print "location: ../setup_list.html"
	print 

else:
	print "location: ../loginpage.html"
        print 





