phrase='Hello, World!'
phrase_2='      Hello     , World  !        '

phrase[4] # prints o
phrase[3:5] # prints lo
phrase[1:3:5] # prints e
phrase[:5] # prints Hello
phrase[4:] # prints o, World!
phrase[1::3] # prints eoWl

len(phrase) # prints 13
phrase.count('l') # prints 3
phrase.count('o',0,5) # prints 1
phrase.find('l') # prints 2
phrase.find('Olá, Mundo!') # prints -1
'World'in phrase # prints True

phrase.replace('World','Python') # prints Hello, Python!
phrase.upper() # prints HELLO, WORLD!
phrase.lower() # prints hello, world!
phrase.capitalize() # prints Hello, world!
phrase.title() # prints Hello, World!
phrase_2.strip() # prints Hello     , World  !
phrase_2.rstrip() # prints       Hello     , World  !
phrase_2.lstrip() # prints Hello     , World  ! 

phrase.split() # prints ['Hello,', 'World!']
'-'.join(phrase) # prints H-e-l-l-o-,- -W-o-r-l-d-!

#022
name=input('whats ur nm? ')
split_name=name.split()
print('> fullname: {}\n> uppercase name: {}\n> first name length: {}\n'.format(name,name.upper(),len(split_name[0])))

#023
number=int(input('number: '))
u=number//1%10
d=number//10%10
c=number//100%10
m=number//1000%10
print('> unidade: {}\n> dezena: {}\n> centena: {}\n> milhar: {}'.format(u,d,c,m))

#024
city_name=str(input('type the name of the city: ')).upper()
print("city's name: {}\nThe city's name begins with 'SANTO'? {}".format(city_name,'SANTO' in city_name))

#025
name_2=str(input('type the name: ')).upper()
print("name: {}\nThe name contains 'SILVA'? {}".format(name_2,'SILVA' in name_2))

#026
phrase_2=input('type a phrase: ')
print('> phrase: {}\n> How many times the "a" shows up? {}\nWhich position the first "a" shows? {}\nWhich position the last "a" shows? {}'.format(phrase_2,phrase_2.count('a'),phrase_2.find('a'),phrase_2.rfind('a')))

#027
name_3=str(input('type a name: ')).title()
split_name=name_3.split()
print('> full name: {}\n> first name: {}\n> last name: {}'.format(name_3,split_name[0],split_name[-1]))
