people={'name':'Vitor','gender':'male','age':19}
print(people['name']) # Vitor
print(people.keys()) # dict_keys(['name', 'gender', 'age'])
print(people.values()) # dict_values(['Vitor', 'male', 19])
print(people.items()) # dict_items([('name', 'Vitor'), ('gender', 'male'), ('age', 19)])

for keys,values in people.items():
    print(keys,values) 
    # name Vitor
    # gender male
    # age 19

people['haircolor']='black'
print(people['haircolor']) # black

brasil=list()
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil) # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]

estado=dict()
brasil=list()
for i in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

#090
student={}
student['name']=str(input('Name: ')).capitalize()
student['averagescore']=float(input(f"{student['name']}'s Average Score: "))
if student['averagescore']>=7:
    student['situation']='Approved'
elif 5<=student['averagescore']<7:
    student['situation']='Recovery'
else:
    student['situation']='Reproved'
for key,value in student.items():
    print(f'{key} = {value}')

#091
from random import randint
list=[]
for i in range(0,4):
    dictionary={'player':i,'valuedrawn':randint(0,6)}
    list.append(dictionary.copy())
print('-'*34)
for i in range(0,len(list)):
    print(f"The value drawn for player{list[i]['player']} was {list[i]['valuedrawn']}")
print('-'*34)
sortedlist=[]
for i in range(0,len(list)):
    sortedlist.append(list[i]['valuedrawn'])
sortedlist.sort(reverse=True)
for i in range(0,len(list)):
    print(f"{i+1}º place: player{list[i]['player']} with {sortedlist[i]}")
print('-'*34)

#092
dictionary=dict()
dictionary['nome']=str(input('Nome: '))
dictionary['nascimento']=int(input('Ano de Nascimento: '))
dictionary['carteiradetrabalho']=int(input('Carteira de Trabalho (0 não tem): '))
if dictionary['carteiradetrabalho']==0:
    print('-'*34)
    for keys,values in dictionary.items():
        print(f'{keys} = {values}')
    print('-'*34)
else:
    dictionary['anodecontratação']=int(input('Ano de Contratação: '))
    dictionary['salário']=float(input('Salário: R$'))
    print('-'*34)
    for keys,values in dictionary.items():
        print(f'{keys} = {values}')
    print('-'*34)

#093
jogador={}
jogador['nome']=str(input('Nome do Jogador: '))
partidas=int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols=[]
total=0
for i in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
for gol in gols:
    if gol!=0:
        total+=gol
jogador['gols']=gols.copy()
jogador['total']=total
print('-'*33)
print(f'{jogador}')
print('-'*33)

#094
list=list()
while True:
    dictionary={'name':str(input('> name: ')),'age':int(input('> age: ')),'gender':str(input('> gender: '))}
    list.append(dictionary)
    print('-'*33)
    addmore=str(input('> do you want to add more [y/n]? ')).upper().strip()[0]
    print('-'*33)
    if addmore=='N':
        break
peoplestotal=0
averageage=agetotal=0
women=[]
womentotal=0
middleaged=[]
for i in range(0,len(list)):
    if list[i]['name']:
        peoplestotal+=1
    if list[i]['age']:
        agetotal+=list[i]['age']
    if list[i]['gender']=='F':
        women.append(list[i]['name'])
        womentotal+=1
    if list[i]['age']>50:
        middleaged.append(list[i]['name'])
        middleaged.append(list[i]['age'])
averageage=agetotal/peoplestotal
print(f"\nPeople Registered: {peoplestotal}\nPeople's Average Age: {round(averageage)}\nWomen: {women} | Total: {womentotal}\nMiddle-Aged Persons: {middleaged}")
#095
jogadores={}
jogador=[]
while True:
    jogadores.clear()
    jogadores['nome']=str(input('\nNome do Jogador: '))
    partidas=int(input(f"Quantas partidas {jogadores['nome']} jogou? "))
    gols=[]
    total=0
    for i in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    for gol in gols:
        if gol!=0:
            total+=gol
    jogadores['gols']=gols.copy()
    jogadores['totaldegols']=total
    jogador.append(jogadores.copy())
    addmore=str(input('Você quer adicionar mais um jogador [s/n]? ')).upper().strip()[0]
    print('-'*33)
    if addmore=='N':
        break
print(f'{jogador}')



