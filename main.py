rounds = input('enter the number of range')
counter = 0

while rounds.isdigit() != True:
    print('please enter an integer')
    rounds = input('enter the number of range')

for i in range(int(rounds)):
    print(i)
    counter +=1

    if counter == int(rounds):
        print('Done!')
    else:
        continue