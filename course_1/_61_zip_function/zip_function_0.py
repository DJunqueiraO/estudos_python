usernames = ['Dude', 'Joe', 'Sally', 'Sam']
passwords = ['123', 'abc456', '789', 'q000']

users = dict(zip(usernames, passwords))

print(type(users))

for key, value in users.items(): 
    print(f"{key} : {value}")
    