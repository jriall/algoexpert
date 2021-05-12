# Bubble Sort
# Write a function that takes in an array of integers and returns a sorted
# version of that array. Use the Bubble Sort algorithm to sort the array.

# Solution

def bubble_sort(array):
  is_sorted = False
  counter = 0
  while not is_sorted:
    is_sorted = True
    for index in range(len(array) - 1 - counter):
      if array[index] > array[index + 1]:
        temp = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temp
        is_sorted = False
    counter += 1
  return array
