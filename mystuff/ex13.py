from sys import argv                  #载入参数变量

script, first, second, third = argv   #解包，将用户执行命令时输入的参数值（在argv中）赋给四个变量

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third