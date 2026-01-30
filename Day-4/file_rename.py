import os
from pathlib import WindowsPath

input_path = input('enter file path: ')
path1 = WindowsPath(input_path.replace('"', ''))
rename_path = input('enter file path: ')
path2 = WindowsPath(rename_path.replace('"', ''))
os.rename(path1,rename_path)