import sys
from load import load_numbers
numbers = load_numbers(sys.argv[1])
# The above code is just to load the data for the program

def quicksort(values):
    # Faster than bogo sort
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_numbers = quicksort(numbers)
print(sorted_numbers)