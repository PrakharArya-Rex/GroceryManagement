import pickle
F=open('grocery.dat','r')
Ltotoal=[]
for x in range(5):
              Lgrand=pickle.load(F)
              Ltotal.append(Lgrand)
print(Ltotal)
