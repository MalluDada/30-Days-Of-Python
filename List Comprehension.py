
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

zero_and_negative_numbers = [i for i in numbers if i<= 0]

print(zero_and_negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [number for row in list_of_lists for number in row]

print(flat)

pattern = [(n,1,n**2,n**3,n**4,n**5) for n in range(11)]
print(pattern)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [[item[0][0].upper(), item[0][0][:3].upper(), item[0][1].upper()]
          for item in countries]
print(result)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_name = [[name[0][0] + ' ' +name[0][1]]
             for name in names]
print(full_name)


# Using lambda 

slope = lambda x1,y1,x2,y2 : (y2 - y1)/(x2-x1)
print(slope(6,7,14,15))
