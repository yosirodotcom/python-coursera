import os
import datetime
# file information

# check file size
os.path.getsize("spider.txt")

# check date
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
