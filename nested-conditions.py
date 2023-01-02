# CONDIÇÕES ANINHADAS
name=str(input("What is your name? ")).upper()
if name=='VITOR':
    print("What a beatiful name; is the same as mine...")
elif name=='PEDRO' or name=='MARIA' or name=='FELIPE' or name=='ANA':
    print('Your name is very popular in Brazil...')
else:
    print('I like your name...')
print('Have a good day, {}!'.format(name))

#036
house_value=float(input('enter the house value: R$'))
buyer_salary=float(input("enter the buyer's salary: R$"))
years=int(input('how many years you want to pay: '))
lan=house_value/(years*12)
minimum=buyer_salary*30/100
if lan<=minimum:
    print('APPROVED LOAN, CONGRATS!')
else:
    print('LOAN DENIED!\nTRY AGAIN ANOTHER TIME.')
print('> house value: {}\n> buyer salary: {}\n> years: {}'.format(house_value,buyer_salary,years))

#037 INCOMPLETE
number=int(input('type a number: '))
number_converter=int(input('choose an option below to convert the number typed.\n>> for binary, type 1\n>> for octal, type 2\n>> for hexadecimal, type 3\ntype your choice here: '))
if number_converter==1:
    print('converting to binary...')
elif number_converter==2:
    print('converting to octal...')
elif number_converter==3:
    print('converting to hexadecimal...')
else:
    print('YOU SELECTED THE WRONG OPTION! try again with only the requested numbers.')

#038
first_number=int(input('type a number: '))
second_number=int(input('type another number: '))
if first_number>second_number:
    print('>> The first number is larger than the second one.\n>> {} > {}'.format(first_number,second_number))
elif second_number>first_number:
    print('>> The second number is larger than the first one.\n>> {} > {}'.format(second_number,first_number))
else:
    print('>> There are no larger or smaller numbers, both are equal\n>> {} == {}'.format(first_number,second_number))

#039
gender=str(input('What is your gender (Male/Female)? '))
if gender=='Male':
    age=int(input('How old are you? '))
    if age<18:
        remaining_age=18-age
        print('> You are not old enough to enlist.\n> You are {} years away from being considered for enlistment.'.format(remaining_age))
    elif age==18:
        print('> Because of your age, you should enlist later this year.')
    else:
        delayed_age=age-18
        print('> The time to enlist has passed! Please contact the responsible professionals for more information.\n> years of delay: {}'.format(delayed_age))
else:
    print('In Brazil, women do not have to enlist for military service.')

#040
first_grade=float(input('type one of your grades: '))
second_grade=float(input('type another grade: '))
average=(first_grade+second_grade)/2
print('> average: {}'.format(average))
if average>7.0:
    print('> APPROVED!\nYou received an average grade higher than 7.0')
elif average>5.0 and average<6.9:
    print('> Recuperation!\nYour average is between 5.0 and 6.9')
else:
    print('REPROVED! Your average is below 5.0')

#041
athletes_age=int('type your age: ')
if athletes_age<=9:
    print('>> your category: MIRIM')
elif athletes_age<=14:
    print('>> your category: INFANTIL')
elif athletes_age<=19:
    print('>> your category: JUNIOR')
elif athletes_age<=20:
    print('>> your category: SÊNIOR')
else:
    print('>> your category: MASTER')

#042
r1=float(input('type the first segment: '))
r2=float(input('type the second segment: '))
r3=float(input('type the third segment: '))
principal_condicion=r1<r2+r3 and r2<r1+r3 and r3<r1+r2
if principal_condicion and r1==r2==r3:
    print('> Based on the submitted data, it is possible to form a perfect triangle.\n> triangle type: Equilateral')
elif principal_condicion and r1-r2==0 or r1-r3==0 or r2-r3==0:
    print('> Based on the submitted data, it is possible to form a perfect triangle.\n> triangle type: Isósceles')
elif principal_condicion and r1!=r2!=r3:
    print('> Based on the submitted data, it is possible to form a perfect triangle.\n> triangle type: Escaleno')
else:
    print('it is not possible to form a perfect triangle.')

