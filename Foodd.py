import random
b = ['upma', 'dosa', 'rice']
already_c = []
time = 0
timea = 0
timeb = 0
timec = 0
time1 = 0
time2= 0

a = random.randint(0,2)
if a == 0:
    print('breakfast is upma')
    time = time+1
    timea = timea + 1
    if time == 1:
        b.pop(0)
        already_c.insert(0,'upma')
    if time == 3:
        already_c.pop(0)
        b.insert(0,'upma')
    if timea == 1:
        a = random.randint(1, 2)
elif a == 1:
    print('breakfast is dosa')
    time1 = time1 + 1
    timeb = timeb+1
    if time1 == 1:
        already_c.insert(1, 'dosa')
        b.pop(1)
    if timeb == 1:
        a = random.randint(0,2)
elif a == 2:
    print('breakfast is rice')
    time2 = time2 + 1
    timec = timec + 1
    if time == 1:
        b.pop(2)
        already_c.insert(2,'rice')
    if timec == 1:
        a = random.randint(0,1)