letterlist = [aword[aletter] for aword in ['cat', 'dog', 'rabbit'] for aletter in range(len(aword))]
print(letterlist) 
print(list(set(letterlist)))
