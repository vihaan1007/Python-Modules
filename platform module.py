import os
import platform
print(dir(platform))
print(platform.system())
print(platform.architecture())
print(platform.machine())

if platform.system() == "Linux":
   os.system("ls")
elif platform.system() == "Windows":
   os.system("dir")
else:
   print("unsupported module")

print(platform.python_version())
print(platform.python_version_tuple())