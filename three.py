print('Введите X = ')
x =int(input())
print('Введите Y = ')
y =int(input())
print(x, y)
if x==0 and y==0 :
    print('Ошибка')
elif (x > 0 and y > 0):
    print('1')
elif (x < 0 and y > 0):
    print('2')
elif (x < 0 and y < 0):
    print('3')
else:
    print('4')
