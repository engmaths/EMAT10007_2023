# Week 1
# Example Solutions to Exercises

#---------------------------------------------------------------

# Introduction
import keyword
print(keyword.kwlist)

#---------------------------------------------------------------

# Part 1 - Variables
# Exercise 1 - Numbers and Arithmetic Operators (Essential)

# 1
a = 6
b = 5

# 2
print(a + b)

# 3 
e = a * b

# 4
e = (a+b)/3

# 5
print(a % b)

# 6
l, w, h = 1, 4, 5
v_cuboid = l * w * h

#---------------------------------------------------------------

# Exercise 2 - Strings (Essential)

# 1
c = 'Hello'
d = 'world'

# 2
new_string = (c + ' ' + d)
print(new_string)

# 3
print(c[2])

#4
print(d[2:5])
print(d[2:])
print(d[-3:])

#---------------------------------------------------------------

# Exercise 3 - Modelling with variables (Essential)

# 1
pi = 3.142
r = 1                         # Radius
a_centre = pi * r **2         # Area of cross section through sphere centre
v_sphere = (4/3) * pi * r**3  # Volume of a sphere
print(v_sphere)


#---------------------------------------------------------------

# Exercise 4 - More variables (Advanced)

# 1
# square root of r
print(r ** (1/2)) 

# round a number to nearest integer
p = 10.7
rounded = (p + 0.5) // 1
print('P rounded=', rounded)



# B 

val = False
var = True 

print(val + var)
print(val * var)
print(val % var)

#---------------------------------------------------------------

# Part 2 Operators
# Exercise 5 - Comparison Operators (Essential)


# 1 
print(a > b)

# 2
print(type(a) == type(b))

# 3
print(c[0] == d[0])



# #---------------------------------------------------------------

# Exercise 6 - Logical Operators (Essential)

# 1
print (not(a % 2) and not(b % 2))

# 2
print (not(a % 2) or not(b % 2))

# 3
Valentina = 70
Hendrik = 65
Anthony = 30

print(Valentina > 40 or Hendrik > 40 or Anthony > 40)

# #---------------------------------------------------------------

# Exercise 7 - Modelling with Operators (Essential)

# 1
print('The volume of the sphere is greater: ', v_sphere > v_cuboid)

cuboid_greater = v_cuboid > v_sphere
print('The volume of the cuboid is greater: ', cuboid_greater)

# 2
eats_plants = True
eats_meat = False

herbivore = eats_plants and not eats_meat
carnivore = eats_meat and not eats_plants
omnivore = eats_plants and eats_meat

# #---------------------------------------------------------------

# Exercise 8 - More Operators (Advanced)

# 1
n = 23
square = (n ** (1/2)) / int (n ** (1/2)) == 1
print(square)









