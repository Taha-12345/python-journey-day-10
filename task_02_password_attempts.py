password = "python123"

for attempt in range(3):
    user = input("Enter password: ")

    if user == password:
        print("Access Granted")
        break
else:
    print("Account Locked")