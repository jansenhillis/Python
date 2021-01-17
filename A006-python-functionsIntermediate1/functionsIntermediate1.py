import random

# impl of randInt(<min>, <max>) using random
# Modulus sets the upper bound, late addition of min sets the lower bound
# (max + 1) to make sure the maximum value is included in the result inclusively
def randInt(min = 0, max = 100):
    # basic type checking
    if not isinstance(min, int):
        return "minimum is not an integer"
    elif not isinstance(max, int):
        return "maximum is not an integer"

    # basic range check
    if (min > max):
        return "minimum cannot be larger than maximum"

    num = (round(random.random() * 100) % ((max + 1) - min)) + min
    return num


print(randInt())                    # should print a random integer between 0 to 100
# print(randInt(max=50))              # should print a random integer between 0 to 50
# print(randInt(min=50))              # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))     # should print a random integer between 50 and 500
# print(randInt(200))                 # min > max -> error
# print(randInt(min = 200))           # mix > max -> error
# print(randInt(0, 0))                # 0 to 0 test
# print(randInt(-10, 10))             # negative lower bound test
# print(randInt(-10, -5))             # negative upper and lower bounds test
# print(randInt("a"))                 # string min bounds test
# print(randInt(10, "b"))             # string max bounds test
# print(randInt("a", "b"))            # string upper and lower bounds test
# print(randInt(None))                # null input test



