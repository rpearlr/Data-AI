import psutil
cpu_usage=psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory()
print(f"Total RAM: {ram_usage.total / (1024**3):.2f} GB")
print(f"Used RAM: {ram_usage.used / (1024**3):.2f} GB")
print(f"RAM Usage Percentage: {ram_usage.percent}%")