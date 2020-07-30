import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# A integer number
# What was the smallest number you could have seen, what was the largest?
# 5, 19

# What did you see on line 2?
# A odd number
# What was the smallest number you could have seen, what was the largest?
# 3, 9
# Could line 2 have produced a 4?
# Can not, the step is 2

# What did you see on line 3?
# A float number
# What was the smallest number you could have seen, what was the largest?
# 2.5, 5.499999……

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 101))
