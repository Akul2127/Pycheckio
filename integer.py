user_i = input("Enter something: ")

while True:
    try:
        val = int(user_i)
        print("It is an integer")
        break
    except ValueError:
        print("Not an integer")
        user_i = input("Enter something: ")