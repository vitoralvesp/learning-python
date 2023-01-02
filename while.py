i=1
while i<11:
    print(i)
    i+=1
print('END')

yesorno='y'
while yesorno!='n':
    number=int(input('type a number: '))
    yesorno=str(input('do you want to continue? [y/n] '))
print('END')

#057
gender=str(input('what is your gender [Male/Female]? ')).strip().upper()[0]
while gender not in 'MmFf':
    gender=str(input('\nplease try again with valid options.\nwhat is your gender [Male/Female]? ')).strip().upper()[0]
print('gender {} successfully registered'.format(gender))

#058
import random
computer=random.randint(0,10)
user_bet=int(input('guess a number, from 0 to 10, and type it here: '))
attempts=0
while user_bet!=computer:
    user_bet=int(input('WRONG! try again: '))
    attempts+=1
print('\nRIGHT! the computer chose {}\nattempts: {}!'.format(computer,attempts+1))

#059
number1=float(input('type a number: '))
number2=float(input('type another number: '))
user=0
while user!=5:
    print('<=>'*5+' MENU '+'<=>'*5+'\n\n[1] add\n[2] multiply\n[3] bigger number\n[4] new numbers\n[5] exit\n\n'+'<=>'*10)
    user=int(input('\nChoose one of the options above: '))
    if user==1:
        print('>> {:.0f} + {:.0f} = {:.0f}\n\n'.format(number1,number2,number1+number2))
    elif user==2:
        print('>> {:.0f} x {:.0f} = {:.0f}\n\n'.format(number1,number2,number1*number2))
    elif user==3:
        if number1>number2:
            bigger=number1
        else:
            bigger=number2
        print('>> bigger: {:.0f}'.format(bigger))
    elif user==4:
        number1=float(input('type a number: '))
        number2=float(input('type another number: '))
    elif user==5:
        print('you have chosen to exit, until next time :)')
    elif user<=0 or user>5:
        print('Please try again with valid options...')

#060
n=int(input('enter a number: '))
c=n
f=1
print('{}! = '.format(n),end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x 'if c>1 else' = ',end='')
    f*=c
    c-=1
print(f)

#061
a1=int(input('primeiro termo da PA: '))
r=int(input('razão da PA: '))
i=1
while i<=10:
    print(a1)
    a1+=r
    i+=1

#062
a1=int(input('primeiro termo da PA: '))
r=int(input('razão da PA: '))
i=1
t=0
novotermo=10
print('\nPA: ',end='')
while novotermo!=0:
    t+=novotermo
    while i<=t:
        print('{}, '.format(a1),end='' if i<t else '...')
        a1+=r
        i+=1
    novotermo=int(input('\n\n>> quantos termos a mais vc quer ver? '))

#063
n=int(input('type a number: '))
t1=0
t2=1
i=3
print('{}, {}, '.format(t1,t2),end='')
while i<=n:
    t3=t1+t2
    print('{}, '.format(t3),end='')
    t1=t2
    t2=t3
    i+=1
print('...')

#064
n=0
i=0
total=0
while n!=999:
    n=int(input('type a number [999 to stop]: '))
    total+=n
    i+=1
print('\n\n> total numbers entered: {}\n> sum of all numbers: {}'.format(i-1,total-999))

#065
number=i=add=largernumber=smallernumber=0
condition='Y'
while condition!='N':
    number=int(input('\nenter a number: '))
    i+=1
    add+=number
    average=add/i

    if i==1:
        largernumber=smallernumber=number
    else:
        if number>largernumber:
            largernumber=number
        if number<smallernumber:
            smallernumber=number

    condition=str(input('do you want to continue? (y/n): ')).upper().strip()[0]
print('\n> sum of all numbers: {}\n> average of all numbers: {:.0f}\n> larger number: {}; smaller number: {}'.format(add,average,largernumber,smallernumber))