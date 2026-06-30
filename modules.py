import random

#characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
'''
def random_user_id():
    user_id =''
    for i in range(0,6):
            user_id += random.choice(characters)
            
    return user_id
print(random_user_id())
'''
'''
n = int(input("Enter length of ID: "))
m = int(input("Enter No. of Id's needed: "))


def user_id_gen_by_user():
    user_id =''
    for i in range(m):
        for j in range(n):
             
            user_id += random.choice(characters)
            if len(user_id) == n:
                print(user_id)
                user_id = ''

    
user_id_gen_by_user()
'''
'''
def rgb_color_gen():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)

    return "rgb({},{},{})".format(r,g,b)
print(rgb_color_gen())
'''
'''
allowed_char = '0123456789ABCDEF'
n = int(input("Enter No. of colours: "))


def list_of_hexa_colors():
    colour = '#'
    list = []
    for i in range(n):
        for  j in range(6):
            colour += random.choice(allowed_char)
            if len(colour) == 7:
                 list.append(colour)

           
           
        colour = '#'
    print(list)

list_of_hexa_colors()
'''
'''
def shuffle_list(items):
    shuffled_list = []
   

    for i in range(len(items)):
        random_index = items[random.choice(range(len(items)))]
        shuffled_list.append(random_index)
        items.remove(random_index)


    return shuffled_list
print(shuffle_list(['Mango', 'Chickoo', 'Banana']))
'''

def random_num(items):
    random_list =[]


    for i in range(len(items)):
        random_index = items[random.choice(range(len(items)))]
        random_list.append(random_index)
        items.remove(random_index)
        if len(random_list) == 7:
            print(random_list)
        else:
            continue



random_num([0,1,2,3,4,5,6,7,8,9])

