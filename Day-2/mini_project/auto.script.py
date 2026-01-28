import shutil
import datetime
import os
import sys
def write_to_file() :
  newpath = r"C:\Users\User\Desktop\details"
  if not os.path.isdir(newpath):
      os.mkdir(newpath)
  t = datetime.datetime.now().strftime("%H-%M-%S")
  formatted="".join(str(datetime.date.today())).join(t)
  path=rf"{newpath}\detail_{formatted}.txt"
  text="Lorem Ipsum"
  with open(path, "a") as f:
      f.write(f"{text}")

import schedule
import time

schedule.every(2).minutes.do(write_to_file)
while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute
