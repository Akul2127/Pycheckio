print("Welcome to Akul's secret  secret Trivia")

ans = input("Are you ready (yes/no): ")
score = 0
t_q = 4

if ans.lower() == 'yes':
    ans = input(' 1. What is Akul most top secret websites?')
    if ans.lower() == 'ev.io, 1v1.lol, sites.google.com/thegamecomplication/, crazygames unblocked':
        score +=1
        print("correct")
    else:
        print("incorrect")

    ans = input("What age did I(Akul) write this on")
    if ans == '10':
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input("What is Akul's favoite hobby?")
    if ans == 'Business, Coding':
        score += 1
        print("correct")
    else:
        print("incorrect")

    print(score)