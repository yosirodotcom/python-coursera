# This prints the last 10 lines of the syslog log file. Useful for viewing the end of a continuously updated log.
user@ubuntu:~$ tail /var/log/syslog

# This pipes the output of tail to the cut command. cut splits each line on spaces (-d' ') and prints from the 5th field to the end of the line (-f5-).
# This cuts out the timestamp and program name from each line, printing just the log message.
user@ubuntu:~$ tail /var/log/syslog | cut -d' ' -f5-

# This cuts each line of syslog after the first 4 fields, sorts the lines, 
# counts duplicate lines with uniq -c, sorts numerically in reverse order, 
# and takes the top 10 lines.
# This gives you a count of the top 10 most frequent log messages in the syslog file.
user@ubuntu:~$ cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head


#!/bin/bash

for logfile in /var/log/*log; do # Loop through all files ending in .log in /var/log

    echo "Processing: $logfile" # Print current logfile name
    
    cut -d' ' -f5- $logfile | # Cut out first 4 fields from each line
    sort | # Sort lines
    uniq -c | # Count duplicate lines
    sort -nr | # Sort by count in descending order
    head -5 # Print top 5 lines
    
done