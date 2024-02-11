#Prakhar Arya XII A Program File
#Grocery Store Manangement

#Importing the modules to be used for the program
import pickle
import os

#For differentiating menus
def asterisk_liner():
    print('**************************************************************************************************************************************')

def dash_liner(w):
    for x in range(w):
        print('-',end='')
    print()

#For using to repeat menu choosing line
def chooser():
    print('              ----Please choose a function from the following Menu----        ')
    print()

#For counting number of items from previously stored data
F=open('grocery.dat','rb')
l=1
Y=F.readlines()
for x in Y:
    z=len(x)
    for q in range(z-1):
        if x[q:q+1]==b'.':
            l=l+1
F.close()

#Defining function for writing data into the file with exception handling
def writing(l):
    #using exception handling for this block
    try:
        print()
        n=int(input("Enter number of lines you would like to enter : "))
        print()
        Ltotal=list()
        F=open("grocery.dat",'ab+')
        f=0
        F.seek(0)
        for f in range(l):
                Lgrand=pickle.load(F)
                Ltotal.append(Lgrand)
        plotter=len(Ltotal)
        #You can add only positive numbers of items
        assert(n>0)
        variable=0
        for variable in range(n):
            while True:
                a=input('Name : ')
                flag = 0
                for totaler in range(plotter):
                    if a.lower() == Ltotal[totaler][0].lower():
                        flag=10
                if flag==0:
                    break
                else:
                    print('Sorry Item Name already exists, Please enter a new name')
                    print()
            while True:
                b=int(input('Item number : '))
                flag = 0
                for totaler in range(plotter):
                    if b == int(Ltotal[totaler][1]):
                        flag=10
                if flag==0:
                    break
                else:
                    print('Sorry Item Number already exists, Please enter a new name')
                    print()
            c=int(input('Quantity. : '))
            d=int(input('Price : '))
            L=[a,b,c,d]
            pickle.dump(L,F)
            print()
        F.close()
        #Changing the number of elements stored in the file
        l=l+n
        return(l)
    except ValueError:
        print("You are requested to enter only a number, don't include symbols or alphabets")
        print()
    except AssertionError:
        print('Please enter a positive number only, no negative integer allowed')
        print()
    '''except:
        print('Oops! An unexpected error happened')
        print()
    finally:
        print('Writing option from menu completed')'''
        
