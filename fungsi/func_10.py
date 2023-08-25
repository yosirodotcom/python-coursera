# menggabungkan string key dan string value as a list pada dictionary

def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.  
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name". 
            full_names.append(first_name+" "+last_name)
            
    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations. 
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']
