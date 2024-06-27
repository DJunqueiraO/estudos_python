from json import dumps, loads

usernames = ['Dude', 'Joe', 'Sally', 'Sam']
passwords = ['123', 'abc456', '789', 'q000']
login_date = ["01/01/2020", "01/02/2020", "01/03/2020", "01/04/2020"]

users = zip(usernames, passwords, login_date)

format_user = \
    lambda user:\
        f'{'{'}"name":"{user[0]}", "password":"{user[1]}", "login_date":"{user[2]}"{'}'}'

format_json = lambda json_str: dumps(loads(json_str), indent=2)

print(format_json("[" + ", ".join(map(format_user, users)) + "]"))