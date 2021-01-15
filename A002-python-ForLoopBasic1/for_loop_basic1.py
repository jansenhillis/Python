#1. Basic - print all integers from 0 to 150
for i in range(151):
    print(i)

#2. Multiple of Five - print all multiples of 5 from 5 to 1000
for i in range(5, 1005, 5):
    print(i)

#3. Counting, the Dojo Way - print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo"
for i in range(1, 101, 1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum
sum = 0
for i in range(500001):
    if i % 2 != 0: #odd
        sum += i
print("Sum: " + str(sum))

#5. Countdown by Fours - print positive numbers starting at 2018, counting down by 4
for i in range(2019, 0, -4):
    print(i)

#6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum, to highNum, 
# print only ints that are multiple of mult. 
lowNum = 0
highNum = 10
mult = 3
for i in range(lowNum, highNum, mult):
    if (i % mult == 0): #integers that are multiples of mult
        print(i)

