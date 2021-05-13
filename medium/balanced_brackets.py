# Balanced Brackets
# Write a function that takes in a string made up of brackets ((, [, {, ), ],
# and }) and other optional characters. The function should return a boolean
# representing whether the string is balanced with regards to brackets.

# A string is said to be balanced if it has as many opening brackets of a
# certain type as it has closing brackets of that type and if no bracket is
# unmatched. Note that an opening bracket can't match a corresponding closing
# bracket that comes before it, and similarly, a closing bracket can't match a
# corresponding opening bracket that comes after it. Also, brackets can't
# overlap each other as in [(]).

# Sample Input
# string = "([])(){}(())()()"
# Sample Output
# true // it's balanced

# Solution

def balanced_brackets(string):
  left_brackets = []
  brackets = {')': '(', '}': '{', ']': '['}
  for char in string:
    if char in brackets.values():
      left_brackets.append(char)
    elif char in brackets.keys():
      if len(left_brackets) and left_brackets[-1] == brackets[char]:
        left_brackets.pop()
      else:
        return False
  return not bool(len(left_brackets))
