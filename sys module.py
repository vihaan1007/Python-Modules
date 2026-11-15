import sys
a=sys.platform,sys.maxsize, sys.version
print(a)
b=sys.path
print(b)
if(sys.platform[:3] == "win"):
    print("Hello windows user")
elif(sys.platform[:3] == "mac"):
    print("Hello macbook user") 
elif(sys.platform[:5] == "linux"):
    print("Hello linux user")
