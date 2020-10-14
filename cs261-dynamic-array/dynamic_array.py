# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Baleria Reyes
import numpy as np
class DynamicArray:
    def __init__(self):
        pass
        self.emptyArray = 0
        self.capacity = 10
        self.myArray = np.ndarray(0)

    def capacity(self):
        return self.capacity

    def is_empty(self):
        return True

    def __getitem__(self):
        return self.myArray

    def __len__(self):
        return 0

    # def append(self):
        
