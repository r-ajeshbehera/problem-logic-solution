'''LESSON 12: Lists — Storing and Working with Collections 📦'''
'''Problem 1: Even Number List
Write a function get_even_numbers(lst) that:

Takes a list of numbers

Returns a new list containing only even numbers'''
def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0] 
  
'''Problem 2: Reverse a List (Without [::-1])
Write a function reverse_list(lst) that:

Takes a list

Returns the same list in reverse order (e.g., [1, 2, 3] → [3, 2, 1])

Don’t use built-in reverse or slicing

🧠 Hint: Use a loop to go from the end to the start and append to a new list.'''
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst
  
  