#Defining a func. for reading data from the binary file
def reading(z):
    print()
    F=open("grocery.dat", "rb")
    Ltotal=list()
    header=['Name', 'Item No', 'Quantity', 'Price']
    chooser()
    print('1. Selective Reading')
    print('2. Collective reading')
    print()
    y=int(input('Enter your choice : '))
    print()
    asterisk_liner()
    print()
    F.seek(0)
    if y==2:
        #A. Making a lists with sub-list according to choice (Same logic used afterwards also)
          for x in range(z):
              Lgrand=pickle.load(F)
              Ltotal.append(Lgrand)
          plotter=len(Ltotal)
        #B. Taking 20 as an arbitary number for storage of characters assuming input not be large than 20 char(Same logic used afterwards also)
          printing= '{:>20}  {:>20}  {:>20} {:>20}'.format(header[0] , header[1] , header[2] , header[3])
          print(printing)
          dash_liner(86)
          for totaler in range(plotter):
                actual='{:>20}  {:>20}  {:>20} {:>20}'.format(Ltotal[totaler][0], Ltotal[totaler][1], Ltotal[totaler][2], Ltotal[totaler][3])
                print(actual)
          print()
          F .close()
    elif y==1:
        chooser()
        print('1. Details of a specific item')
        print('2. Details of item(s) displayed by Item number')
        print()
        t=int(input('Enter your choice : '))
        print()
        asterisk_liner()
        print()
        F.seek(0)
        if t==1:
            u=input('Enter your item name : ')
            print()
            for x in range(z):
              Lgrand=pickle.load(F)
              if Lgrand[0].lower()==u.lower():
                  Ltotal.append(Lgrand)
            plotter=len(Ltotal)
            #A.
            printing= '{:>20}  {:>20}  {:>20} {:>20}'.format(header[0] , header[1] , header[2] , header[3])
            print(printing)
            dash_liner(86)
            #B.
            for totaler in range(plotter):
                  actual='{:>20}  {:>20}  {:>20} {:>20}'.format(Ltotal[totaler][0], Ltotal[totaler][1], Ltotal[totaler][2], Ltotal[totaler][3])
                  print(actual)                                          
            print()
            F .close()
        elif t==2:
            chooser()
            print('1. Display items if greater than or equal to Item Number')
            print('2. Display items if smaller than or equal to Item Number')
            print()
            c=int(input('Enter your choice : '))
            print()
            alpha = int(input('Enter your Item Number : '))
            print()
            asterisk_liner()
            print()
            if c==1:
                for i in range(z):
                    Lgrand=pickle.load(F)
                    if Lgrand[1]>=alpha:
                        Ltotal.append(Lgrand)
                plotter=len(Ltotal)
                #A.
                printing= '{:>20}  {:>20}  {:>20} {:>20}'.format(header[0] , header[1] , header[2] , header[3])
                print(printing)
                dash_liner(86)
                #B.
                for totaler in range(plotter):
                    actual='{:>20}  {:>20}  {:>20} {:>20}'.format(Ltotal[totaler][0], Ltotal[totaler][1], Ltotal[totaler][2], Ltotal[totaler][3])
                    print(actual)
                print()
                F .close()
            elif c==2:
                for i in range(z):
                    Lgrand=pickle.load(F)
                    if Lgrand[1]<=alpha:
                      Ltotal.append(Lgrand)
                plotter=len(Ltotal)
                #A.
                printing= '{:>20}  {:>20}  {:>20} {:>20}'.format(header[0] , header[1] , header[2] , header[3])
                print(printing)
                dash_liner(86)
                #B.
                for totaler in range(plotter):
                    actual='{:>20}  {:>20}  {:>20} {:>20}'.format(Ltotal[totaler][0], Ltotal[totaler][1], Ltotal[totaler][2], Ltotal[totaler][3])
                    print(actual)
                print()
                F .close()
                #I. If wrong choices were intered
            else:
                print("Sorry wrong choice as unavailable")
                F.close()
        else:
            print('Sorry wrong choice as unavailable')
            F.close()
    else:
        print('Sorry wrong choice as unavailable')
        F.close()

#Modifying the price or quantity of the list of records
def modifying(d):
    F=open('grocery.dat','rb')
    Lmodified=list()
    #To check if records were modified or not
    flag=0
    chooser()
    #As other details remain the same, so can only be dropped by deleting
    print('1. Change the quantity ')
    print('2. Change the price')
    print()
    choice=int(input('Please enter your choice : '))
    print()
    item_name=input('Enter your Item Name to be modified : ')
    print()
    new_Quantity=0
    new_price=0
    asterisk_liner()
    print()
    #Changing items by item name seperately 
    if choice==1:
        new_Quantity=int(input('Enter your new quantity : '))
    if choice==2:
        new_price=int(input('Enter your new price : '))
    F.seek(0)
    #Running one loop for easier processing
    for x in range(d):
        #Changing flag values once matched and values are changed
        Lgrand=pickle.load(F)
        if Lgrand[0].lower()==item_name.lower():
            if choice==1:
                Lgrand[2]=new_Quantity
                flag=4
            if choice==2:
                Lgrand[3]=new_price
                flag=4
        Lmodified.append(Lgrand)
    if flag==0:
            print('Sorry your item name was not found as it does not exist')
    #Deleting the whole list and substituting with modified list
    counter=len(Lmodified)
    F.close
    F=open("grocery.dat",'ab+')
    F.seek(0)
    F.truncate()
    for x in range(counter):
        pickle.dump(Lmodified[x],F)

