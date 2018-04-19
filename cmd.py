#!/usr/bin/python

import commands
import cgi,time

print "Content-Type: text/html"
print ""

data=cgi.FieldStorage()

command=data.getvalue('c')

if command == "date":
	print "hello"
	time.sleep(1)
        print "<pre>"
	print commands.getoutput('date')
	print "</pre>"

elif command == "cal":
        print "<pre>"
	print commands.getoutput('cal')
	print "</pre>"

elif command == "ftp":
	print "<pre>"
	print commands.getoutput('sudo yum install vsftpd -y')
	print "</pre>"




