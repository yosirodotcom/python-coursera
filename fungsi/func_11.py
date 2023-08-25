# membalikkan key-value menjadi value-key di dalam dictionary yang baru
# ini bisa dilakukan jika nilai value terduplikasi pada nilai key lainnya

# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 


def invert_resource_dict(resource_dictionary):
  # Initialize a "new_dictionary" variable as a dict data type using
  # empty {} curly brackets. 
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the 
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}
