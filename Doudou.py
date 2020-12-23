# name = 'douya'
# age = 7
# weight = 7.1
# allIsNothing = False
#
# print(type(name))
# print(type(age))
# print(type(weight))
# print(type(allIsNothing))
#
# array = [1, "douya"]
# print(type(array))
# print('豆芽%03d岁' % age)
# print('豆芽%d岁 %.1f千克重' % (age, weight))
#
# # 自动转换
# print('豆芽%d岁' % allIsNothing)  # 0
# print('豆芽%d岁' % weight)  # 7
# print('豆芽%s岁' % weight)
#
# sentence = f'\t豆芽猫{age}岁,\n{weight}kg重'
# print(sentence)
#
# print(age, end='####\n')

# 第三节
# 输入

text = input('请输入密码:')
print(f'你输入的密码是{text}')
# input接收到的都为str
print(type(text))

# 类型转换 int() float() str() tuple() list() eval()
number = int(text)
print(type(number))

# 运算符
#  // 整除商  ** 指数
# 1 - 0.5 = 0.5
# 9 // 4 = 2
# 2 * 0.5 = 1.0
# 4 / 2 = 2.0  除法特殊 都是小数

# 多变量赋值
num, name, weight = 7, 'douya', 7.1
print(f'{num}, {name}, {weight}')

# 多变量赋同一值
a = b = 9



# 符合运算
b = 2
a += b
print(a)
a *= b
print(a)
a /= b
print(a)

# 符合运算符的优先级: 先算符合运算右边的表达式 再进行符合运算

# 逻辑运算符
# 与: and  或: or 非: not
# 书写习惯: 将两边的表达式用括号括起来

# 数字间的逻辑运算
# and: 如果有0 则返回0  不然 返回最后一个数字
# or: 如果所有值为0 则返回0  不然返回第一个数字
