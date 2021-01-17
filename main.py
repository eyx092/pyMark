print("pyMark v1.0.0")
print("Starting...")

import calendar, time
from random import randint
from datetime import datetime
import platform, subprocess
import psutil #pip install psutil

peak_cpu_usage = 0

def get_processor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        return subprocess.check_output(command, shell=True).strip()
    return ""

print("To start pyMark, press 'S' and then enter.")
init = input("To exit, type 'exit' and then enter: ")
if init == 's':
    print("WARNING! You may exprience a decrease in performance")
    print("on other applications while this benchmark is running.")
    confirm_init = input("Continue (Y/N)? ")
    if confirm_init == 'y':
        current_epoch = calendar.timegm(time.gmtime())
        print("Running the benchmark...")
        print("|", end="")
        for i in range(100000000):
            x = randint(1,9999999999999999)
            y = randint(1,9999999999999999)
            z = x / y
            current_cpu_usage = psutil.cpu_percent(interval=None)
            if current_cpu_usage > peak_cpu_usage:
                peak_cpu_usage = current_cpu_usage
            if i % 10000000 == 0:
                print("\u2593", end="")
        epoch = calendar.timegm(time.gmtime())
        print("|", end="")
        print()
        runtime = epoch - current_epoch
        benchmark = 100000000/(runtime)
        runtime_min = runtime // 60
        runtime_sec = runtime % 60
        log = open("log.txt","a")
        log.write("\n")
        log.write("\n")
        print("PyMark Score:", benchmark)
        log.write("PyMarkScore: "+str(benchmark))
        log.write("\n")
        print("Total Benchmark Runtime:", runtime_min, "min", runtime_sec, "sec")
        log.write("Total Benchmark Runtime: "+str(runtime_min)+" min "+str(runtime_sec)+" sec")
        log.write("\n")
        print("Processor:", get_processor_info())
        log.write("Processor: "+str(get_processor_info()))
        log.write("\n")
        print("Cores:",psutil.cpu_count())
        log.write("Cores: "+str(psutil.cpu_count()))
        log.write("\n")
        print("Physical Cores:",psutil.cpu_count(logical=False))
        log.write("Physical Cores: "+str(psutil.cpu_count(logical=False)))
        log.write("\n")
        print("Logical Cores:",psutil.cpu_count(logical=True))
        log.write("Logical Cores: "+str(psutil.cpu_count(logical=True)))
        log.write("\n")
        print("Peak CPU Usage: ",peak_cpu_usage,"%",sep="")
        log.write("Peak CPU Usage: "+str(peak_cpu_usage)+"%")
        log.write("\n")
        print("Platform:",platform.system())
        log.write("Platform: "+str(platform.system()))
        log.write("\n")
        log.write("Date & Time: "+str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        log.close()
        time.sleep(10)
        print("Closing the application...")
    elif confirm_init == 'n':
        print("Closing the application...")
    else:
        print("Command not found. Closing the application...")
elif init == 'exit':
    print("Closing the application...")
else:
    print("Command not found. Closing the application...")
