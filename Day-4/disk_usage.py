import shutil

total, free, used = shutil.disk_usage(path = "/")

total_gb =  round(total/1024**3,2)
free_gb = round(free/1024**3,2)
used_gb = round(used/1024**3,2)

print(f"Total GB availible : {total_gb}")
print(f"Used GB availible : {used_gb}")
print(f"Free GB availible : {free_gb}")