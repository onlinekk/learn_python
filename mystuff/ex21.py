def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACT %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a / b
	

print "Let's do some math with just functions!"

age = add(30, 5)            #把计算的结果赋给变量（即只赋给return后的量），字符串没有，下同
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq) 


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) #实际运算顺序：÷×-+；函数返回值可以直接作为函数的参数
What = age + height - weight * (iq / 2) #另一种表达式

print "That becomes: ", what,"(",What,")", "Can you do it by hand?\n"

print "This is a new one: 24 + 34 / 100 - 1023"
print "F1: \n", 24 + 34 / 100 - 1023 ,"\n"
print "F2: \n", add(24, subtract(divide(34, 100), 1023)), "\n"
print "F3: \n", subtract(add(24, divide(34, 100)), 1023), "\n"
print "\n"