# Using lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
result = list1 + list2
result = [x + y for x, y in zip(list1, list2)]  # Manual element-wise addition
print(result)  # [6, 6, 6, 6, 6]

# # Using NumPy arrays
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
# array2 = np.array([5, 4, 3, 2, 1])
# result = array1 + array2  # Automatic element-wise addition
# print(result)  # [6 6 6 6 6]
