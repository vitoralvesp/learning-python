# obs: tuples are immutable
# structure:
lunch=('hamburguer','juice','pizza','pudim')

'''#072
tuple=('one','two','three','four','five','six','seven','eight','nine','ten')
user=int(input('type a number between 0 and 10: '))
i=0
while True:
    while user<0 or user>10:
        user=int(input('PLEASE, TRY AGAIN! type a number between 0 and 10: '))
    print('\n-- You have typed zero...' if user==0 else f'-- You have typed {tuple[user-1]}...')
    break

#073
futeboltuple=('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Atlético Paranaense','Atlético Mineiro','Fortaleza','São Paulo','América Fc Saf','Chapecoense')
firstplaced=futeboltuple[0:5]
lastplaced=futeboltuple[-4:]
alphabeticalorder=sorted(futeboltuple)
chapecoense=futeboltuple.index('Chapecoense')
print(f'-- First Placed: {firstplaced}\n-- Last Placed: {lastplaced}\n-- Alphabetical Order: {alphabeticalorder}\n-- Chapecoense Position: {chapecoense+1}')

#074
from random import randint
finaltuple=()
for i in range(0,5):
    randomnumber=randint(0,5)
    tuple=(randomnumber,)
    finaltuple+=tuple
print(f'\n-- finaltuple: {finaltuple}\n-- biggestvalue and lowestvalue: {max(finaltuple)}, {min(finaltuple)}')

#075
finaltuple=evennumbers=()
print('\n')
for i in range(0,4):
    number=int(input('type a number: '))
    tuple=(number,)
    finaltuple+=tuple
    if number%2==0:
        evennumbers+=tuple
print(f'\n-- finaltuple: {finaltuple}')
print(f'\n-- how many times does 9 appear: {finaltuple.count(9)}')
print(f'\n-- index of the first 3 entered: {finaltuple.index(3)}' if 3 in finaltuple else '\n-- number 3 was not entered')
print(f'\n-- even numbers: {evennumbers}')
'''
#076
productstuple=()
addmore='Y'
i=0
while True:
    while addmore!='N':
        productname=str(input("\n1. enter the product's name: ")).upper()
        while productname=='':
            print('\n**TRY AGAIN WITH A VALID OPTION**')
            productname=str(input("1. enter the product's name: ")).upper()
        productvalue=float(input("2. enter the product's value: R$"))
        addmore=str(input('3. do you want to add more [Y/N]: ')).upper().strip()[0]
        tuple=(productname,productvalue,)
        productstuple+=tuple
    print('\n\n')
    print('-'*40)
    print(f'{"PRODUCTS LIST":^40}')
    print('-'*40)
    for i in range(0,len(productstuple)):
        stringvalue=type(productstuple[i])==str
        floatvalue=type(productstuple[i])==float
        if stringvalue:
            print(f'{productstuple[i]:.<30}',end='')
        else:
            if floatvalue:
                print(f'R${productstuple[i]:>7.2f}')
    print('-'*40)
    break