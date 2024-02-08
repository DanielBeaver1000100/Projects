
def main():
    choice='~'
    wheel1=[]
    wheel2=[]
    wheel3=[]
    wheel4=[]
    wheel5=[]
    wheel6=[]
    pluglist1=[]
    pliglist2=[]
    while not(choice=='Q'):
        print()
        print('1. Choose 3 wheels')
        print('2. Plug board')
        print('3. Set Roter number')
        print('4. Set knob number')
        print('5. assemble Enigma and Enter Text')
        print('Q. Quit')
        print()
        choice=input('please enter a number from the menue:').strip().upper()

        #Quit
        
        if choice=='Q':
            print('Goodbye')
            
        #Choose 3 wheels
            
        elif choice=='1':
            check='n'
            while check=='n':
                wheelno1=int(input('Enter the wheel for position 1: '))
                if (wheelno1<7 and wheelno1>=1):
                    print('position 1 = wheel',str(wheel1))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel, wheel range 1-6')
                    print()

            check='n'
            while check=='n':
                wheelno2=int(input('Enter the wheel for position 2: '))
                if (wheelno2<7 and wheel2>=1)and wheelno2 != wheelno1:
                    print('position 2 = wheel',str(wheel2))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel, wheel range 1-6, no duplicate wheels')
                    print()

            check='n'
            while check=='n':
                wheelno3=int(input('Enter the wheel for position 3: '))
                if (wheelno3<7 and wheelno3>=1)and wheelno3 != wheelno1 and wheel3 != wheelno2:
                    print('position 3 = wheel',str(wheel3))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel, wheel range 1-6, no duplicate wheels')
                    print()

        #Plug board

        elif choice=='2':


        #Set roter number

        elif choice=='3':
            check='n'
            while check=='n':
                roter1=int(input('Enter the wheels rotation for position 1: '))
                if (roter1<27 and roter1>=1):
                    print('position 1 wheel rotated to ',str(roter1))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel rotation, rotation range 1-26')
                    print()

            check='n'
            while check=='n':
                roter2=int(input('Enter the wheels rotation for position 2: '))
                if (roter2<27 and roter2>=1):
                    print('position 2 wheel rotated to ',str(roter2))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel rotation, rotation range 1-26')
                    print()

            check='n'
            while check=='n':
                roter3=int(input('Enter the wheels rotation for position 3: '))
                if (roter3<27 and roter3>=1):
                    print('position 3 wheel rotated to ',str(roter2))
                    print()
                    check='y'
                else:
                    print('Not a valid wheel rotation, rotation range 1-26')
                    print()


        #Ste knob number

        elif choice=='4':
            
            check='n':
            while check=='n':
                knob1=int(input('Enter the posioion of knob 1: '))
                if (knob1<27 and knob1>=1):
                    print('knob 1 set to ',str(knob1))
                else:
                    print('Not a valid posision, position range 1-26')
                    print()

            check='n':
            while check=='n':
                knob2=int(input('Enter the posioion of knob 1: '))
                if (knob2<27 and knob2>=1):
                    print('knob 2 set to ',str(knob2))
                else:
                    print('Not a valid posision, position range 1-26')
                    print()
            

            

        
            
