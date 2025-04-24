

#else working in loop
for i in range(3):
    password = input("Enter password: ")
    if password == 'secret':
        print("Password accepted")
        break
else:
    print("No imput attempts letf or all passwords entered wrongly ")
    
