AB = []
text_A = input('Введите А ')
temp_A =text_A.split()
A= list(map(int,temp_A))
AB.append(A)
text_B = input('Введите B ')
temp_B = text_B.split()
B = list(map(int,temp_B))
AB.append(B)

def find_distance_AB(AB):
    point_A, point_B = AB
    AB_disane = 0
    for i in range(len(point_A)):
        AB_temp = (point_B[i]-point_A[i])**2
        AB_disane += AB_temp
    return AB_disane**0.5

print(AB)
print(find_distance_AB(AB))