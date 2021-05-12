# Selection Sort
# Write a function that takes in an array of integers and returns a sorted
# version of that array. Use the Selection Sort algorithm to sort the array.

def selection_sort(array):
  for i in range(len(array)):
    smallest = i
    for j in range(i, len(array)):
      if array[j] < array[smallest]:
        smallest = j
    if smallest != i:
      swap_places(i, smallest, array)
  return array


def swap_places(first, second, array):
  array[first], array[second] = array[second], array[first]
