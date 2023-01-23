#084
'''peopleslist=list()
lighter=list()
heavier=list()
addmore='Y'
while True:
    copydata=list()
    while addmore!='N':
        copydata.append(str(input(f'\n> add a name: ')))
        copydata.append(float(input(f'> add a weight: ')))
        peopleslist.append(copydata[:])
        copydata.clear()
        addmore=str(input('>> do you want to add more people [y/n]: ')).upper().strip()[0]
    i=0
    for people in peopleslist:
        if len(peopleslist)==0:
            heavier.append(people[0])
            lighter.append(people[0])
        else:
            if people[1]>=80:
                heavier.append(people[0])
                heavier.append(people[1])
            if people[1]<80:
                lighter.append(people[0])
                lighter.append(people[1])
    break
print('='*30)
print(f'\n>> Peoples List: {peopleslist}\n>> People Registered: {len(peopleslist)}\n>> Most HEAVIER People: {heavier}\n>> Most LIGHTER People: {lighter}')

#085
numbers=list()
copynumbers=list()
even=list()
odd=list()
for i in range(0,7):
    copynumbers.append(int(input(f'> {i+1}. enter a number: ')))
    for number in copynumbers:
        if number%2==0:
            even.append(number)
        else:
            odd.append(number)
    copynumbers.clear()
even.sort()
odd.sort()
numbers.append(even)
numbers.append(odd)
print(f'\n--> the even numbers entered were: {numbers[0]}\n--> the odd numbers entered were: {numbers[1]}')

#086
matrix=[[0,0,0],[0,0,0],[0,0,0]]
for line in range(0,3):
    for column in range(0,3):
        matrix[line][column]=int(input(f'>> enter a value for [{line},{column}]: '))
print('\n')
for line in range(0,3):
    for column in range(0,3):
        print(f'[{matrix[line][column]:^5}]',end='')
    print()
'''
#087
matrix=[[0,0,0],[0,0,0],[0,0,0]]
addevens=largest=addcolumns=0
for line in range(0,3):
    for column in range(0,3):
        matrix[line][column]=int(input(f'>> enter a value for [{line},{column}]: '))
print('\n')
for line in range(0,3):
    addcolumns+=matrix[line][2]
    for column in range(0,3):
        print(f'[{matrix[line][column]:^5}]',end='')
        if matrix[line][column]%2==0:
            addevens+=matrix[line][column]
        if column==0 or matrix[1][column]>largest:
            largest=matrix[1][column]
    print()

print(f'\n-->> the sum of all even values entered: {addevens}\n-->> sum of all numbers in the third column: {addcolumns}\n-->> The largest value in the second line: {largest}')