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
'''
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



