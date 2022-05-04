import math
AB = int(input())
BC= int(input())
AC = round(math.sqrt(pow(AB, 2) + pow(BC, 2)))
print(AC)
new_AC = AC / 2
new_BC = BC / 2
teta = math.cos(new_BC / new_AC )
print(round(int(math.degrees(teta))))
 