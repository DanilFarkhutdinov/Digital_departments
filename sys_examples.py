import sys

print(sys.version)
print(sys.version_info)

print(sys.argv)

if len(sys.argv) < 3:
    print("Ошибка")
    exit(1)
sourse_dir = sys.argv[1]
dest_dir = sys.argv[2]
print('source_dir', sourse_dir)
print('dest_dir', dest_dir)
