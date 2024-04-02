import random as rand

l=['rock','paper','scissor']
comp=rand.choice(l)
cp=0
up=0
while True:
    user = input('Rock, Paper, Scissor. \n enter your choice : ')
    if comp == user:
        print('Opponents Choice : ', comp)
        print('Match Tie.')
        cp+=1
        up+=1
    elif comp == 'rock' and user == 'paper':
        print('Opponents Choice : ', comp)
        print('You Won')
        up += 1
    elif comp == 'rock' and user == 'scissor':
        print('Opponents Choice : ', comp)
        print('Opponent Won')
        cp += 1
    elif comp == 'scissor' and user == 'paper':
        print('Opponents Choice : ', comp)
        print('Opponent Won')
        cp += 1
    elif comp == 'scissor' and user == 'rock':
        print('Opponents Choice : ', comp)
        print('You Won')
        up += 1
    elif comp == 'paper' and user == 'scissor':
        print('Opponents Choice : ', comp)
        print('You Won')
        up += 1
    elif comp == 'paper' and user == 'rock':
        print('Opponents Choice : ', comp)
        print('Opponent Won')
        cp += 1
    else:
        print('Choose again.May be you enter wrong input.')
    print('If you want to continue playing enter 1 \nIf you want to quit Game enter 0')
    ch=int(input('What do you want? '))
    if ch==1:
        continue
    else:
        break
print('Opponent points is : ',cp)
print('User points is : ',up)
if cp>up:
    print('Opponent Won')
elif cp<up:
    print('User Won')
else:
    print('Match Draw')