import getpass, warnings
a= getpass.getpass(prompt="Tell the Password: ")
if(a != "Password"):
    warnings.filterwarnings("error")
    warnings.warn("wrong Password")

print(a)
user = getpass.getuser()
print(user)
