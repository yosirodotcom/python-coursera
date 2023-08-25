## Di dalam bash:

# untuk mengarahkan ke folder data
# $> cd data

# untuk mengecek isi folder
# $> ls

# untuk membuka isi file text atau csv
# $> cat employees.csv

# berpindah ke folder lain ( yang berada di atas )
# cd ~/scripts

# buka terminal python nano
# nano generate_report.py
# tulis kode di dalam nano seperti ini

# shebang
#!/usr/bin/env python3
import csv

# The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
csv.register_dialect("empDialect", skipinitialspace=True, strict=True)


def read_employees(csv_file_location):
    employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


employee_list = read_employees("/home/<username>/data/employees.csv")
print(employee_list)


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ":" + str(dictionary[k]) + "\n")
        f.close()


write_report(dictionary, "/home/<username>/data/report.txt")

# exit nano Ctrl+O Enter Ctrl+X

## Di dalam bash:

# For the file to run it needs to have execute permission (x). Let's update the file permissions
# and then try running the file. Use the following command to add execute permission to the file

# $> chmod +x generate_report.py

# Now test the function by running the file using the following command:

# $> ./generate_report.py
