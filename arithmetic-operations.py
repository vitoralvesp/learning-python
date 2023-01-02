'''
ORDEM DE PRECEDÊNCIA
1. parênteses
2. potências
3. multiplicação, divisão, divisão inteira e resto
4. adição e subtração
'''

a=5+3*2 #11
b=3*5+4**2 #31
c=3*(5+4)**2 #243
print(a,b,c)

d=pow(2,2) # 2**2
e=81**(1/2)
print(d,e)

f='hello'*5 #'hellohellohellohellohello'


#005
number=int(input('type a number: '))
print('The number before is: {}\nThe number after is: {}'.format(number-1,number+1))

#006
number_2=int(input('type a number: '))
print('>>> The double of {} is: {}\n>>> The triple of {} is: {}\n>>>The square root of {} is: {}.'.format(number_2,number_2*2,number_2,number_2*3,number_2,number_2**(1/2)))

#007
number_3=float(input('type the first one: '))
number_4=float(input('type the second one: '))
averageScore=(number_3+number_4)/2
print('your average score is: {}'.format(averageScore))

#008
meters=int(input('type a number: '))
centimeters=meters*100
millimeters=meters*1000
print('this value of meters corresponds to {} centimeters and {} millimetters.'.format(centimeters, millimeters))

#009
number_5=int(input('type a number: '))
n1=number_5*1
n2=number_5*2
n3=number_5*3
n4=number_5*4
n5=number_5*5
print('the multiplication table of {} until 5 is:\n{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}'.format(number_5,number_5,n1,number_5,n2,number_5,n3,number_5,n4,number_5,n5))

#010
real=float(input('enter the value you have: '))
dollar_converter=real/3.27
print('your money converted to dollar is ${}'.format(dollar_converter))

#011
room_width=float(input('type the room width: '))
room_height=float(input('type the room height: '))
room_area=room_width*room_height
paint=room_area/2
print('the amount of paint required for this room ({}m2) will be: {}L'.format(room_area,paint))

#012
price=float(input('type the price: '))
discount=price*5/100
print('new price: {}'.format(discount))

#013
salary=float(input('type the salary: '))
salary_increase=salary*15/100
print('new salary: {}'.format(salary_increase))