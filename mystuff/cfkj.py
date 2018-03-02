for i in range(1,10):
	for j in range(1,i + 1):
		print "%d*%d=%2d " % (j, i, i*j),
	print ""
print "\n"                                 
		
for i in range(1,10):
     for j in range(1,10):
        print "%d*%d=%2d " % (j,i,i*j),
print "\n"


for i in range(1, 10):
	for j in range(i, 10):
		print "%d*%d=%2d " % (i,j,i*j),
	print " "
print "\n"

for i in range(1, 10):
	print " " * 7 * (i - 1),
	for j in range(i, 10):
		print "%d*%d=%2d" % (i,j,i*j),
	print " "
print "\n"