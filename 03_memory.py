import numpy as np 
import sys 

# python takes more memory
python_list = list(range(100))
x = sys.getsizeof(python_list[0])* len(python_list)
print(x)  #2800

#numpy takes less memory 
numpy_array = np.arange(100)
y = numpy_array.nbytes
print(y) #800 

