import re
import csv
from collections import defaultdict

# Initialize dictionaries
error_dict = defaultdict(int)
per_user = defaultdict(lambda: {"INFO": 0, "ERROR": 0})

# Read syslog data and process log entries
with open("syslog.log", "r") as syslogfile:
    for line in syslogfile:
        info_match = re.search(r"ticky: INFO ([\w\s]*) \[#\d+\] \(([\w.]+)\)", line)
        error_match = re.search(r"ticky: ERROR ([\w\s]*) \(([\w.]+)\)", line)

        if info_match:
            user = info_match.group(2)
            per_user[user]["INFO"] += 1

        if error_match:
            message = error_match.group(1)
            user = error_match.group(2)
            per_user[user]["ERROR"] += 1
            error_dict[message] += 1

# Sort error dictionary by count and add column names
sorted_errors = [("Error", "Count")] + sorted(
    error_dict.items(), key=lambda x: x[1], reverse=True
)

# Sort per_user dictionary by username and add column names
sorted_users = [("Username", "INFO", "ERROR")]
for user, counts in sorted(per_user.items()):
    sorted_users.append((user, counts["INFO"], counts["ERROR"]))

# Write sorted data to CSV files
with open("error_message.csv", "w", newline="") as error_csvfile:
    csvwriter = csv.writer(error_csvfile)
    csvwriter.writerows(sorted_errors)

with open("user_statistics.csv", "w", newline="") as user_csvfile:
    csvwriter = csv.writer(user_csvfile)
    csvwriter.writerows(sorted_users)
