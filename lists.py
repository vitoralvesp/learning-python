# obs: lists are mutable
lunch=['hamburguer','fries','coca cola']
lunch.append('ice cream') #add ice cream to the end (length now is 4)
lunch.insert(0,'anything else') #add anything else in the 0 position without removing hamburguer (length now is 5)
lunch.pop(2) #remove fries
lunch.remove('anything else') #remove anything else
lunch.reverse() # ['ice cream', 'coca cola', 'hamburguer']

alphabet=['b','e','a','c','d']
alphabet.sort() #puts in order (strings, integers, ...)

newlunch=lunch[:] # copy lunch without conect them
newlunch[2]='orange juice' # change newlunch (lunch not affected)

