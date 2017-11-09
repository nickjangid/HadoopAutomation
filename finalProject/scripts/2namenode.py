#!/usr/bin/python2


import cgi
print "content-type: text/html" 

#print
#print cgi.FormContent()

namenode=cgi.FormContent()['n1'][0]


if  namenode == 'namenode':
	print "location: ../nn.html"
	print 

elif namenode == 'datanode':
	print "location: ../dn.html"
        print 
elif namenode == 'job':
	print "location: ../nm.html"
        print 
elif namenode == 'task':
	print "location: ../tm.html"
        print 
else:
	print "location: ../2cluster.html"
        print 


