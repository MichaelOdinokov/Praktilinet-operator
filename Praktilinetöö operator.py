from math import *
from random import ''
try:
    a=int(input("Kirjuta summa:"))
    if a>0:
        print("Positiivne")
        if a%2==0:
            n=a/2
            print(f" on paaris")
        else:
            print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale nummber")

    

