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

#081
list=[]
while True:
    list.append(int(input('\n> type a number: ')))
    addmore=str(input('> do you want to add more [y/n]: ')).upper().strip()[0]
    if addmore=='N':
        break
sortedlist=list[:]
descendinglist=list[:]
sortedlist.sort()
descendinglist.sort(reverse=True)
print(f'\n--> List: {list}\n--> Sorted List: {sortedlist}\n--> Descending List: {descendinglist}\n--> Number of elements inserted: {len(list)}')
if 5 in list:
    i=0
    for number in list:
        if number==5:
            i+=1
    print(f'--> 5: True, {i} occurences')
else:
    print('--> 5 is not in the list')

#082
list=[]
pairnumberslist=[]
evennumberslist=[]
while True:
    addmore='Y'
    i=0
    while addmore!='N':
        i+=1
        list.append(int(input(f'\n> {i}. type a number: ')))
        addmore=str(input('> do you want to add more [y/n]: ')).upper().strip()[0]
    print('\n')
    print(f'='*20)
    for i in list:
        if i%2==0:
            pairnumberslist.append(i)
            print(f'{i} == PAIR!')
        else:
            evennumberslist.append(i)
            print(f'{i} == EVEN')
    print(f'='*20)
    print('\n')
    break
print(f'\n--> Full List: {list}\n--> List with PAIRS numbers only: {pairnumberslist}\n--> List with EVEN numbers only: {evennumberslist}')
'''
#083
sentence=str(input('>> enter a sentence: '))
print(f'>> Your sentence is correct! {sentence}' if sentence[0]=='(' and sentence[-1]==')' else f'>> Your sentence is incorrect! Please, try again...')