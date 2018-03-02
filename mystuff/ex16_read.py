from sys import argv
script, filename = argv
txt = open('ex16_test.txt')
print "The following is your file <%s>" % filename
print txt.read()
txt.close()