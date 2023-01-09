# obs: lists are mutable
lunch=['hamburguer','fries','coca cola']
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

    