#043
height=float(input('enter your heigth here: '))
weight=float(input('enter your weight here: '))
imc=weight/(height*height)
print('> Your IMC: {:.1f}'.format(imc))
if imc<18.5:
    print('> status: underweight')
elif imc>18.5 and imc<25:
    print('> status: ideal weight')
elif imc>25 and imc<30:
    print('> status: overweight')
elif imc>30 and imc<40:
    print('> status: obesity')
elif imc>40:
    print('status: major obesity')
elif imc<=0:
    print('enter a valid value.')
else:
    print('enter a valid value.')

#044
price=float(input('> price to be paid: R$'))
if price!=0:
    payment=float(input('> payment method\n1 - cash/check payment\n2 - cash on card\n3 - up to 2x on credit card\n4 - 3x or more\n>> type an option here: '))
    if payment!=0 and payment<5:
        if payment==1:
            print('>'*10+' you choose CASH/CHECK PAYMENT '+'<'*10)
            discount=price*(10/100)
            new_price=price-discount
            print('> CONGRATULATIONS, YOU HAVE JUST RECEIVED A 10% DISCOUNT!\n> You will pay now: R${:.2f}'.format(new_price))
        elif payment==2:
            print('>'*10+' you choose CASH ON CARD '+'<'*10)
            discount=price*(5/100)
            new_price=price-discount
            print('> CONGRATULATIONS, YOU HAVE JUST RECEIVED A 5% DISCOUNT!\n> You will pay now: R${:.2f}'.format(new_price))
        elif payment==3:
            print('>'*10+' you choose UP TO 2X ON CREDIT CARD '+'<'*10)
            print('You will pay: R${:.2f}'.format(price))
        elif payment==4:
            print('>'*10+' you choose 3X OR MORE ON CREDIT CARD '+'<'*10)
            interest=120/100
            new_price=price*interest
            print('You will pay: R${:.2f}'.format(new_price))
    else:
        print('try a valid option...')
else:
    print('if you dont owe anything, you dont have to pay anything =)')

#045
import random
print('<=>'*5+'JOKENPÔ GAME'+'<=>'*5)
user_play=int(input('to play against the computer, choose an option from 0 to 2 and wait for the result!\n[ 0 ] stone\n[ 1 ] paper\n[ 2 ] scissors\ninput your choise here: '))
if user_play>=0 or user_play<3:
    computer_play=random.randint(0,2)
    if computer_play==0 or computer_play<3:
        if user_play==computer_play:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>>Your choise: {}\n>> Computer choise: {}\nTIE! Both of you chose the same option!'.format(user_play,computer_play))
        
        # user_play chooses always 0
        elif user_play==0 and computer_play==1:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 0 ] stone\n>> Computer choise: [ 1 ] paper\nPOINT FOR THE COMPUTER! the paper wraps the stone')
        elif user_play==0 and computer_play==2:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 0 ] stone\n>> Computer choise: [ 2 ] scissors\nPOINT FOR YOU! the rock breaks the scissors')

        # user_play chooses always 1
        elif user_play==1 and computer_play==0:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 1 ] paper\n>> Computer choise: [ 0 ] stone\nPOINT FOR YOU! the paper wraps the stone')
        elif user_play==1 and computer_play==2:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 1 ] paper\n>> Computer choise: [ 2 ] scissors\nPOINT FOR THE COMPUTER! the scissors cut paper')

        # user_play chooses always 2
        elif user_play==2 and computer_play==0:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 2 ] scissors\n>> Computer choise: [ 0 ] stone\nPOINT FOR THE COMPUTER! the rock breaks the scissors')
        elif user_play==2 and computer_play==1:
            print('[ 0 ] stone  [ 1 ] paper  [ 2 ] scissors')
            print('>> Your choise: [ 2 ] scissors\n>> Computer choise: [ 1 ] paper\nPOINT FOR THE COMPUTER! the scissors cut paper')
    else:
        print('!!! TO DEVS ONLY: CHECK THE COMPUTER CODE!!!\n> Computer choice: {}'.format(computer_play))
else:
    print('Please, try again with valid options.')
