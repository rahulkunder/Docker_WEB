#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

f = cgi.FieldStorage()
def custom():
    name = f.getvalue("x")
    image = f.getvalue("y")
    o = subprocess.getoutput("sudo docker run -id --name {} {}".format(name,image))
    print("Output \n" + o)


def cmd():
  #  f=cgi.FieldStorage()
    cmd = f.getvalue("x")
    o = subprocess.getoutput("sudo " +  cmd)
    print("Output \n" + o)


if f.getvalue("y"):
    custom()
else:
    cmd()


