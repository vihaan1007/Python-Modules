import pathlib
import os

print(os.getcwd())
print(pathlib.Path.cwd())

#print(os.path.join('name', 'name2)) =
#print(pathlib.Path('name/name2')) =
#print(pathlib.Path('name1') / 'name2')
#print(pathlib.Path.expanduser("name"))
print(pathlib.Path.home())
from pathlib import Path
Path("module/ans1").resolve()
Path("module/ans1").absolute()
os_path=os.path.join("ans1", "ans2")
p_path=Path("ans1", "ans2")
print(p_path.name)
#Path('name').mkdir()
#to make if a folder exists
#Path("name").mkdir(exist_ok=True)
#file inside folder:
#Path('answers/newfile.txt').touch()

#checking
p=Path("answers")#not a path
print(bool(p.is_file()))#False
print(bool(p.is_dir()))#False
parent=p.parent
print(bool(p.parent.is_file()))
print(bool(p.parent.is_dir()))
print(bool(p.exists()))
from pathlib import Path

p = Path("answers")

if p.exists():
    if p.is_file():
        print("This is a file")
    elif p.is_dir():
        print("This is a directory")

    if parent.is_dir():
        print("Parent is a directory")
    else:
        print("Parent is a file")
else:
    print("Path does not exist")
#Stat
#Path("name").stat()
#Path("name").owner()
#Path("name").group()
