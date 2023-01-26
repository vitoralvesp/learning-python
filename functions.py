'''def sayMyName():
    print('HEISENBERG!')
sayMyName() # HEISENBERG!

def worldsSecondBestLawyer(saulgoodman):
    print(f'IF YOU HAVE TROUBLE WITH THE JUSTICE,\nBETTER CAUL {saulgoodman}')
worldsSecondBestLawyer('SAUL') # IF YOU HAVE TROUBLE WITH THE JUSTICE, BETTER CAUL SAUL

def addNumbers(*num):
    # print(num) tuple
    total=0
    for number in num:
        total+=number
    print(total)
addNumbers(1,2,3,4,5) #15  
addNumbers(1,8) #9

#096
def area(largura,comprimento):
    area=largura*comprimento
    print('-'*40)
    print(f'A área de um terreno {largura}x{comprimento} é de {area}.')
largura=float(input('Largura (m): '))
comprimento=float(input('Comprimento (m): '))
area(largura,comprimento)

#097
def escreva(texto):
    print('~'*40)
    print(f'{texto:^40}')
    print('~'*40)
texto=str(input('> Insira sua mensagem aqui: '))
escreva(texto)

#098
from time import sleep
def contador(inicio,fim,passo):
    if passo<0:
        passo*=-1
    if passo==0:
        passo=1
    print('-'*40)
    print(f'Contagem de {inicio} à {fim} de {passo} em {passo}:')
    if inicio<fim:
        i=inicio
        while i<fim+1:
            print(f'{i} ',end='',flush=True)
            sleep(.5)
            i+=passo
        print('FIM!')
    else:
        i=inicio
        while i>=fim:
            print(f'{i} ',end='',flush=True)
            sleep(.5)
            i-=passo
        print('FIM!')

contador(1,10,1)
contador(10,0,2)

print('-'*40)
print(f'Agora é a sua vez de personalizar a contagem!')
inicio=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contador(inicio,fim,passo)
'''
#099
def maior(*num):
    maior=0
    for i in num:
        if i>maior:
            maior=i
    print('-='*20)
    print(f'O maior número inserido foi {maior}.')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()










