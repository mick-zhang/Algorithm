def texts(text):
    letterlist = []
    for aword in text:
        for aletter in aword:
            if aletter not in letterlist:
                letterlist.append(aletter)
    print(letterlist)

def main():
    Animal = ['cat', 'dog', 'rabbit']
    Computer = ['keyboard', 'monitor', 'mouse']
    text = [Animal, Computer]
    
    for result in text:
        texts(result)
        
main()
