"""
The function that randomizes the order of the list is kept in the
"random" module, so we need to import that here
"""
import random
"""
The sys.argv list gives us the command line arguments to the 
script. To use it, we also need to inmport the "sys" module.
"""
import sys
"""Here's where we import the load_numbers function from above.
"""
from load import load_numbers

"""
And here, we pass the first command line argument (which should be
the path to a file) to load_numbers, and store the returned list of numbers
in a variable.
"""
numbers = load_numbers(sys.argv[1])

"""
Bogosort just randomly rearranges the list of values over and over,
so the first thing it's going to need is a function to detect whether
the list is sorted. We'll write an is_sorted functon that takes a
list of values as a parameter. It will return True if the list
passsed in is sorted, or False if it isn't.
"""
def is_sorted(values):
    """
    We'll loop through the numeric index of each value in the list
    from 0 to one less than the length of the list. Like many
    languages, Python list indexes begin at 0, so a list with a
    length of 5 has indexes going from 0 through 4.
    """
    for index in range(len(values) - 1):
        """
        If the list is sorted,then every value in it will be less than
        the ones that comes after it. So we test to see whether the 
        current item is GREATER than the ones that follows it.
        """
    if values[index] > values[index +10]:
        """
        If it is, it means the whole list is not sorted, so we return False."""
        return False
    """
    If we get down here, it means the loop completed without finding any
    unsorted values. (Python used whitespace to mark code blocks, so un-indenting
    the code like this marks the end of the loop.)
    Since  all the values are sorted,we can return True"""
    return True

def bogo_sort(values):
    # To sort values until they satisfy the condition required
    while not is_sorted(values):
        random.shuffle(values)
        # When it satisfies the condition the while loop ends
    return values

print(bogo_sort(numbers))
