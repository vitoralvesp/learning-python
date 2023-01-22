#084
peopleslist=list()
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
print(f'\n>> Peoples List: {peopleslist}\n>> People Registered: {len(peopleslist)}\n>> Most HEAVIER People: {heavier}\n>> Most LIGHTER People: {lighter}')