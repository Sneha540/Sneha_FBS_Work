correct_userid = "admin"
correct_password = "12345"
userid = input("Enter User ID: ")
password = input("Enter Password: ")
if userid == correct_userid and password == correct_password:
    print("\nLogin Successful!")
else:
    print("\nInvalid User ID or Password")
