#!/usr/bin/python2


import cgi
print "content-type: text/html" 

#print
#print cgi.FormContent()

namenode=cgi.FormContent()['n1'][0]


if  namenode == 'namenode':
	print "location: ../namenode.html"
	print 

elif namenode == 'datanode':
	print "location: ../datanode.html"
        print 
elif namenode == 'nodemanager':
	print "location: ../job.html"
        print 
elif namenode == 'datamanager':
	print "location: ../task.html"
        print 
else:
	print "location: ../cluster.html"
        print 


