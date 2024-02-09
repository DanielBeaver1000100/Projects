import time
def spin(array=[],num=2):
    holder=""
    for i in range(num-1):
        holder=array[0]
        array.pop(0)
        array.append(holder)
    return array
def checkDictionary(letter,dic):
    try:
        dic[letter]
    except:
        ex=False
    else:
        ex=True
    return ex
def checkForLetter(letter):
    ex=False
    string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in string:
        if char in letter:
            ex=True
    return ex
def letterToNum(letter):
    alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alph)):
        if letter==alph[i]:
            return i
def numToLetter(num):
    alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alph)):
        if i==num:
            return alph[i]
def main():
    choice='~'
    I=["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
    II=["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"]
    III=["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"]
    IV=["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B"]
    V=["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K"]
    VI=["J","P","G","V","O","U","M","F","Y","Q","B","E","N","H","Z","R","D","K","A","S","X","L","I","C","T","W"]
    VII=["N","Z","J","H","G","R","C","X","M","Y","S","W","B","O","U","F","A","I","V","L","P","E","K","Q","D","T"]
    VIII=["F","K","Q","H","T","L","X","O","C","B","J","S","P","D","Z","R","A","M","E","W","N","I","U","Y","G","V"]
    UKWB=["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T",]
    UKWC=["F","V","P","J","I","A","O","Y","E","D","R","Z","X","W","G","C","T","K","U","Q","S","B","N","M","H","L",]
    plugDict={}
    displayDict={}
    plugCount=0
    print('Welcome to the enigma machene code and de-coder')
    print('Start building the Machene by entering the settings for your code')
    print()
    print('PLUG BOARD')
    print('The plug board is the settings for what letter is forced to turn into in the beginning and end of the coding/decoding process')
    print('Ex. plug [A,B] ENTER A OUTPUT B  and vice versa')
    print()
    print('every plug is connected to 2 letters, There are a MAXIMUM of 12 plugs, every letter can only be used ONCE')
    print()
    
    ##CODE FOR PLUG BOARD INPUT
    
    while(choice!='N'and plugCount<12):
        choice=input('Do you wish to add a plug(Y/N): ').strip().upper()
        if choice!='Y'and choice!='N':
            print('invalid Statement')
            
        elif choice =='Y':
            plugCount+=1
            print()
            print('Plug Number:'+str(plugCount))

            con='F'
            while con=='F':
                plugin=str(input('Enter the first letter for the plug: ')).strip().upper()

                if len(plugin)!=1 or checkForLetter(plugin)==False:
                    print('invalid Statement')
                elif checkDictionary(plugin , plugDict)==True:
                    print(plugin +" IS already connected to "+ plugDict[plugin] )   
                else:
                    con='T'
            
            con='F'
            while con=='F':
                plugin2=str(input('Enter the Second letter for the plug: ')).strip().upper()

                if len(plugin2)!=1 or checkForLetter(plugin2)==False or plugin2==plugin:
                    print('invalid Statement')
                elif checkDictionary(plugin2 , plugDict)==True:
                    print(plugin2 +" IS already connected to "+ plugDict[plugin2] )   
                else:
                    con='T'
            displayDict.update({plugin:plugin2})
            plugDict.update({plugin:plugin2})
            plugDict.update({plugin2:plugin})
            print("Plug ["+plugin+":"+plugin2+"] created")
            choice='~'
    ##"""
    ##comment slow input
    print()
    print("The next step is to choose the wheel and the notch location")
    print()
    print("Roter-Notches")
    print("There are 8 different Roters in an enigma machene however you only need to choose 3. Roters will rotate and change oriantation throughout the coding/decoding process\n there are only 2 Notchs, Notches tell the Roters when to rotate, Both Notches and Roters have start orientation 1-26 to choose from")
    print()
    print("The finished configuation will look like this")
    print(" _   _   _ \n|R|N|R|N|R|\n ¯   ¯   ¯")
    print("Every 'R' is a Roter and every 'N' is a Notch")
    print("when the wheel on the Notchs right rotates to the designated position(Ie: Notches start location) the Notch will turn the wheel to it's left once")
    print()
    print("Start by choosing the far left Roter and it starting position")
    print("Roters can only be used once")
    print()
    ##ROTER INPUT AND NOTCH SETTINGS
    ##ROTER1
    
    con='F'
    while con=='F':
        roter1=int(input('Enter the Roter for the far left (1-8): '))
        if roter1>0 and roter1<9:
            print("Roter "+str(roter1)+" Is placed in the far left slot")
            con='T'
        else:
            print('Not a valid Roter option')

    con='F'
    while con=='F':
        print()
        roter1Rot=int(input('Enter Roter '+str(roter1)+' starting position (1-26): '))
        if roter1Rot>0 and roter1Rot<27:
            print()
            print("Roter "+str(roter1)+" is starting on "+str(roter1Rot))
            con='T'
        else:
            print('Not a valid Start option')

    ##NOTCH

    con='F'
    while con=='F':
        print()
        notch1=int(input("Enter the left Notch's starting position (1-26): "))
        if notch1>0 and notch1<27:
            print()
            print("Left Notch is starting on "+str(notch1))
            con='T'
        else:
            print('Not a valid Start option')

    ##ROTER2

    con='F'
    while con=='F':
        print()
        roter2=int(input('Enter the middle Roter (1-8): '))
        if roter2==roter1:
            print("Roter "+str(roter2)+" is already in use")
        elif roter2>0 and roter2<9:
            print("Roter "+str(roter2)+" Is placed in the middle slot")
            con='T'
        else:
            print('Not a valid Roter option')  

    con='F'
    while con=='F':
        print()
        roter2Rot=int(input('Enter Roter '+str(roter2)+' starting position (1-26): '))
        if roter2Rot>0 and roter2Rot<27:
            print()
            print("Roter "+str(roter2)+" is starting on "+str(roter2Rot))
            con='T'
        else:
            print('Not a valid Start option')
            
    ##NOTCH

    con='F'
    while con=='F':
        print()
        notch2=int(input("Enter the Right Notch's starting position (1-26): "))
        if notch2>0 and notch2<27:
            print()
            print("Right Notch is starting on "+str(notch2))
            con='T'
        else:
            print('Not a valid Start option')

    ##ROTER3

    con='F'
    while con=='F':
        print()
        roter3=int(input('Enter the Right Roter (1-8): '))
        if roter3==roter1 or roter3==roter2:
            print("Roter "+str(roter3)+" is already in use")
        elif roter2>0 and roter2<9:
            print("Roter "+str(roter3)+" Is placed in the Right slot")
            con='T'
        else:
            print('Not a valid Roter option')  

    con='F'
    while con=='F':
        print()
        roter3Rot=int(input('Enter Roter '+str(roter3)+' starting position (1-26): '))
        if roter3Rot>0 and roter3Rot<27:
            print()
            print("Roter "+str(roter3)+" is starting on "+str(roter3Rot))
            con='T'
        else:
            print('Not a valid Start option')

##CHOOSE MIRROR

    print()
    print("MIRRORS")
    print("Finally the last decision is to choose the Mirror the roters will use to send the encoded letter back through the roters and twords the output" )
    print("there are 2 Mirrors to choose form 'UKW-B' or 'UKW-C'")
    print()
    con='F'
    while con=='F':
        mirror=str(input('enter the mirror for the roter set (B/C): ')).strip().upper()
        if mirror=='B'or mirror=='C':
            print()
            print("mirror UKW-"+str(mirror)+" is placed at the end of the roters")
            con='T'
        else:
            print('Not a valid mirror option')
            
##Display final settings ask for the text to encode

    print()
    print("Your enigma machene looks like this")
    print("ROTERS-NOTCHES")
    print("\n          |"+str(roter1)+"|-"+str(notch1)+"-|"+str(roter2)+"|-"+str(notch2)+"-|"+str(roter3)+"| UKW-"+str(mirror))
    print()
    print("PLUGBOARD")
    print(displayDict)
    print()
    print()
    print()
    ##"""
    
    '''
    ##Fast manual input
    plugDict.update({"A":"B"})
    plugDict.update({"B":"A"})
    plugDict.update({"Y":"Z"})
    plugDict.update({"Z":"Y"})
    plugDict.update({"D":"V"})
    plugDict.update({"V":"D"})
    plugDict.update({"E":"R"})
    plugDict.update({"R":"E"})
    plugDict.update({"Q":"M"})
    plugDict.update({"M":"Q"})
    plugDict.update({"L":"C"})
    plugDict.update({"C":"L"})
    roter1=4
    roter1Rot=25
    notch1=26
    roter2=3
    roter2Rot=15
    notch2=1
    roter3=8
    roter3Rot=16
    mirror='C'
    '''
    con='T'
    while con=='T':
        print('note numbers and spaces will not be scrambled')
        text=str(input('Enter the text to encode/decode:')).strip().upper()
##Encode
    ##Copy all lists chosen
        if roter1==1:
            roter1=I.copy()
        elif roter1==2:
            roter1=II.copy()
        elif roter1==3:
            roter1=III.copy()
        elif roter1==4:
            roter1=IV.copy()
        elif roter1==5:
            roter1=V.copy()
        elif roter1==6:
            roter1=VI.copy()
        elif roter1==7:
            roter1=VII.copy()
        elif roter1==8:
            roter1=VIII.copy()

        if roter2==1:
            roter2=I.copy()
        elif roter2==2:
            roter2=II.copy()
        elif roter2==3:
            roter2=III.copy()
        elif roter2==4:
            roter2=IV.copy()
        elif roter2==5:
            roter2=V.copy()
        elif roter2==6:
            roter2=VI.copy()
        elif roter2==7:
            roter2=VII.copy()
        elif roter2==8:
            roter2=VIII.copy()

        if roter3==1:
            roter3=I.copy()
        elif roter3==2:
            roter3=II.copy()
        elif roter3==3:
            roter3=III.copy()
        elif roter3==4:
            roter3=IV.copy()
        elif roter3==5:
            roter3=V.copy()
        elif roter3==6:
            roter3=VI.copy()
        elif roter3==7:
            roter3=VII.copy()
        elif roter3==8:
            roter3=VIII.copy()

        if mirror=='B':
            mirror=UKWB.copy()
        else:
            mirror=UKWC.copy()
    #Rotate and setup the wheels
        roter1=spin(roter1,roter1Rot)
        roter2=spin(roter2,roter2Rot)
        roter3=spin(roter3,roter3Rot)
        
    #Go through text and append to encoded or encript
        encoded=""
        for i in range(len(text)):
            if checkForLetter(str(text[i]))==False:
                encoded=encoded+str(text[i])
            else:
            #key press turning roters
                if notch1==roter1Rot and notch2==roter2Rot:
                    roter1=spin(roter1)
                    roter1Rot+=1
                    if roter1Rot>26:
                        roter1Rot=1
                    roter2=spin(roter2)
                    roter2Rot+=1
                    if roter2Rot>26:
                        roter2Rot=1
                    roter3=spin(roter3)
                    roter3Rot+=1
                    if roter3Rot>26:
                        roter3Rot=1
                elif notch1==roter1Rot:
                    roter1=spin(roter1)
                    roter1Rot+=1
                    if roter1Rot>26:
                        roter1Rot=1
                    roter2=spin(roter2)
                    roter2Rot+=1
                    if roter2Rot>26:
                        roter2Rot=1
                else:
                    roter1=spin(roter1)
                    roter1Rot+=1
                    if roter1Rot>26:
                        roter1Rot=1

            #plugboard
                if checkDictionary(text[i],plugDict)==True:
                    letter=plugDict[text[i]]
                else:
                    letter=text[i]
            #print(letter)
            #plugboard to roter1
                letternum=letterToNum(letter)
                letter=roter1[letternum]
            #print(letter)
            #roter1 to roter2
                letternum=letterToNum(letter)
                letter=roter2[letternum]
            #print(letter)
            #roter2 to roter3
                letternum=letterToNum(letter)
                letter=roter3[letternum]
            #print(letter)
            #roter3 to mirror
                letternum=letterToNum(letter)
                letter=mirror[letternum]
            #print(letter)   
            #mirror sends to itsself
                letternum=letterToNum(letter)
                letter=mirror[letternum]
            #print(letter)
            #Back through roter3
                letter=roter3[roter3.index(numToLetter(mirror.index(letter)))]
            #print(letter)
            #Back through roter2
                letter=roter2[roter2.index(numToLetter(roter3.index(letter)))]
            #print(letter)
            #Back through roter1
                letter=roter1[roter1.index(numToLetter(roter2.index(letter)))]
            #print(letter)
            #out of roter1
                letternum=letterToNum(letter)
                letter=numToLetter(roter1.index(letter))
           # print(letter)

            #Plugboard
                if checkDictionary(letter,plugDict)==True:
                    letter=plugDict[letter]

            #Append to results

                encoded=encoded+str(letter)
            
        

    
##print results
        print()
        print()
        print(encoded)
        print()
        con2='F'
        while con2=='F':
            choice=input('Do you wish to continue(Y/N): ').strip().upper()
            if choice!='Y'and choice!='N':
                print('invalid Statement')
                
            elif choice =='N':
                print('OK Shutting down...')
                con='F'
                con2='T'
                time.sleep(5)
                exit()
            else:
                print()
                con2='T'
        
    
            
            
main()



                



                

            
        
        
        
        
    
        
