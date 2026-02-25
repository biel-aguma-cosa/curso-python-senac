people = {}

print("NEW USER")
name = input('Name: ')

people[name] = {
    'name' : name,
    'email' : input('EMail: '),
    'password' : input('Password: '),
    'birthday' : [
        int(input("BIRTHDAY\n- day:")),
        int(input("- month:")),
        int(input("- year:"))
    ],
    'height' : float(input("MISCELLANEOUS\nHeight (m): ")),
    'weight' : float(input("Weight (kg): ")),
    'access' : input("ACCESS\nLevel: ")
}

print('\n\n\n\n\n\n')
for data in people[name]:
    print(str(data)+": "+str(people[name][data]))
print()
for data in people[name]:
    print(str(data)+": "+str(type(people[name][data])))
