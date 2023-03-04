user_input = input("Enter something:")

try:
    val = int(user_input)
    print("It is not a string")
except ValueError:
    print(" It is a string")