# menyusun string secara terbalik

def mirrored_string(my_string):
  forwards = ""
  backwards = ""
    # The for loop iterates through each character of the "my_string"
  for character in my_string:
      # The if-statement checks if the character is not a space.
      if character.isalpha():
          # If True, the body of the loop adds the character to the
          # to the end of "forwards" and to the front of
          # "backwards". 
          forwards += character
          backwards = character + backwards
          print(forwards, backwards)
      # If False (meaning the character is not a letter), no action
      # is needed. This coding approach results prevents any 
      # non-alphabetical characters from being written to the
      # "forwards" and "backwards" variables. The for loop will 
      # restart until all characters in "my_string" have been
      # processed.      
  # The final if-statement compares the "forwards" and "backwards"
  # strings to see if the letters are the same both forwards and
  # backwards. Since Python is case sensitive, the two strings will 
  # need to be converted to use the same case for this comparison.   
  if forwards.lower() == backwards.lower():
      return True
  return False 
print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True