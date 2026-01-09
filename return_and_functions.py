# returning multiple values
def get_user():
    name = "Ivan"
    age = 25
    retrun name, age


user_name, user_age = get_user()
print(user_name, user_age)