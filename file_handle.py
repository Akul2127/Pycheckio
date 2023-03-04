import os

path = "C:\\Users\\Akul\\Documents\\Coding\\game_tips.txt"

if os.path.exists(path):
    print("Location exists")
else:
    print("Sorry could not find it. \nCheck to see the file location again "
          "or make sure that \nyou spelled correctly")
