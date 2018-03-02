def break_words(stuff):
	"""This function will break up words for us.""" #这些语句是 文档注释，在使用帮助命令时会显示，用以向用户说明
	words = stuff.split(' ')  #括号中是' ',引号中间是一个空格，即以空格为分隔符，分隔后是以列表的形式储存
	return words  #将句子分散成词
	
def sort_words(words):
	"""sort the words."""
	return sorted(words)  #给词按照首字母顺序排序，相同的按第二个字母，以此类推
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0) 
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words the prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
	
	
#下面是在powershell中运行时的输入和显示
	
# >>> import ex25    调用ex25.py  在这里，ex25.py就是一个模块，调用时不用加py。 
                     #也可以使用 from ex25 import *来调用，这样下面在使用ex25.py中的函数时就不需要再加ex25.了
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)       ex25.break_words(sentence)表示调用ex25.py中的 break_words(sentence)函数
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']  这是一个列表
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words   words在这里是一个列表，虽然是全局变量，但是可以对其进行操作。pop（0）(即移除列表中的第一个元素)之后，就没有第一个词了，就像f.readline()一样
# ['good', 'things', 'come', 'to', 'those', 'who']   
# >>> ex25.print_last_word(sorted_words)
# who
# >>> ex25.print_first_word(sorted_words)
# All
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>>
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who