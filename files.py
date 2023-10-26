import os
from os import path
from pathlib import Path

file = open("main.py", "r") #rb бинарный
print(file.read())
file.close()

# with open("calculator.py", "r") as file:
#     for line in file:
#         print(line.strip())
#     file.close()

cur_path = os.getcwd()
files_dir = Path(cur_path) / "files"
print(files_dir)
try:
    files_dir.mkdir()
except:
    pass

file_path = files_dir / 'file.txt'

with file_path.open("a+") as file:
    #file.write("123")
    file.seek(0)
    print(file.read())

print(os.path.exists("file.txt"))

print(Path("file.txt").exists())

print(path.basename(file_path))
print(path.dirname(file_path))
print(path.splitext("file.txt"))

print(path.abspath(path.join("..", "testdir")))

print(os.environ.get("TEST", "value"))

