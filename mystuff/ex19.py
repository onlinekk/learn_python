def cheese_and_crackers(cheese_count, boxes_of_crackers): #定义函数
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the function numbers directly:" #输出
cheese_and_crackers(20, 30) #调用函数，直接用数字为参数


print "OR, we can use variables from our script:"
amount_of_cheese = 10 #定义变量
amount_of_crackers = 50 #定义变量

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #调用函数，用变量为参数


print "We can even do math inside too:" #输出
cheese_and_crackers(10 + 20, 5 + 6) #调用函数，用数学表达式为参数


print "And we can combine the two, variables and math:" #输出
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #调用函数，用变量 + 数学表达式为参数