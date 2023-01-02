#066
number=add=0
while True:
    number=int(input('type a number (999 to stop): '))
    if number==999:
        break
    add+=number
print(f'\nThe sum between all the numbers typed are {add}')

#067
while True:
    number=int(input('What value do you want to see the multiplication table for?\nA: '))
    if number<0:
        break
    print('-'*30)
    for i in range(1,11):
        print(f'{number} x {i} = {number*i}')
    print('-'*30)
print('program ending...')

#068
import random
i=0
print('=-'*10+'\nJOGO DO PAR OU ÍMPAR\n'+'=-'*10)
while True:
    computernumber=random.randint(0,11)
    number=int(input('\n1. Diga um valor: '))
    total=number+computernumber
    userchoise=' '
    while userchoise not in 'PI':
        userchoise=str(input('2. Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'\n>> VOCÊ jogou {number} e o COMPUTADOR {computernumber}, total de {total}.')
    if total%2==0 and userchoise=='P' or total%2>0 and userchoise=='I':
        i+=1
        print('>> VOCÊ VENCEU, vamos jogar novamente...\n')
    else:
        if total%2>0 or total%2<0 and userchoise=='P':
            print(f'>> VOCÊ PERDEU =)\n>> partidas ganhas: {i}\n')
            break

#069
olderthan18=men=womenyoungerthan20=0
while True:
    age=int(input('\n1. enter a age: '))
    gender=addmore=' '
    while gender not in 'MF':
        gender=str(input('2. enter a gender [M/F]: ')).upper().strip()[0]
    #functionalities
    if age>18:
        olderthan18+=1
    if gender=='M':
        men+=1
    if gender=='F' and age<20:
        womenyoungerthan20+=1
    
    while addmore not in 'YN':
        addmore=str(input('3. do you want add more [Y/N]? ')).upper().strip()[0]
    if addmore=='N':
        break
print(f'\n>> people older than 18: {olderthan18}\n>> men: {men}\n>> women younger than 20: {womenyoungerthan20}')

#070
productname=cheapestproductname=' '
total=higherthan1000=cheapestproduct=items=0
while True:
    productname=str(input('\n> Product Name: '))
    productvalue=float(input('> Product Value (R$): '))
    items+=1
    total+=productvalue
    if items==1 or productvalue<cheapestproduct:
        cheapestproduct=productvalue
        cheapestproductname=productname
    if productvalue>1000:
        higherthan1000+=1
    addmore=' '
    while addmore not in 'YN':
        addmore=str(input('> do you want to add more [Y/N]? ')).upper().strip()[0]
    if addmore=='N':
        break
print(f'\n=> total: R${total:.2f}\n=> products higher than one thousand: {higherthan1000}\n=> cheapest product: {cheapestproductname}, {cheapestproduct:.2f}')

#071
valor=int(input('\n=> informe o valor a ser sacado: R$'))
total=valor
cedula=50
totaldecedulas=0
while True:
    if total>=cedula:
        total-=cedula
        totaldecedulas+=1
    else:
        if totaldecedulas>0:
            print(f'   Total de {totaldecedulas} cédulas de R${cedula}')
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        totaldecedulas=0
        if total==0:
            break
        


