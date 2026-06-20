# Area of Triangle
base= float(input("Enter base length "))
height= float(input("Enter height length "))
Area_of_triangle= 1/2*base*height

print('Area Of triangle is ',Area_of_triangle )

# Euclidean Triangle
x_1= float(input("Enter x1  "))
y_1= float(input("Enter y1  "))
x_2= float(input("Enter x2  "))
y_2= float(input("Enter y2  "))

Slope= float((y_2 - y_1)/(x_2 - x_1))
Euclidean_distance= float((x_2 - x_1)**2 +  (y_2 - y_1)**2)**(1/2)
print('Slope is ', Slope)
print('Euclidean Distance is  ',Euclidean_distance)

# Using in operator
print('jargon in full of jargon ',  'jargon' in 'full of jargon')

# Bill Calculation
hours= int(input("Enter hours: "))
rate_per_hour= float(input("Enter rate per hour: "))
print('Total bill is:  ', hours*rate_per_hour)


# Power Table

n = 1
print(n, 1, n, n**2, n**3)

n = 2
print(n, 1, n, n**2, n**3)

n = 3
print(n, 1, n, n**2, n**3)

n = 4
print(n, 1, n, n**2, n**3)

n = 5
print(n, 1, n, n**2, n**3)