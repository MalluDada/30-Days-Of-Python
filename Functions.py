
a =int(input('Enter a: '))
b = int(input('Enter b: '))

def add_two_numbers(a,b):
   sum = a + b
   return sum
print(add_two_numbers(a,b))

add_two_numbers(a,b)

r = int(input('Enter radius: '))


def area_of_circle(r):
   pi = 3.14
   area = pi * r**2
   return area
print('Area Of Circle:',area_of_circle(r))


def addition(*nums):
    total = 0

    for num in nums:
       if type(num) != int:
            return "All numbers should be integers"
       else:
         total += num

       
    return total 

print(addition(2,4,7))
print(addition(2,'HEELO',5,6))

def celcius_to_farenheit(c):
    f = (c*9/5)+32
    return f
print(celcius_to_farenheit(35))


Autumn = ["September", "October", "November"]
Winter = ["December", "January", "February"]
Spring = ["March", "April", "May"]

def check_season(month):
    if month in Autumn:
        return "Autumn"
    elif month in Winter:
        return "Winter"
    elif month in Spring:
        return "Spring"
    else:
         return "Summer"
    
   
print(check_season("October"))
  
def solve_quadratic_eqn(a,b,c):
    d = b**2 - 4*a*c

    if d < 0:
      return "No real roots exist"
    
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    return x1,x2
print(solve_quadratic_eqn(4,10,5))

fruit_list = ["Banana", "Apple", "Mango"]

def print_list(fruits):
    for fruit in fruits:
     print(fruit)

print_list(fruit_list)



def reverse(list):
    reverse_list = []
    for i in range(len(list)-1,-1,-1):
     reverse_list.append(list[i])
    print(reverse_list)


reverse([1,2,3,4])

def even_and_odd(n):
    odd = 0
    even = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    
    print("even:{} and odd:{}".format(even,odd))


even_and_odd(10)

def add_item(my_list,item):
    my_list.append(item)
    return my_list


print(add_item([1,2,3,4],5))

def odd_sum(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i

    return total
        
        
print(odd_sum(10))

def find_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    
    return factorial


print(find_factorial(3))


def is_empty(value):
    if len(value) == 0:
        return "It is empty"
    else:
        return "It is not empty"


print(is_empty(""))
print(is_empty("My name is Malhar"))

def greet(name = "Guest"):
    if len(name) == 0:
        return "Hello Guest!"

    else:
        return "Hello {}!".format(name)

print(greet("Malhar"))
print(greet())


def show_args(**args):
    for key,value in args.items():
        print("{}: {}".format(key, value))


show_args(name="Alice", age=30, city="New York")





n = int(input("Enter your number: "))
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(n))
