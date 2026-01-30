import os
import shutil

temp_path=r"C:\Temp"
for file in os.listdir(temp_path) :
  file_path = os.path.join(temp_path,file)
  if os.path.isdir(file_path) :
    shutil.rmtree(file_path)
  else :
    os.remove(file_path)
