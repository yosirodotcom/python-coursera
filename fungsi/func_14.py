# Mencari nilai ganjil di antara rentang nilai tertentu


# The function accepts two variable integers through the parameters and
# returns all odd numbers between x and y-1.
def odd_numbers(x, y):
    # This list comprehension uses a for loop to iterate through values
    # of n in a range from x to y, with the value of y excluded (meaning
    # keep the default range() function behavior to exclude the
    # end-of-range value from the range). Since an incremental value is not
    # specified, the range function uses the default increment of +1.
    # The if condition checks n to test if the number is odd using the
    # modulo operator. This condition is written to check if n is divided
    # by 2, that the remainder is not 0.
    return [n for n in range(x, y) if n % 2 != 0]


# Call the years() function with two parameters.
print(odd_numbers(5, 15))
# Should print [5, 7, 9, 11, 13]
