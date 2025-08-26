
'''import platform 

# printing the Architecture of the OS
print("[+] Architecture:", platform.architecture()[0])

import platform

# printing the Architecture of the OS
print("[+] Architecture :", platform.architecture()[0])

# Displaying the machine
print("[+] Machine :", platform.machine())


# printing the Operating System release information
print("[+] Operating System Release :", platform.release())

# prints the currently using system name
print("[+] System Name :",platform.system())

# This line will print the version of your Operating System
print("[+] Operating System Version :", platform.version())

# This will print the Node or hostname of your Operating System
print("[+] Node: " + platform.node())

# This will print your system platform
print("[+] Platform :", platform.platform())

# This will print the processor information
print("[+] Processor :",platform.processor())

print("[+] MAchne:", platform.machine)
# printing the Operating System release information
print("[+] Operating System Release :", platform.release())

# prints the currently using system name
print("[+] System Name :",platform.system())

# This line will print the version of your Operating System
print("[+] Operating System Version :", platform.version())

# This will print the Node or hostname of your Operating System
print("[+] Node: " + platform.node())

# This will print your system platform
print("[+] Platform :", platform.platform())

# This will print the processor information
print("[+] Processor :",platform.processor())

from datetime import datetime
import psutil

# Using the psutil library to get the boot time of the system
boot_time = datetime.fromtimestamp(psutil.boot_time())
print("[+] System Boot Time :", boot_time)

# getting thesystem up time from the uptime file at proc directory
with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()

        uptime = int(float(uptime))
        uptime_hours = uptime // 3600
        uptime_minutes = (uptime % 3600) // 60
        print("[+] System Uptime : " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")



import os

pids = []
for subdir in os.listdir('/proc'):
        if subdir.isdigit():
                    pids.append(subdir)
                    print('Total number of processes : {0}'.format(len(pids)))




import pwd

users = pwd.getpwall()
for user in users:
        print(user.pw_name, user.pw_shell)
'''
