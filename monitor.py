#!/usr/bin/env python3
from os import path, makedirs
from time import time
import psutil

script_path = path.dirname(path.realpath(__file__))
logs_path = f"{script_path}/logs"
timestamp = time()

# Create logs folder if not exists
if not path.exists(logs_path):
    makedirs(logs_path)

# open log files
cpu_log = open(f"{logs_path}/cpu.csv", "a")
mem_log = open(f"{logs_path}/mem.csv", "a")
disk_log = open(f"{logs_path}/disk.csv", "a")

# Get resources info
virtual_memory = psutil.virtual_memory()._asdict()
disk_usage = psutil.disk_usage('/')._asdict()
memory_total = virtual_memory.get('total')
memory_available = virtual_memory.get('available')

# Calculate resources free percent
cpu_free_percent = round(100 - psutil.cpu_percent(interval=1), 1)
memory_free_percent = round(memory_available / memory_total * 100, 1)
disk_free_percent = round(disk_usage.get('free')/1024/1024/1024, 1)

# print(timestamp, cpu_free_percent, memory_free_percent, disk_free_percent)

# Write logs
cpu_log.write(f"{timestamp},{cpu_free_percent}\n")
mem_log.write(f"{timestamp},{memory_free_percent}\n")
disk_log.write(f"{timestamp},{disk_free_percent}\n")

# Close opend files
cpu_log.close()
mem_log.close()
disk_log.close()
