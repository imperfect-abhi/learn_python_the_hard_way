# We will see how print statement is used along with how arithmetic operations are being performed.
# We first count the number of chickens which includes Hens and Roosters.
print("I will now count my chickens:")

print("Hens\n", 25 + 30 / 6)
print("Roosters\n", 100 - 25 * 3 % 4)

# Then we count the number of eggs
print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# We then make a few test of inequalities. However, this first line of code
# prints  a string and shouldn't be confused with performing arithmetic operations.
print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")


# In the below statements we can observe how the return type of the comparisons
# made are booleans.
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)