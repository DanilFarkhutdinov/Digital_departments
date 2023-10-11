file = open("main.py", "r") #rb бинарный
print(file.read())
file.close()

# with open("calculator.py", "r") as file:
#     for line in file:
#         print(line.strip())
#     file.close()

with open ("file.txt", "a+") as file:
    file.write("123")
    file.seek(0)
    print(file.read())