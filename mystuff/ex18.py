﻿#this one is like your scripts with argv
def print_two(*args):  #注意此处有冒号,用以结束本行
	arg1, arg2 = args  #将参数解包
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *argv is actually pointless, we can just this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#this one takes no argument
def print_none():
	print "I got nothin'."
	
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()