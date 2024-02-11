import pickle

def writing(l):
    try:
        n=int(input("Enter number of lines u would like to enter : "))
        #You can add only positive numbers of items
        assert(n>0)
        F=open("grocery.dat",'ab')
        #Changing the number of elements stored in the file
        l=l+n
        for x in range(n):
            print()
            a=input('Name : ')
            b=int(input('Item number : '))
            c=int(input('Quantity. : '))
            d=int(input('Price : '))
            L=[a,b,c,d]
            pickle.dump(L,F)
        F.close()
        return(l)
    except ValueError:
        print("You are requested to enter only a number, don't include symbols or alphabets")
    except AssertionError:
        print('Please enter a positive number only, no negative integer allowed')
    except:
        print('Oops! An unexpected error happened')
    else:
        print('Record(s) successfully stored')
    finally:
        print('Writing optioin from menu completed')

l=0
x=writing(l)
print(x)
