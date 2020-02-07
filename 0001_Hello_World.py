print ("Hello Word")  #print is the first function I had learned in Python
print('Dongdong likes playing games')
print('Meimei likes watching Daddy playing games')
print("This is the first sentence.\
This is the second sentence.")
age = 20
name = "Roy"
print('{0} was {1} years old'.format(name,age))
print('Why is {0} playing with that python?'.format(name))
print(f'{name} was {age} years old when he wrote this book')  # notice the 'f' before the string
print(f'Why is {name} playing with that python?')  # notice the 'f' before the string

# decimal (.) precision of 3 for float '0.333'
print('{0:.4f}'.format(1/3))
# fill with underscore (_) with the text centered
# (^) to 11 width '____________hello_________________'
print('{0:_^20}'.format('hello'))
# keyword-based 'Roy wrote A Python Code'
print('{name} wrote {book}'.format(name='Roy',book='A Python Code'))
#define and print - maybe the better way???
book="2 Python Code"
print(f'{name} wrote {book}')

#numerical operations
print(2+3)
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')
print("\"test\"")

#print no line
print('a')
print('b')
print('a',end='')
print('b',end='\n')
print('a',end=' ')
print('b',end=' ')
print('c')

#print Escape Sequences
print("What's your problem")
print('What\'s your problem')
print("What\"s your problem")
print('This is the first line.\nThis is the second line')
print("This is the first line.\
This line will continue")

print(r"Newlines are indicated by \n")
print("Newlines are not indicated by \n")

#start from 2019/09/02 - study on data



