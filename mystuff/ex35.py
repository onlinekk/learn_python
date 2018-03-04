# -*- coding:UTF-8 -*-
from sys import exit 

def gold_romm(): #对用户输入的数据进行处理，字符中含有“0”或“1”且数值不大于50，可以“安全退出”，若大于50，则会“死”；若输入的不含有0或1则提示
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")
	if "0" in next or "1" in next: #若next中含有字符“1”或者“0”
		how_much = int(next)
	else:
		dead("Man, learn to type a number.") #调用dead函数
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0) #退出程序
	else:
		dead("You greedy bastard!")
		
		
def bear_room():
	print "There is bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved: #1
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True #运行此代码块后，bear_moved的值即被改变
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your legs off.")
		elif next == "open door" and bear_moved: #只有先运行代码块1后，才能运行此代码块
			gold_romm()
		else:
			print "I got no idea what that means."
			
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next: #为真时，返回至start()，即程序开头
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room() #若输入的不是flee“或“head”，则返回至函数开始
		
		
def dead(why):
	print why, "Good job!" #若why是字符(串)，则输出时与Good job在一行
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start() #调用start函数