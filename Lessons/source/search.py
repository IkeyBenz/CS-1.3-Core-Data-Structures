#!python

def linear_search(array, item):
  """return the first index of item in array or None if item is not found"""
  # implement linear_search_iterative and linear_search_recursive below, then
  # change this to call your implementation to verify it passes all tests
  # return linear_search_iterative(array, item)
  return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
  # loop over all array values until item is found
  for index, value in enumerate(array):
    if item == value:
      return index  # found
  return None  # not found


def linear_search_recursive(array, item, index=0):
  
  if index >= len(array):
    return None
  if array[index] == item:
    return index

  return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
  """return the index of item in sorted array or None if item is not found"""
  # implement binary_search_iterative and binary_search_recursive below, then
  # change this to call your implementation to verify it passes all tests
  # return binary_search_iterative(array, item)
  return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
  start, stop = 0, len(array) - 1

  midpoint = (start + stop) // 2

  while array[midpoint] is not item and start < stop:
    if array[midpoint] < item:
      start = midpoint + 1
    else:
      stop = midpoint
    midpoint = (start + stop) // 2

  if array[midpoint] is item:
    return midpoint
  
  return None


def binary_search_recursive(array, item, left=None, right=None):
  if not left: left = 0
  if not right: right = len(array) - 1

  midpoint = (right + left) // 2

  if array[midpoint] == item:
    return midpoint
  elif left == right:
    return None
  elif array[midpoint] > item:
    return binary_search_recursive(array, item, left, midpoint)
  return binary_search_recursive(array, item, midpoint+1, right) # +1 because we floor the midpoint
  

# EXAMPLE:
#   array = [1,2,3,4,5,6], item = 2
#   
#   left | right | midpoint | array[midpoint]
#     0  |   5   |    2     |       3        
#     0  |   2   |    1     |       2    == item -> return midpoint (1)
# 
#   array = [1,2,3,4,5,6], item = 6
#   left | right | midpoint | array[midpoint]
#     0  |   5   |    2     |       3
#     2  |   5   |    3     |       4
#     3  |   5   |    4     |       5
#     4  |   5   |    4