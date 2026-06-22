#String Concatenation

course = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(course))

#Playinng with Strings
company = "Coding for All"


print(len(company))

print(company.upper())

print(company.capitalize())
print(company.title())
print(company.swapcase())

#Slicing a string
slice = company[7:]
print(slice)

#Checking a word in string 
sub_string= 'Coding'
print(company.index(sub_string))
print(company.find(sub_string))
print('Coding' in company)

#replacing a word
company= company.replace('Coding','Python')
print(company)
print(company[:11] + 'Everyone')

words= company.split()
words[2] = 'Everyone'

print(' '.join(words))

# Using Split
companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

course= 'Coding For All'
words= course.split()

print(words[0][0] + words[1][0] +words [2][0])

#index
first_word= 'C'
print(course.index(first_word))

sentence= 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])


#Using tab sequence

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#formating string

radius = 10
area = 3.14 * radius**2

formatted_string= 'The area of a circle with radius {} is {} meters square.'.format(radius,area)
print(formatted_string)



a = 8
b = 6

print('{} + {}= {}'.format(a,b,a+b))

print('{} - {}= {}'.format(a,b,a-b))

print('{} * {}= {}'.format(a,b,a*b))

print('{} / {}= {:.2f}'.format(a,b,a/b))

print('{} % {}= {}'.format(a,b, a%b))

print('{} // {}= {}'.format(a,b,a//b))

print('{} ** {}= {}'.format(a,b,a**b))