import random

# impl of randInt(<min>, <max>) using random
# Modulus sets the upper bound, late addition of min sets the lower bound
# (max + 1) to make sure the maximum value is included in the result inclusively
def randInt(min = 0, max = 100):
    
    num = (round(random.random() * 100) % ((max + 1) - min)) + min
    return num


# print(randInt())                  # should print a random integer between 0 to 100
# print(randInt(max=50))            # should print a random integer between 0 to 50
# print(randInt(min=50))            # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))   # should print a random integer between 50 and 500
# print(randInt(200))                 # min > max
print(randInt(min = 200))           # mix > max
# print(randInt(0, 0))                # max = 0
# print(randInt(-10, 10))
# print(randInt(-10, -5))


