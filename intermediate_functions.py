x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
student[0]['last_name'] = 'Bryant'
print(student[0])
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print(z[0])

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def name_list(names):
    for i in range (0,len(names)):
        new_list=''
        for key,val in names[i].items():
            new list += f'{key} - {val}, '
        print(new_list)
name_list(students)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for i in range(0, len(students)):
    print(students[i]['first_name'])

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

for i in range(0, len(students)):
    print(students[i]['last_name'])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, val in some_dict.items():
        print(f'{len(val)} {key.upper()}')
        for i in range(len(val)):
            print(val[i])


printInfo(dojo)