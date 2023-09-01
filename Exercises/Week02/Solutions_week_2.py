# Week 2
# Example Solutions to Exercises

#---------------------------------------------------------------

# Part 1 -  Conditional Statements
# Exercise 1 - Conditional Statements (Essential)

# 1
a = 2
b = 3
num = a - b

if num < 0:
    print('negative')
elif num > 0:
    print('positive')
else:
    print('zero')
    
# 2
valentina = 30
hendrik = 30
anthony = 30

if (valentina > 40 and hendrik > 40 and anthony > 40):
    print('All student passed')
    
elif (valentina > 40 or hendrik > 40 or anthony > 40):
    print('Some students passed')
    
else:
    print('No students passed')
    
# 3
x = 20

if x > 10:
    x = x - 20

elif x < 2:
    x = x + 21
    
else:
    x = x * 2.5
    
print(x)

# Assignment operators can also be used for variable re-assignment
x = 20

if x > 10:
    x -= 20

elif x < 2:
    x += 21
    
else:
    x *= 2.5
    
print(x)

# 4
n = input('Enter a number: ')
n = int(n)

if n % 2 == 0: 
    print('even')
    
else:
    print('odd')
    
# OR

n = input('Enter a number: ')
n = int(n)

if n % 2: 
    print('odd')
    
else:
    print('even')
    

#---------------------------------------------------------------

# Exercise 2 - Modelling using conditional statements (Essential)
 
# 1
GBP = 25
R = 1.38
if GBP < 50:
    M = 0.9
elif 50 <= GBP < 500:
    M = 0.92
elif 500 <= GBP < 5_000:
    M = 0.95
elif 5_000 <= GBP < 50_000:
    M = 0.97
else:
    M = 0.98
 
USD = GBP * M * R

print('USD=', USD, ', effective exchange rate=', USD/GBP)
#---------------------------------------------------------------

# Exercise 3 - More conditional statements (Advanced)

# 1
# Coordinates of a point
p_x = -3
p_y = 0

# Coordinates of circle centres
c1_x = 0
c1_y = 0

c2_x = 2
c2_y = 1

c3_x = -5
c3_y = 0

# Radius of each circle
c1_r = 5
c2_r = 2
c3_r = 3

# Euclidean distance from the point to each of the circle centres
p_to_c1 = ((p_x - c1_x)**2 + (p_y - c1_y)**2)**(1/2)
p_to_c2 = ((p_x - c2_x)**2 + (p_y - c2_y)**2)**(1/2)
p_to_c3 = ((p_x - c3_x)**2 + (p_y - c3_y)**2)**(1/2)

print(P_to_C3)

# Test if point lies in each circle:
# Check if the distance from the point to the centre of the circle is less than 
# or equal to the radius of the circle. 
if p_to_c2 <= c2_r:
    print("The point ", p_x, ',', p_y, " is in circle C2.")
    # If p is in c2, it is also in c1
    print("The point ", p_x, ',', p_y, " is in circle C1.") 
    
elif p_to_c1 <= c1_r:
    print("The point ", p_x, ',', p_y, " is in circle C1.")
        
if p_to_c3 <= c3_r:
    print("The point ", p_x, ',', p_y, " is in circle C3.")   
    
#---------------------------------------------------------------

# Part 2 User input and nested control statements
# Exercise 4 - User Input(Essential)

# 1 
num = int(input('Enter a number: '))

if num < 0:
    print('negative')
elif num > 0:
    print('positive')
else:
    print('zero')
    
    
# 2
name = input('Enter your name: ')
print('Your name ends with the letter ', name[-1])

# Exercise 3 - Nested control statements (Essential)

# 1
name = input('Enter student name: ')
score = int(input('Enter student score: '))

if score >= 40:
    if 40 <= score < 50:
        G = 'D'
    elif 50 <= score < 60:
        G = 'C'
    elif 60 <= score < 70:
        G = 'B'
    else:
        G = 'A'
        
    print(name, ' passed with grade ', G)
    
else:
    print(name, ' failed')
    
# 2
# A - Using comparison operators
n = input('Enter a number: ')
n = int(n)

if n % 2 == 0: 
    print('even')
    
    if n % 4 == 0:
        print('multiple of 4')
    
else:
    print('odd')
    
    if n % 3 == 0:
        print('multiple of 3')
        
# OR

n = input('Enter a number: ')
n = int(n)

if n % 2 : 
    print('odd')
    
    if n % 3 == 0:
        print('multiple of 3')
    
else:
    print('even')
    
    if n % 4 == 0:
        print('multiple of 4')
        
        
# B - Using logical operators
n = input('Enter a number: ')
n = int(n)

if n % 2 : 
    print('odd')
    
    if not n % 3:
        print('multiple of 3')
    
else:
    print('even')
    
    if not n % 4 :
        print('multiple of 4')
    

# 3
key =  input(
'''You approach a castle.
The castle door is closed.
You find a key.
Do you pick up the key? (Y/N): ''')

if key == 'Y':
    print('Magic key turns you into a frog. \n You lose!')
    
elif key == 'N':
    print('Castle door opens.')
    castle = input('Do you enter the castle? (Y/N)')
    
    if castle == 'Y':
        print('Find treasure.\nYou win!')
    elif castle == 'N':
        print('No treasure.\nYou lose!')
else:
    print('Invalid input. Exiting game.')
        
    
      
# 4
n = input('Enter a number, n: ')

n = int(n)

if n > 10:
    
    print('n greater than 10')    
    

else:
    
    m = input('Enter another number, m: ')
    
    m = int(m)

    if n*m > 10:
        print('n * m greater than 10')
    

    
        
    



