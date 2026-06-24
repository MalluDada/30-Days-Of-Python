dog = {'name' : 'Nancy', 'Colour' : 'Golden', 'breed' :'Golden Retriever', 'Legs' : '4', 'age': '1 year'}
print(dog)

Student_dict = {'first_name' : 'Malhar', 'last_name' : 'Sagara', 'gender' : 'Male', 'age' : '19', 'marital_status' : 'Unmarried', 'skills' : ['Coding', 'Dancing', 'Singing']}
print(len(Student_dict))

print(Student_dict['skills'])
print(type(Student_dict['skills']))


Student_dict['skills'].extend(['Managing', 'Cricket'])

print(Student_dict)

keys = Student_dict.keys()
print(keys)

Student_dict.pop('marital_status')
print(Student_dict)

del dog
print(dog)