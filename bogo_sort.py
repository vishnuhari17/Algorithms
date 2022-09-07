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
so the first thing it's going"""

