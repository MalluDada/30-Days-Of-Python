'''
age = int(input("Enter your age "))
remaining_years = 18 - age
if age >= 18: 
    print("You are eligible to drive")
else:
    print("You have to wait for {} more years to be eligible to drive".format(remaining_years))
'''

'''
my_age = 19

your_age = int(input("Enter Your Age: "))

if your_age > my_age:
    if your_age - my_age == 1:
            print("You are 1 year older than me")
    else:
          print("You are {} years older than me".format(your_age - my_age))
elif  my_age - your_age == 1 :
    print("You are 1 year younger than me") 
else:
      print("You are {} years younger than me".format(my_age - your_age))  

'''
'''
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >=70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

'''
'''
Autumn = ['September', 'October', 'November']
spring = [' March', 'April', 'May']
Winter = ['December', 'January', 'February']

month = input("Enter Month: ")

if month in Autumn:
    print("Autumn")
elif month in spring:
    print("Spring")
elif month in Winter:
    print("Winter")
else:
    print("Summer")
'''

person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
      }
    }


if 'skills' in person:
    print(person['skills'][len(person['skills']) // 2])


    if 'skills' in person:
        if 'Python' in person['skills']:
            print("Python is a skill")
        else:

            print("Python is not a skill")


skills = person['skills']


if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
    print('He is a front end developer')

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')

elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')

else:
    print("Not a  Developer")


if person['is_married'] == True and person['country'] == 'Finland':
        print("{} {} lives in {}. He is married".format(person['first_name'], person['last_name'], person['country']))
else:
        print("Not Married")