#Function to delete elements from the records
def deleting(b):
    F=open('grocery.dat','rb')
    Fnew=open('temp.dat','ab')
    chooser()
    print('1. Delete an item specifically(Name/ Item Number)')
    print('2. Delete items by amount(Quantity/ Price)')
    print()
    option=int(input('Enter your choice : '))
    print()
    asterisk_liner()
    print()
    F.seek(0)
    if option==1:
        chooser()
        print('1. Delete an item by Item Name')
        print('2. Delete an item by Item Number')
        print()
        var=int(input('Enter your choice : '))
        print()
        asterisk_liner()
        print()
        if var==1:
            deleter=input('Enter Name of your item to be deletd : ')
            #X. Dropping the unrequired item and reducing the quantity
            for x in range(b):
                Lgrand=pickle.load(F)
                if Lgrand[0].lower()==deleter.lower():
                    b=b-1
                    continue
                else:
                    pickle.dump(Lgrand,Fnew)
            F.close()
            os.remove('grocery.dat')
            Fnew.close()
            os.rename('temp.dat','grocery.dat')
            return(b)
        elif var==2:
            remover=int(input('Enter Item Number of your item to be deletd : '))
            #X.
            for x in range(b):
                Lgrand=pickle.load(F)
                if Lgrand[1]==remover:
                    b=b-1
                    continue
                else:
                    pickle.dump(Lgrand,Fnew)
            F.close()
            os.remove('grocery.dat')
            Fnew.close()
            os.rename('temp.dat','grocery.dat')
            return(b)
        else:
            print("Please enter a valid option")
    elif option==2:
        chooser()
        #To return quantities with less or too much quantity or price all at once
        print('1. Delete the items as per Quantity')
        print('2. Delete the items as per Price')
        print()
        good=int(input('Enter your choice : '))
        print()
        asterisk_liner()
        print()
        if good==1:
            chooser()
            print('1. Delete items if greater than or equal to a specific Quantity')
            print('2. Delete items if smaller than or equal to a specific Quantity')
            print()
            great=int(input('Enter your choice : '))
            print()
            asterisk_liner()
            print()
            if great==1:
                cutter=int(input('Enter the Quantity from where you want the deletion to start : '))
                #X.
                for x in range(b):
                    Lgrand=pickle.load(F)
                    if Lgrand[2]>=cutter:
                        b=b-1
                        continue
                    else:
                        pickle.dump(Lgrand,Fnew)
                F.close()
                os.remove('grocery.dat')
                Fnew.close()
                os.rename('temp.dat','grocery.dat')
                return(b)
            elif great==2:
                #X.
                cutter=int(input('Enter the Quantity from where you want the deletion to start : '))
                for x in range(b):
                    Lgrand=pickle.load(F)
                    if Lgrand[2]<=cutter:
                        b=b-1
                        continue
                    else:
                        pickle.dump(Lgrand,Fnew)
                F.close()
                os.remove('grocery.dat')
                Fnew.close()
                os.rename('temp.dat','grocery.dat')
                return(b)
            else:
                print('You have made an invalid choice')
                F.close()
                Fnew.close()
                return(b)
        elif good==2:
            chooser()
            print('1. Delete items if greater than or equal to a specific Price')
            print('2. Delete items if smaller than or equal to a specific Price')
            print()
            great=int(input('Enter your choice : '))
            print()
            asterisk_liner()
            print()
            if great==1:
                cutter=int(input('Enter the price from where you want the deletion to start : '))
                #X.
                for x in range(b):
                    Lgrand=pickle.load(F)
                    if Lgrand[3]>=cutter:
                        b=b-1
                        continue
                    else:
                        pickle.dump(Lgrand,Fnew)
                F.close()
                os.remove('grocery.dat')
                Fnew.close()
                os.rename('temp.dat','grocery.dat')
                return(b)
            elif great==2:
                cutter=int(input('Enter the price from where you want the deletion to start : '))
                #X.
                for x in range(b):
                    Lgrand=pickle.load(F)
                    if Lgrand[3]<=cutter:
                        b=b-1
                        continue
                    else:
                        pickle.dump(Lgrand,Fnew)
                F.close()
                os.remove('grocery.dat')
                Fnew.close()
                os.rename('temp.dat','grocery.dat')
                return(b)
            else:
                print('You have made an invalid choice')
                F.close()
                Fnew.close()
                return(b)
        else:
            print('You have made an invalid choice')
            F.close()
            Fnew.close()
            return(b)
    else:
        print('Sorry please neter a right choice')
        F.close()
        Fnew.close()
        return(b)

