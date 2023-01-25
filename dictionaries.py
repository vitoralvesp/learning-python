'''
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
array=[]
for i in range(0,4):
    dictionary={'player':i,'valuedrawn':randint(0,6)}
    array.append(dictionary.copy())
print('-'*34)
for i in range(0,len(array)):
    print(f"The value drawn for player{array[i]['player']} was {array[i]['valuedrawn']}")
print('-'*34)
sortedarray=[]
for i in range(0,len(array)):
    sortedarray.append(array[i]['valuedrawn'])
sortedarray.sort(reverse=True)
for i in range(0,len(array)):
    print(f"{i+1}º place: player{array[i]['player']} with {sortedarray[i]}")
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
'''
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





