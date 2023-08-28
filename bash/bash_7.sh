# While loop

#!/bin/bash

# Contoh 1
n=1 # Initialize n variable to 1

while [ $n -le 5 ]; do # Start a while loop that will run as long as n <= 5

    echo "Iteration number $n" # Print the current iteration number

    ((n+=1)) # Increment n by 1

done # End the while loop

# Contoh 2
n=0 # Initialize counter variable n to 0

command=$1 # Get first command line argument into variable command

while ! $command && [ $n -le 5 ]; do # Keep looping while command is false AND n <= 5

    sleep $n # Sleep for n seconds

    ((n+=1)) # Increment n

    echo "Retry #$n" # Print retry message

done