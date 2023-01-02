for i in range(-1,10):
    i=i+1
    print(i)
print("it's over!")

#046
from time import sleep
print('countdown beginning now!')
for i in range(10,-1,-1):
    print(i)
    sleep(.5)
print('fireworks!!')

#047
for i in range(1,51):
    division=i%2
    if division==0:
        print(i)

#048
add=0
for i in range(0,21):
    division=i%3
    if division==0:
        add+=i
print(add)

#049
multiplication_table=int(input('multiplication table of: '))
for i in range(0,11):
    print('{} x {} = {}'.format(multiplication_table,i,multiplication_table*i))

#050
firstnumber=int(input('first number: '))
secondnumber=int(input('second number: '))
thirdnumber=int(input('third number: '))
fourthnumber=int(input('fourth number: '))
fifthnumber=int(input('fifth number: '))
sixthnumber=int(input('sixth number: '))
numberslist=[firstnumber,secondnumber,thirdnumber,fourthnumber,fifthnumber,sixthnumber]
add=0
for i in numberslist:
    division=i%2
    if division==0:
        add+=i
print(add)

#051
a1=int(input('primeiro termo da PA: '))
r=int(input('razão da PA: '))
n=11
an=a1+(n-1)*r
for i in range(a1,an,r):
    print(i)

#052
number=int(input('type a number: '))
total=0
for i in range(1,number+1):
    if number%i==0:
        print('\033[0;32m',end='')
        total+=1
    else:
        print('\033[31m',end='')
    print('{} '.format(i),end='')
print('\n\033[mthe number {} was divisible {} times.'.format(number,total))
if total==2:
    print('\n> PRIME!')
else:
    print('\n> NOT PRIME!')

#053
phrase=str(input('enter a phrase here: ')).upper()
phrase_length=len(phrase)
revolved_phrase=''
for i in range(1,phrase_length+1):
    revolved_phrase+=phrase[-i]
print('> phrase: {}\n> revolved phrase: {}'.format(phrase,revolved_phrase))
if phrase[0]==revolved_phrase[0]:
    print('\n\n>>> this sentence is a PALINDROME!')
else:
    print('\n\n>>> this sentence is NOT a PALINDROME.')

#054
birthyear_1=int(input('type your year of birth: '))
birthyear_2=int(input('type the birth year of a friend of yours: '))
birthyear_3=int(input('type the birth year of a relative: '))
birthyear_4=int(input('type the birth year of your brother/sister: '))
birthyear_list=[birthyear_1,birthyear_2,birthyear_3,birthyear_4]
for year in birthyear_list:
    actualyear=2022
    year=actualyear-year
    if year>=18:
        print('\n> actual age: {}\n> status: has already reached the age of majority!'.format(year))
    elif year<18:
        print('\n> actual age: {}\n> status: has not yet reached the age of majority.'.format(year))
    else:
        print('\n>> alert: please, type a valid value.')

#055
highestweight=0
lowestweight=0
for i in range(1,6):
    weight=float(input("{}th person's weight: ".format(i)))
    if i==1:
        highestweight=weight
        lowestweight=weight
    else:
        if weight>highestweight:
            highestweight=weight
        if weight<lowestweight:
            lowestweight=weight
print('\n> highest weight: {}Kg\n> lowest weight: {}Kg'.format(highestweight,lowestweight))
#056
add_ages=0
average_age=0
older_person=0
womens=0
for i in range(1,5):
    name=str(input("\n{}th person's name: ".format(i)))
    age=int(input("{}th person's age: ".format(i)))
    gender=str(input("{}th person's gender [m/f]: ".format(i)))
    add_ages+=age
    average_age=add_ages/4

    if i==1 and gender=='m':
        older_person=age
        older_name=name
    elif gender=='m' and age>older_person:
        older_person=age
        older_name=name
    elif gender=='f' and age<=20:
        womens+=1
    
print("> average age of the group: {}\n> group's older man: {}, {}\n> there are {} women under the age of 20".format(average_age,older_name,older_person,womens))
