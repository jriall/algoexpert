# Min Max Stack Construction

# Write a MinMaxStack class for a Min Max Stack. The class should support:

# Pushing and popping values on and off the stack.
# Peeking at the value at the top of the stack.
# Getting both the minimum and the maximum values in the stack at any given
# point in time.
# All class methods, when considered independently, should run in constant time 
# and with constant space.

# Solution

class MinMaxStack:
  def __init__(self):
    self.stack = []

  def peek(self):
    return self.stack[-1]['value']

  def pop(self):
    return self.stack.pop()['value']

  def push(self, number):
    if len(self.stack) == 0:
      minimum = number
      maximum = number
    else:
      head = self.stack[-1]
      minimum = min(number, head['minimum'])
      maximum = max(number, head['maximum'])
    self.stack.append({
      'value': number,
      'minimum': minimum,
      'maximum': maximum,
    })    

  def getMin(self):
    return self.stack[-1]['minimum']

  def getMax(self):
    return self.stack[-1]['maximum']
