# returning multiple values
def get_user():
    name = "Ivan"
    age = 25
    return name, age


user_name, user_age = get_user()
print(user_name, user_age)


### Returing a Functi0on
def power(exponent):
    def inner(base):
        return base ** exponent
    return inner


square = power(2)
print(square(3))


cube = power(3)
print(cube(3))