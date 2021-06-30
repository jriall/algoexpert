# Staircase Traversal

# You're given two positive integers representing the height of a staircase and
# the maximum number of steps that you can advance up the staircase at a time.
# Write a function that returns the number of ways in which you can climb the
# staircase.

# For example, if you were given a staircase of height = 3 and maxSteps = 2 you
# could climb the staircase in 3 ways. You could take 1 step, 1 step, then 1
# step, you could also take 1 step, then 2 steps, and you could take 2 steps,
# then 1 step.

# Note that maxSteps <= height will always be true.

# Sample Input
# height = 4
# maxSteps = 2
# Sample Output
# 5
# // You can climb the staircase in the following ways: 
# // 1, 1, 1, 1
# // 1, 1, 2
# // 1, 2, 1
# // 2, 1, 1
# // 2, 2

# Recursive solution

def staircaseTraversal(height, maxSteps):
  cache = {0: 1, 1: 1}
  return staircaseTraversalHelper(height, maxSteps, cache)

def staircaseTraversalHelper(height, maxSteps, cache):
  if height in cache:
    return cache[height]
  result = 0
  for step in range(1, min(maxSteps, height) + 1):
    result += staircaseTraversal(height - step, maxSteps) 
  cache[height] = result
  return result

# Iterative solution

def staircaseTraversal(height, maxSteps):
  steps = [0 for num in range(height + 1)]
  steps[0] = 1
  steps[1] = 1
  for step in range(2, height + 1):
    result = 1
    while result <= maxSteps and result <= step:
      steps[step] = steps[step] + steps[step - result]
      result += 1
  return steps[height]

# Improved iterative solution (from solutions video)

def staircaseTraversal(height, maxSteps):
  steps = [1]
  curr = 0
  for step in range(1, height + 1):
    start = step - maxSteps - 1
    end = step - 1
    if start >= 0:
      curr -= steps[start]
    curr += steps[end]
    steps.append(curr)
  return steps[-1]
