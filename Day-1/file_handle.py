import shutil
import datetime
import os
from pathlib import Path
newpath = r"C:\Users\User\Desktop\backup_3"
os.mkdir(newpath)
os.mkdir(rf"{newpath}\backup_jpeg")
os.mkdir(rf"{newpath}\backup_png")
sourcepath=r"C:\Users\User\Downloads"
file_name=["cartoon","pngtree","jpeg-home","jpegxt-home"]
for i in file_name :
  file = Path(rf"{sourcepath}\{i}")
  ext = file.suffix
  if(ext == ".jpg") :
    shutil.move(rf"{sourcepath}\{i}",rf"{newpath}\backup_jpeg")
  else :
    shutil.move(rf"{sourcepath}\{i}",rf"{newpath}\backup_png")

