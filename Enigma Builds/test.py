


def checkForLetter(letter):
    ex=False
    string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in string:
        if char in letter:
            ex=True
    return ex

def main():
    
    print('note numbers and spaces will not be scrambled')
    text=str(input('Enter the text to encode/decode:')).strip().upper()
    encoded=""
    for i in range(len(text)):
        if checkForLetter(str(text[i]))==False:
            encoded=encoded+str(text[i])
        
    print(encoded)


main()
