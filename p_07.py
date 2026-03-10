# LESSON 9: Function Parameters and Return Values
# Write a function that takes two numbers and returns their product.
def product(a, b):
  return (a*b)
value = product(3, 4)
print(value)
'''Problem 1: Age Checker Function
Write a function can_vote(age) that:

Takes an age

Returns True if age is 18 or more, else False

Then, print a message using the return value'''

def can_vote(age):
  if age >= 18:
    return True
  else:
    return False
person=can_vote(20)
print(f"Can the person vote? {person}")

'''Problem 2: Word Repeater
Write a function repeat_word(word, times) that:

Takes a word and a number

Returns the word repeated that many times, separated by spaces'''

def repeat_word(word, times):
  return (word + " ") * times
result = repeat_word("hello", 3)
print(f"The repeated word is: {result}")  