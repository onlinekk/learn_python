def num(n1, n2):
	print "I have %d pair of shoes and %d pens" % (n1, n2)
	print "\n"

num(2, 3) #1
num(1+1, 2+1)#2

shu1 = 3*6
shu2 = 100.0/6.0
print "I want to tell you that",
num(shu1, shu2) #3

print "Input 2 numbers first please"
s1 = int(raw_input("Enter the 1st number: "))
s2 = int(raw_input("Enter the 2nd number: "))
print "hi, do you know that",
num(s1, s2) #4