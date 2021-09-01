username = input()
password = input()

try_password = input()

while try_password != password:
    try_password = input()
else:
    print(f'Welcome {username}!')