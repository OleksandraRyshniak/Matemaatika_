from random import * 
keerukus=input("Valige ülesannete „Tase 1, Tase 2, Tase 3“ raskusaste: ")
arv1=int(input("Sisestage, alates millist arvest: "))
arv2=int(input("Sisestage, kuni millise arvuni: "))
kogus=int(input("Sisestage näidete arv:"))
arv_1=randint(arv1, arv2)
arv_2=randint(arv1, arv2)
arv_3=randint(arv1, arv2)
if keerukus=="Tase 1":
    try:
        for i in range (kogus):
            tehed1=["+", "-"]
            if arv_1>=arv_2:
                valitudtehe1=choice(tehed1)
                print(f"{arv_1} {valitudtehe1} {arv_2} =")
                vastus=float(input("Anna vastus: "))
            elif arv_2>arv_1:
                valitudtehe1=choice(tehed1)
                print(f"{arv_2} {valitudtehe1} {arv_1} =")
                vastus=float(input("Anna vastus: "))
            else: 
                print("Vääralt sisestatud numbrid.")
            if vastus==eval(str(arv_1)+valitudtehe1+str(arv_2)):
                print("Tore")
            else: 
                print("Vale!")
    except:
        print("Vale formaat")
elif keerukus=="Tase 2":
    for i in range (kogus):
        tehed2=["+", "-", "*", "/"]
        if arv_1>=arv_2:
            valitudtehe2=choice(tehed2)
            print(f"{arv_1} {valitudtehe2} {arv_2} =")
            vastus=float(input("Anna vastus: "))
        elif arv_2>arv_1:
            valitudtehe2=choice(tehed2)
            print(f"{arv_2} {valitudtehe2} {arv_1} =")
            vastus=float(input("Anna vastus: "))
        else: 
            print("Vääralt sisestatud numbrid.")
        if vastus==eval(str(arv_1)+valitudtehe2+str(arv_2)):
            print("Tore")
        else: 
            print("Vale!")
elif keerukus=="Tase 3":
    for i in range (kogus):
        tehed3=["+", "-", "*", "/", "**"]
        if arv_1>=arv_2 and arv_1>=arv_3 and arv_2>=3:
            valitudtehe3=choice(tehed3)
            print(f"{arv_1} {valitudtehe3} {arv_2} {valitudtehe3} {arv_3} =")
            vastus=float(input("Anna vastus: "))
        elif arv_2>=arv_1 and arv_2>=arv_3 and arv_1>=arv_3:
            valitudtehe3=choice(tehed3)
            print(f"{arv_2} {valitudtehe3} {arv_1} {valitudtehe3} {arv_3}=")
            vastus=float(input("Anna vastus: "))
        elif arv_3>=arv_2 and arv_3>=arv_1 and arv_2>=arv_1:
            valitudtehe3=choice(tehed3)
            print(f"{arv_2} {valitudtehe3} {arv_1} {valitudtehe3} {arv_3}=")
            vastus=float(input("Anna vastus: "))
        else: 
            print("Vääralt sisestatud numbrid.")
        if vastus==eval(str(arv_1)+valitudtehe2+str(arv_2)):
            print("Tore")
        else: 
            print("Vale!")
else:
    print()




