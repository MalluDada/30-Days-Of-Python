empty_tuple = ()

print(empty_tuple)


brothers = ('Malhar', 'Rushabh', 'Nisarg', 'Urvish')

sisters = ('Nancy', 'Dolly', 'Mahima', 'Muskan', 'Ayushi')

siblings = brothers + sisters

print(siblings)
print(len(siblings))

parents = ('Bhupendra', 'Rita')


family_members = siblings + parents

print(family_members)

*siblings, father, mother = family_members
print(siblings)
print(father)
print(mother)