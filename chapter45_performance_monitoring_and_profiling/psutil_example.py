import psutil as psutil

CPU_usage = psutil.cpu_percent(interval=1, percpu=True)
ram = psutil.virtual_memory()

print(f'CPU: {CPU_usage} ')
print(f'RAM: {ram}')