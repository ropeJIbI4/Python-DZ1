# Напишите программу для. проверки истинности утверждения not(X or Y or Z) = not X and not Y and not Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.
X=True
X1=False
Y=True
Y1=False
Z=True
Z1=False
def Right(a, b, c):
    action_1 = not (a or b or c)
    action_2 = not a and not b and not c
    print(action_1,action_2)
    return action_1 == action_2
print(Right(X,Y,Z))
print(Right(X1,Y,Z))
print(Right(X,Y1,Z))
print(Right(X,Y,Z1))
print(Right(X,Y1,Z1))
print(Right(X1,Y1,Z1))
print(Right(X1,Y,Z1))
