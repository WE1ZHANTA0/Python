# age = 20
# name = 'Swaroop'
#
# print('{} was {} years old when he wrote this book'.format(name, age))
# print('Why is {} playing with that python?'.format(name))
#
# # 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
# print('{0:.3f}'.format(1.0/3))
# # 填充下划线 (_) ，文本居中
# # 将 '___hello___' 的宽度扩充为 11
# print('{0:_^11}'.format('hello'))
# # 用基于关键字的方法打印显示 'Swaroop wrote A Byte of Python'
# print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#
# print('a', end=' ')
# print('b', end=' ')
# print('c')
#
# number = 23
# running = True

# while running:
#     guess = int(input('Enter an integer : '))
#
#     if guess == number:
#         print('Congratulations, you guessed it.')
#         # 这会导致 while 循环停止
#         running = False
#     elif guess < number:
#         print('No, it is a little higher than that.')
#     else:
#         print('No, it is a little lower than that.')
# else:
#     print('The while loop is over.')
#     # 你可以在此处继续进行其它你想做的操作
#
# print('Done')

# rangeArr = range(1, 5)
# print(rangeArr)
# for i in rangeArr:
#     print(i)
# else:
#     print('The for loop is over')

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')



