import timeit

# Define the code for a for-loop to create a list of squares
for_loop_code = """
squares = []
for x in range(1000000):
    squares.append(x**2)
"""

# Define the code for list comprehension to create a list of squares
list_comprehension_code = """
squares = [x**2 for x in range(1000000)]
"""

# Measure the time taken by the for-loop
for_loop_time = timeit.timeit(for_loop_code, number=10)

# Measure the time taken by list comprehension
list_comprehension_time = timeit.timeit(list_comprehension_code, number=10)

# Print the results
print(f"Time taken by for-loop: {for_loop_time} seconds")
print(f"Time taken by list comprehension: {list_comprehension_time} seconds")