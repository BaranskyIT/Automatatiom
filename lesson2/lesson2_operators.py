# user_login = "adam"
# user_pass = "Qwerty12345"

# login = input("Login: ")
# password = input("Password: ")

# if login == user_login and password == user_pass:
#     print("Все верно")
# else:
#     print("Все неверно")

crit1 = "red"
crit2 = "lock"

color = input("Color: ")
feature = input("Feature: ")

if color == crit1 and feature == crit2:
    print("100% Беру!")
elif color == crit1 or feature == crit2:
    print("Можно взять")
else:
    print("Посмотрю еще")