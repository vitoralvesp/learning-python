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
'''
#096
def area(largura,comprimento):
    area=largura*comprimento
    print('-'*40)
    print(f'A área de um terreno {largura}x{comprimento} é de {area}.')
largura=float(input('Largura (m): '))
comprimento=float(input('Comprimento (m): '))
area(largura,comprimento)






