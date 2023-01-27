'''help()
help(print)
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
        i: início
        f: fim
        p: passo
        return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c} ',end='')
        c+=p
    print('FIM!')
help(contador)

def somar(a=0,b=0,c=0):
    print(a+b+c)
somar(3,2,1) # 6
somar(3,2) # 5
somar(3) # 3
somar() # 0

def somar(a=0,b=0,c=0):
    return a+b+c
soma=somar(1,2,3)
print(soma) # 6
'''
#101
def voto(an):
    from datetime import date
    anoatual=date.today().year
    idade=anoatual-an
    if idade>=18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif 15<idade<18 or idade>70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO NEGADO!'
an=int(input('insira o seu ano de nascimento: '))
print(voto(an))
