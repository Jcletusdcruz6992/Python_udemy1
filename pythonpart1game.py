from random import randint, randrange
global x
x=str(randint(100, 999))     # randint is inclusive at both ends
print(x)
def game(x):
    print('x={}'.format(x))
    num=str(input('Enter a three digit number'))
    if(num==x):
        return("Code Matched and you won")
    else:
        if(num[0]==x[0] or num[1]==x[1] or num[2]==x[2]):
            print('there is a match,try again!')
            return game(x)
        else:
            print('None matches!,try again')
            return game(x)
y=game(x)
print(y)
randrange(100, 1000)  # randrange is exclusive at the stop
