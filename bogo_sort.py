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
        If the list is sorted,then every value """

