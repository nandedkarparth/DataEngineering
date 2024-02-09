from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print("Original List:", numbers)
print("Product of List Elements:", product)
