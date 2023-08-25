# The main program then calls these functions and checks if either the disk usage 
# is too low (less than 20%) or the CPU usage is too high (more than 75%). 
# If either condition is met, an error message is printed; otherwise, 
# a success message is printed. This code can be used to monitor the system's 
# disk and CPU health.


import shutil
import psutil

# Function to check disk usage percentage on a specified disk
def check_disk_usage(disk):
    # Get disk usage statistics using shutil.disk_usage
    du = shutil.disk_usage(disk)
    
    # Calculate the percentage of free space on the disk
    free = du.free / du.total * 100
    
    # Return True if free space is greater than 20%, indicating sufficient space
    return free > 20

# Function to check CPU usage percentage
def check_cpu_usage():
    # Get the CPU usage percentage using psutil.cpu_percent
    usage = psutil.cpu_percent(1)
    
    # Return True if CPU usage is less than 75%, indicating acceptable usage
    return usage < 75

# Main program logic
if not check_disk_usage("/") or not check_cpu_usage():
    # If either disk usage is low or CPU usage is high, print an error message
    print("ERROR!")
else:
    # If both disk usage is acceptable and CPU usage is within limits, print a success message
    print("Everything is OK!")