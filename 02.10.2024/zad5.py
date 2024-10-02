import numpy as np

SIZE_X, SIZE_Y = 5, 5

array = np.array(range(1, SIZE_X * SIZE_Y + 1))
print(array)

array_2d = array.reshape((SIZE_X, SIZE_Y))
print(array_2d)

extracted_array_2d = array_2d[:, [1, 2, 3]]
print(extracted_array_2d)
