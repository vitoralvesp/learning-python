# obs: lists are mutable
'''lunch=['hamburguer','fries','coca cola']
lunch.append('ice cream') #add ice cream to the end (length now is 4)
lunch.insert(0,'anything else') #add anything else in the 0 position without removing hamburguer (length now is 5)
lunch.pop(2) #remove fries
lunch.remove('anything else') #remove anything else
lunch.reverse() # ['ice cream', 'coca cola', 'hamburguer']

alphabet=['b','e','a','c','d']
alphabet.sort() #puts in order (strings, integers, ...)

newlunch=lunch[:] # copy lunch without conect them
newlunch[2]='orange juice' # change newlunch (lunch not affected)

#078
numbers=list()
highernumber=lowernumber=0
for i in range(0,4):
    numbers.append(int(input(f"{i+1}. type a random number: ")))
    if i==0:
        highernumber=lowernumber=numbers[i]
    else:
        if numbers[i]>highernumber:
            highernumber=numbers[i]
        if numbers[i]<lowernumber:
            lowernumber=numbers[i]
print(f'\n> List: {numbers}\n> Higher Number: {highernumber} (INDEX {numbers.index(highernumber)})\n> Lower Number: {lowernumber} (INDEX {numbers.index(lowernumber)})')

#079
numbers=[0]
addmore='Y'
i=0
while True:
    while addmore!='N':
        number=int(input('\n>> type a number: '))
        while number==numbers[i]:
            number=int(input('>> PLEASE DONT REPEAT THE NUMBERS! try again with another number: '))
        numbers.append(number)
        i+=1
        addmore=str(input('>> do you want to continue [y/n]: ')).upper().strip()[0]
    break
numbers.remove(0)
sortedlist=numbers[:]
sortedlist.sort()
print(f'\n-->> List Created: {numbers}\n-->> Sorted List: {sortedlist}')
'''
#080
list=[]
for i in range(0,5):
    number=int(input(f'>> enter the {i+1}º value: '))
    if i==0 or number>list[-1]:
        list.append(number)
    else:
        index=0
        while index<len(list):
            if number<=list[index]:
                list.insert(index,number)
                break
            index+=1
print(f'\n--> List: {list}')