#1. Hello World
print("Hello World")

#2. Hello Your Name
name = "Jansen"
print("Hello " + name)
print("Hello", name)

#3. Hello Num
# Convert num to a string so concatenation will work 
num = "111"
print("Hello " + num)
print("Hello", num)

#4. I love food
food1 = "Chinese"
food2 = "Sushi"
print("I love to eat {} and {}".format(food1, food2))
print(f"I love to eat {food1} and {food2}")

#5 String explore
str = "world"
print(str.capitalize())
print(str.isalpha())
print(str.isdecimal())
print(str.join(food2))