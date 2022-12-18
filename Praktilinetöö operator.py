from math import *
#6
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
D=b**2-4*a*c
print(f"D={D}")
if D>0:
    x1=-b+sqrt(D)/2*a
    x2=-b-sqrt(D)/2*a
    print(f"x1={round(x1, 2)}, x2={round(x2, 2)}.")
if D==0:
    x=-b/2*a
    print(f"x={round(x, 2)}")
if D<0:
    print("lahendusi pole")
print()

#5



#3
v=(input("Tahad lahti mõtestada nädalapäeva järjekorranumbri ? (Jah või Ei): "))
if v=="Jah" or v=="jah":
    a=int(input("Kirjuta summa: "))
    if a==1:
        n="Esmaspäev"
        print(f"{n}")
    elif a==2:
        n="Teisepäev"
        print(f"{n}")
    elif a==3:
        n="Kolmapäev"
        print(f"{n}")
    elif a==4:
        n="Neljapäev"
        print(f"{n}")
    elif a==5:
        n="Reede"
        print(f"{n}")
    elif a==6:
        n="Laupäev"
        print(f"{n}")
    elif a==7:
        n="Laupäev"
        print(f"{n}")
if v=="Ei" or v=="ei":
    print("Kahju")

print()

#2
try:
    a=int(input("Kirjuta esimene summa:"))
    b=int(input("Kirjuta teine summa:"))
    c=int(input("Kirjuta komane summa:"))
    n=a+b+c
    if a>0:
        print("Positiivne")
        if n>180 or n<180:
            print("Need võivad olla sama kolmnurga nurgad")
            if n<180:
                print(f"Võrdkülgne kolmnurk {n} ")
            else:
                print(f"Skaleeni kolmnurk {n}")
                if n>180:
                    print(f"võrdhaarne kolmnurk {n}")
                else:
                    print("Mitte võrdhaarne kolmnurk")
    else:
        print("Negatiivne")
except:
    print("Viga!")

print()


#1
try:
    a=int(input("Kirjuta summa:"))
    if a>0:
        print("Positiivne")
        if a%2==0:
            n=a/2
            print(f"{a} on paaris")
        else:
            print(f"{a} on paaritu")
    else:
        print("Negatiivne")
except:
    print("Vale nummber")



    