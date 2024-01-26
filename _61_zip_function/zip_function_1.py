usernames = ['Dude', 'Joe', 'Sally', 'Sam']
passwords = ['123', 'abc456', '789', 'q000']
login_date = ["01/01/2020", "01/02/2020", "01/03/2020", "01/04/2020"]

users = zip(usernames, passwords, login_date)

for user in users: 
    print(user)
    