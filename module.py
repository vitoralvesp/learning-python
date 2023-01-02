# import (import math)
# from import (from math import sqrt)
import math,random
num=int(input('type a number: '))
sqrt_num=math.sqrt(num)
print('{:.2f}'.format(sqrt_num))

random_number=random.randint(1,10)
print(random_number)

#016
number_1=float(input('type a float number: '))
integer_part=math.trunc(number_1)
print('the interger part of this number is {}'.format(integer_part))

#017
opposite_catheter=float(input('opposite catheter: '))
adjacent_cathet=float(input('adjacent cathet: '))
hypotenuse=math.hypot(opposite_catheter,adjacent_cathet)
print('h={:.2f}'.format(hypotenuse))

#018
angle=float(input('type an angle number: '))
sen=math.sin(math.radians(angle))
cos=math.cos(math.radians(angle))
tan=math.tan(math.radians(angle))
print('angle: {}\nsen: {}\ncos: {}\ntan: {}'.format(angle,sen,cos,tan))

#019
student_1=input('enter the name of your first student: ')
student_2=input('enter the name of your second student: ')
student_3=input('enter the name of your third student: ')
student_4=input('enter the name of your fourth student: ')
students_list=[student_1, student_2, student_3, student_4]
chosen_student=random.choice(students_list)
print('the chosen student was: {}'.format(chosen_student))

#020
student_1=input('enter the name of your first student: ')
student_2=input('enter the name of your second student: ')
student_3=input('enter the name of your third student: ')
student_4=input('enter the name of your fourth student: ')
students_list=[student_1, student_2, student_3, student_4]
random.shuffle(students_list)
print('the order of the students is {}'.format(students_list))
