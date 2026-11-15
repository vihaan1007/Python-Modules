import math
pii=-3.14
pi=3.14
x=1
y=2
z=3
print(round(pi))#round up or down
print(math.ceil(pi))#round up; ceiling
print(math.floor(pi))#round down; floor
print(abs(pi))#value from 0
print(abs(pii))
print(pow(pi, 2))#pi=base expo=2
print(math.sqrt(441))#no negative value
print(max(x, y, z))#largest
print(min(x, y, z))#smallest

#practice ques 1
a=int(input("a= "))
print(abs(a))
if(a < 0):
    print("negative number are not exepted")
else:
    print(math.sqrt(a))
print(math.ceil(a))
print(math.floor(a))

#practice ques 2

r=float(input("radius= "))
print("area=", 3.14 * (r ** 2) ,"and perimeter=", 2 * 3.14 * r)