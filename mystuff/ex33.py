i = 0
numbers = []

# while i < 6:
	# print "At the top i is ", i
	# numbers.append(i)
	
	# i = i + 1
	# print "Number now: ", numbers
	# print "At the bottom i is %d" % i
	
def xh(k, p):
	global i 
	while i <= k: #若不加global i，则由于是在函数内部，且对i进行了<操作，i会被作为局部变量处理，而此时i这个“局部变量”显然是没有被定义的。
	              #若不用global i，也可以用for i in range（k），此时由于i在for开始时即被定义。
				  #可以看出，while中的i必须是已经定义过的变量，而for中的i是在for执行时随即定义的
		print "At the top i is ", i
		numbers.append(i)
	
		i = i + p
		print "Number now: ", numbers
		print "At the bottom i is %d" % i
	
k = int(raw_input('> Insert an limit int: '))
p = int(raw_input('> Insert an step int: '))
xh(k, p)

print "The numbers: "

for num in numbers:
	print num