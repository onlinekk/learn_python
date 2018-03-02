print "How old are you?", #逗号可以让How old are you?与输入的数字同行
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %( #这里换行为了使每行不多于80个字符；不可以将（放在下一行
age, height, weight)