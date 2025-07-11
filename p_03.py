# LESSON 5: Conditions and If Statements 🧠
# Ask the user for their age. If they are 18 or older, print:
# 👉 "You are an adult."
# Otherwise, print:
# 👉 "You are not an adult yet."

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an adult.")
else: 
    print("You are not an adult yet.") 
    
    

# Ask the user to enter a number.

# 👉 If it’s even(i.e., divisible by 2), print "That's an even number."
# 👉 If it’s odd, print "That's an odd number."

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("That's an even number.")
else:
    print("That's an odd number.")