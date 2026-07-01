
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

other_companies = ('OpenAI', 'Nvidia', 'Adobe')

it_companies.update(other_companies)

print(it_companies)

it_companies.pop()

print(it_companies)

it_companies.remove('OpenAI')
print(it_companies)

it_companies.discard('Oracle')
print(it_companies)
'''
'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print(C)

print(B.intersection(A))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.isdisjoint(A))

D = B.union(A)
print(D)

print(A.symmetric_difference(B))
print(A.difference(B))

del A
del B

print(B)

age = [22, 19, 24, 25, 26, 24, 25, 24]

set_age = set(age)

print(len(age))
print(len(set_age))

sentence = 'I am a teacher and I love to inspire and teach people'

sentences = set(sentence.split())

print(sentences)
