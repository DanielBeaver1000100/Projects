def numToLetter(num):
    alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alph)):
        if i==num:
            return alph[i]


def letterToNum(letter):
    alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alph)):
        if letter==alph[i]:
            return i
def main():
    text='A'
    print(text)
    print()
    text=letterToNum(text)
    print(text)
    print()
    text=numToLetter(text)
    print(text)
main()
    
