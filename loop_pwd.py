

#else working in loop
for i in range(3):
    password = input("Enter password: ")
    if password == 'secret':
        print("Password accepted")
        break
else:
    print("No imput attempts letf or all passwords entered wrongly ")
    

#nested loops
for i in range(3):
    for j in range(3):
        print(f"{i},{j}")


#multiplication table

n = 5
for i in range(1, n+1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i*j}", end='\t')
    #move to a new line
    print()
    