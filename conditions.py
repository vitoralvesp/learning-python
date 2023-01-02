name=str(input('type ur name: ')).upper()
print("we've the same name! that's so nice!"if name=='VITOR'else"u have a pretty name...")

name_2=str(input('type ur name: ')).upper()
if name_2=='HENRIQUE':
    print('u have the same name as my brother...')
print('im happy to meet u, {}'.format(name_2))

#028
import random
number=random.randint(0,5)
user_bet=int(input('guess a number, from 0 to 5, and type it here: '))
print('CORRECT! you and the computer choose the same number!'if user_bet==number else'WRONG! the computer chose {} and you {}.'.format(number,user_bet))

#029
speed=float(input("what's ur speed right now? "))
print("YOU GOT FINED! ur speed is too high!"if speed>=80 else"CONGRATS, ur speed is good!\ncontinue being an excellent driver.")

#030
number_2=int(input('type a number: '))
print('PAIR'if number_2%2==0 else'ODD')

#031
km_distance=float(input('type the distance here: '))
short_distance_price=0.50*km_distance
long_distance_price=0.45*km_distance
print('> distance typed: {}\n> price: R$ {}'.format(km_distance,short_distance_price)if km_distance<=200 else'> distance typed: {}\n> price: R$ {}'.format(km_distance,long_distance_price))

#032
year=int(input('Hey, i came from future.\nWhich year is it? '))
is_leap=(year%4==0 and year%100!=0) or (year%400==0)
print('> actual year: {}\nwow this year is leap'.format(year,is_leap)if is_leap else'> actual year: {}\nthis year definitely is not leap'.format(year,is_leap))

#033
a=int(input('type a number: '))
b=int(input('type a number: '))
c=int(input('type a number: '))
smaller=a
if b<a and b<c:
    smaller=b
if c<a and c<b:
    smaller=c
largest=a
if b>a and b>c:
    largest=b
if c>a and c>b:
    largest=c
print('{} > {}'.format(largest, smaller))

#034
salary=float(input('type your salary: R$'))
raise_10=salary+(salary*0.1)
raise_15=salary+(salary*0.15)
print('you have just received a raise of 10%\nYour salary now is: R$ {}'.format(raise_10)if salary>1250 else 'you have just received a raise of 10%\nYour salary now is: R$ {}'.format())

#035
r1=float(input('type the first segment: '))
r2=float(input('type the second segment: '))
r3=float(input('type the third segment: '))
print('Based on the submitted data, it is possible to form a perfect triangle.'if r1<r2+r3 and r2<r1+r3 and r3<r1+r2 else'it is not possible to form a perfect triangle.')
