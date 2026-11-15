import random

x=random.randint(1,6)
print(x)
y=random.random()
print(y)
mylist=["rock", "paper", "scissor"]
z=random.choice(mylist)
print(z)
cards=[1,2,3,4,5,6,7,8,9,10,"A","Q","K","J"]
random.shuffle(cards)
print(cards)

#myprogram

Mylist=["rock","paper","scissor"]
a=random.choice(Mylist)
b=input("your choice among scissor,paper,rock= ")
if(a == "rock"):
    if(b == "scissor"):
        print("python wins")
    elif(b == "paper"):
        print("you win")
    else:
        print("tie")

elif(a == "scissor"):
    if(b == "paper"):
        print("python wins")
    elif(b == "rock"):
        print("you win")
    else:
        print("tie")

elif(a == "paper"):
    if(b == "rock"):
        print("python wins")
    elif(b == "scissor"):
        print("you win")
    else:
        print("tie")