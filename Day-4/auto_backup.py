import shutil
import datetime
from pathlib import WindowsPath

input_path = input('enter file path: ')
path = WindowsPath(input_path.replace('"', ''))
t = datetime.datetime.now().strftime("%H-%M-%S")
formatted="".join(str(datetime.date.today())).join(t)
newpath = rf"C:\Users\User\Desktop\bill2_{formatted}.txt"
shutil.copy(path,newpath)