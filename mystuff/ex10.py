tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat fodd
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#附加内容
while True:
	for i in ["/","-","|","\\",",","|"]:   #开始时此处忘了加冒号
		print "%s\r" % i,
		
# k = 0
# while True:
	 # for k in [k + 1]:   
		 # print "%d" % k,