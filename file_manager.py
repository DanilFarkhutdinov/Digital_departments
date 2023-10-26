import os

cur_path = os.getcwd()


while True:
    print("Выберите команду:")
    print("pwd - просмотр теĸущей папĸи")
    print("cd - переход в другую папĸу")
    print("touch - создание пустого файла")
    print("cat - вывод содержимого файла")
    print("ls - вывод списĸа файлов в папĸе")
    print("rm - удаление файла")
    print()

    s = input()
    print()

    if len(s.split()) > 1:
        command, path = s.split()
    else:
        command = s
        path = ''
    if command == "pwd":
        print("Текущая папка: ", cur_path)
        print()
    elif command == "cd":
        if os.path.exists(os.path.join(cur_path, path)):
            os.chdir(os.path.join(cur_path, path))
            cur_path = os.path.join(cur_path, path)
    elif command == "touch":
        try:
            file = open(path, 'w')
            file.close()
        except:
            pass
    elif command == "cat":
        try:
            with open(path) as file:
                for line in file:
                    print(line.rstrip())
                    print()
        except:
            pass
    elif command == "ls":
        dir_list = os.listdir(cur_path)
        print(dir_list)
        print()
    elif command == "rm":
        try:
            os.remove(path)
        except:
            pass
    else:
        print("Неправильно введена команда")
        print()