# obs: tuples are immutable
# structure:
lunch=('hamburguer','juice','pizza','pudim')

#072
tuple=('one','two','three','four','five','six','seven','eight','nine','ten')
user=int(input('type a number between 0 and 10: '))
i=0
while True:
    while user<0 or user>10:
        user=int(input('PLEASE, TRY AGAIN! type a number between 0 and 10: '))
    print('\n-- You have typed zero...' if user==0 else f'-- You have typed {tuple[user-1]}...')
    break
