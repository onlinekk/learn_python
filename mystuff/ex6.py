x = "There are %d types of people." % 10   #将右边的字符串赋给变量x
binary = "binary" #定义变量binary，下同
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
 
print x #输出变量x代表的字符串
print y

print "I said: %r." % x  #将变量x代表的字符串填入格式化符%所在的位置，采用repr()的显示
print "I also said: '%s'." % y #将变量y代表的字符串填入格式化符%所在的位置，采用str()的显示

hilarious = False #将布尔值False赋给变量hilarious
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e

# 格式化字符串时，Python使用一个字符串作为模板。
# 模板中有格式符，这些格式符为真实值预留位置，并说明真实数值应该呈现的格式。
# Python用一个tuple将多个值传递给模板，每个值对应一个格式符。
# 这些值可以是数字、字符串、布尔值、变量等