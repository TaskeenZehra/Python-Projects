import random as ran
while True:
    comp = ran.randint(1, 100)
    user = int(input('Enter Your Number From 1-100 : '))
    print("Computer Selected Number : ", comp)
    if user > comp:
        print('Your guess number is too high.')
    elif user < comp:
        print('Your guess number is too low.')
    else:
        print('Your guess number is equal to computer.')
    s=int(print("If you want to exit application enter 0 either 1"))
    if s == 0:
        exit()