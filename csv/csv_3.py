# membuat csv file dari data dictionary
import csv

users = [
    {
        "name": "Sol Mansi",
        "username": "solm",
        "departmen": "IT infrastructure"
    },
    {
        "name": "Lio Nelson",
        "username": "lion",
        "departmen": "User Experience Research"
    },
    {
        "name": "Chalie Grey",
        "username": "greyc",
        "departmen": "Development"
    },
    
]

keys = ["name", "username", "departmen"]

with open('by_department.csv', 'w') as by_department:
    writer =csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

