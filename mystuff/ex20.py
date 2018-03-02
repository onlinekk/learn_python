from sys import argv #从模块中引入变量

script, input_file = argv #解包

def print_all(f): #定义函数，一个参数，函数功能是读取文件内容并打印
    print f.read()

def rewind(f): #定义单参数函数，功能是回到文件的0字节处
	f.seek(1, 0) #从开头处（0）开始偏移，偏移1个字节
	
def print_a_line(line_count, f): #定义双参数函数，功能是打印出行数，读取文件的一行内容并显示
	print line_count, f.readline()
	
current_file = open(input_file) #打开文件，将fileobject传递给变量current_file

print "First let's print the whole file:\n" #打印

print_all(current_file) #调用函数

print "Now let's rewind, kind of like a type."#打印

rewind(current_file)#调用函数

print "Let's print three lines:" #打印

current_line = 1 #定义新变量
print_a_line(current_line, current_file) #调用函数

current_line += 1 #更新变量
print_a_line(current_line, current_file) #调用函数

current_line += 1
print_a_line(current_line, current_file)

current_file.close()