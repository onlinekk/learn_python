from sys import argv  #从python的内置模块sys中将参数变量功能引入脚本中将参数变量功能引入脚本

script, filename = argv #将argv解包，将在执行命令时赋给argv的参数值分给script与filename连个变量
 
txt = open(filename)  #将open()接收参数（filename代表的文件名的字符串）后的返回值（file object）赋给变量txt

print "Here's your file %r:" % filename #输出
print txt.read() #对变量txt代表的文件执行read()命令（或函数）,并将结果打印输出

txt.close()#关闭文件


print "Type the filename again:" #输出
file_again = raw_input("> ") #输入文件名，并将名称字符赋给变量file_again

txt_again = open(file_again)#将open()接收参数（file_again代表的文件名的字符串）后的返回值（file object）赋给变量txt_again

print txt_again.read() #对txt_again代表的文件执行read()命令，并将结果打印输出

txt_again.close()#关闭文件