def billing(s):
    F=open("grocery.dat", "rb")
    print()
    Ltotal=list()
    header=['Name', 'Item No', 'Quantity', 'Price']
    #A.
    for x in range(s):
        Lgrand=pickle.load(F)
        Ltotal.append(Lgrand)
    plotter=len(Ltotal)
    #B.
    printing= '{:>20}  {:>20}  {:>20} {:>20}'.format(header[0] , header[1] , header[2] , header[3])
    print(printing)
    dash_liner(86)
    for totaler in range(plotter):
        actual='{:>20}  {:>20}  {:>20} {:>20}'.format(Ltotal[totaler][0], Ltotal[totaler][1], Ltotal[totaler][2], Ltotal[totaler][3])
        print(actual)
    print()
    F .close()
    F=open("grocery.dat", "rb")
    Joker=int(input('Enter number of items you would like to purchase : '))
    print()
    q=int(Joker)
    Lmoderate=list()
    Lmoderate.extend(Ltotal)
    Lbill=list()
    if Joker <= plotter:
        for x in range(Joker):
            Ltotal=Lmoderate
            Lmoderate=list()
            checking=0
            taker=int(input('Enter your Item Number : '))
            for gg in range(plotter):
                if taker == int(Ltotal[gg][1]):
                    checking=10
                    op=int(input('Enter the amount or the number of items you would like to purchase : '))
                    if op <= int(Ltotal[gg][2]):
                        Lstore=[Ltotal[gg][0],Ltotal[gg][1],op,Ltotal[gg][3],op*int(Ltotal[gg][3])]
                        Lcheese=[Ltotal[gg][0],Ltotal[gg][1],int(Ltotal[gg][2])-op,Ltotal[gg][3]]
                        Lbill.append(Lstore)
                        Lmoderate.append(Lcheese)
                    else:
                        print('ERROR : Sorry you cannot order more than the maximum value :',int(Ltotal[gg][2]))
                        Lteller=[Ltotal[gg][0],Ltotal[gg][1],Ltotal[gg][2],Ltotal[gg][3]]
                        Lmoderate.append(Lteller)
                else:
                    Lteller=[Ltotal[gg][0],Ltotal[gg][1],Ltotal[gg][2],Ltotal[gg][3]]
                    Lmoderate.append(Lteller)
            if checking == 0:
                print('ERROR : Sorry no item was found with this Number')
            print()
    counter=len(Lmoderate)
    F.close
    F=open("grocery.dat",'ab')
    F.seek(0)
    F.truncate()
    for x in range(counter):
        pickle.dump(Lmoderate[x],F)
    F.close()
    g=len(Lbill)
    starter=['Name', 'Item No', 'Quantity', 'Price','Amount']
    printing= '{:>20}  {:>20}  {:>20} {:>20} {:>20}'.format(starter[0] ,starter[1] ,starter[2] ,starter[3] ,starter[4] ,)
    print(printing)
    dash_liner(108)
    Totaling=0
    for v in range(g):
        actual='{:>20} {:>20} {:>20} {:>20} {:>20}'.format(Lbill[v][0] ,Lbill[v][1] ,Lbill[v][2] ,Lbill[v][3] ,Lbill[v][4])
        print(actual)
        Totaling += int(Lbill[v][4])
    print('{:>62} {:>20} {:>20}'.format('SGST','5%',float(int(Totaling)/20)))
    print('{:>62} {:>20} {:>20}'.format('CGST','5%',float(int(Totaling)/20)))
    print('{:>83} {:>20}'.format('Total',float(int(Totaling)+int(Totaling)/10)))

print()
choice=0
while True:
    if choice=='6':
        break
    else:
        user=input('Please Enter your Username : ')
        code=input('Please Enter your password : ')
        if code=='1234' and user=='Admin':
            print()
            asterisk_liner()
            print()
            print('Total Already Existing Records :',l)
            while True:
                #Informing user no. of previously stored items
                print()
                asterisk_liner()
                print() 
                print('           ---- Welcome Admin! GMSA ( The Grocery Store Management App ) ----         ')
                print('                     ----Tell me How can We Help you today----                               ')
                print()
                chooser()
                print('1. Adding new items to the list')
                print('2. Display the record of the items stored in the list')
                print("3. Modify the items stored in the list")
                print('4. Delete previously stored data from the list')
                print('5. Genearte a bill for the customer')
                print('6. Exit')
                print()
                choice=input('Please Enter your choice : ')
                print()
                asterisk_liner()
                if choice=='1':
                    p=writing(l)
                    l=p
                elif choice=='2':
                    reading(l)
                elif choice=='3':
                    modifying(l)
                    print()
                elif choice=='4':
                    w=deleting(l)
                    l=w
                    F=open('temp.dat','a+')
                    F.close()
                elif choice=='5':
                    billing(l)
                elif choice=='6':
                    print()
                    break
                else:
                    print()
                    print('Please enter a valid choice')
        else:
            print('Sorry wrong password or Username entered')
            print()
print('Thank You!')
print()
asterisk_liner()
