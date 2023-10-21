import filecmp
import shutil
import tempfile
import zipfile
from pathlib import Path

files_dir = Path("files")

result = filecmp.cmp(files_dir / 'file.txt', files_dir / 'file2.txt')
print(result)

result2 = filecmp.cmpfiles('files', 'files2', ['file.txt'])
print(result2)


#shutil.rmtree('files2')

#$shutil.copytree('files', 'files2')
print(shutil.disk_usage('.'))

with tempfile.NamedTemporaryFile(suffix='.zip') as temp_file:
    print(temp_file.name)
    with zipfile.ZipFile(temp_file.name, 'w') as zipfile:
        zipfile.write(files_dir / 'file.txt', 'file.txt')
        zipfile.write(files_dir / 'file2.txt', 'file2.txt')