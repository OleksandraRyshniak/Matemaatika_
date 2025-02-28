from random import * 
keerukus=input("Valige ülesannete „Tase 1, Tase 2, Tase 3“ raskusaste: ")
hinne=0
try:
        arv1=int(input("Sisestage, alates millist arvest: "))
        arv2=int(input("Sisestage, kuni millise arvuni: "))
        kogus=int(input("Sisestage näidete arv:"))
except:
    print("Vale formaat!")
if keerukus=="Tase 1":
        for i in range (kogus):
            try:
                arv_1=randint(arv1, arv2)
                arv_2=randint(arv1, arv2)
                tehed1=["+", "-"]
                valitudtehe1=choice(tehed1)
                print(f"{arv_1} {valitudtehe1} {arv_2} =")
                vastus=float(input("Anna vastus: "))
                if vastus==eval(str(arv_1)+valitudtehe1+str(arv_2)):
                    print("Tore")
                    hinne+=1
                else: 
                    print("Vale!")
            except:
                print("Vale formaat!")
        if hinne==kogus:
            print("Kui soovite jätkata kontrollimist ja uuendamist, sisestage allpool Tase 2, kui mitte, sisestage Ei.")
            vas=input("Vastus: ")
            if vas=="Tase 2":
                for i in range (kogus):
                    try:
                        arv_3=randint(arv1, arv2)
                        arv_4=randint(arv1, arv2)
                        tehed2=["+", "-", "*", "/"]
                        valitudtehe2=choice(tehed2)
                        print(f"{arv_3} {valitudtehe2} {arv_4} =")
                        vastus=float(input("Anna vastus: "))
                        if vastus==round(eval(str(arv_3)+valitudtehe2+str(arv_4)),2):
                            print("Tore")
                            hinne+=1
                        else: 
                            print("Vale!")
                    except:
                            print("Vale formaat!")
                
            elif vas=="Ei":
                print(" ")
                ("Vale")
            else:
                print("Vale")
elif keerukus=="Tase 2":
        for i in range (kogus):
            try:
                arv_3=randint(arv1, arv2)
                arv_4=randint(arv1, arv2)
                tehed2=["+", "-", "*", "/"]
                valitudtehe2=choice(tehed2)
                print(f"{arv_3} {valitudtehe2} {arv_4} =")
                vastus=float(input("Anna vastus: "))
                if vastus==round(eval(str(arv_3)+valitudtehe2+str(arv_4)),2):
                    print("Tore")
                    hinne+=1
                else: 
                    print("Vale!")
            except:
                    print("Vale formaat!")
        if hinne==kogus:
            print("Kui soovite jätkata kontrollimist ja uuendamist, sisestage allpool Tase 3, kui mitte, sisestage Ei.")
            vas_=input("Vastus: ")
            if vas_=="Tase 3":
                for i in range (kogus):
                    try:
                        tehed3=["+", "-", "*", "/", "**"]
                        arv_5=randint(arv1, arv2)
                        arv_6=randint(arv1, arv2)
                        arv_7=randint(arv1, arv2)
                        valitudtehe3=choice(tehed3)
                        tehed1=["+", "-"]
                        valitudtehe1=choice(tehed1)
                        print(f"{arv_5} {valitudtehe3} {arv_6} {valitudtehe1} {arv_7} =")
                        vastus=float(input("Anna vastus: "))
                        if vastus==round(eval(str(arv_5)+valitudtehe3+str(arv_6)+valitudtehe1+str(arv_7)),2):
                            print("Tore")
                            hinne+=1
                        else: 
                            print("Vale!")
                    except:
                        print("Vale formaat!")
            elif vas_=="Ei":
                print(" ")
            else:
                ("Vale")
elif keerukus=="Tase 3":
        for i in range (kogus):
            try:
                tehed3=["+", "-", "*", "/", "**"]
                arv_5=randint(arv1, arv2)
                arv_6=randint(arv1, arv2)
                arv_7=randint(arv1, arv2)
                valitudtehe3=choice(tehed3)
                tehed1=["+", "-"]
                valitudtehe1=choice(tehed1)
                print(f"{arv_5} {valitudtehe3} {arv_6} {valitudtehe1} {arv_7} =")
                vastus=float(input("Anna vastus: "))
                if vastus==round(eval(str(arv_5)+valitudtehe3+str(arv_6)+valitudtehe1+str(arv_7)),2):
                    print("Tore")
                    hinne+=1
                else: 
                    print("Vale!")
            except:
                print("Vale formaat!")
else:
    print("Sisestage Tase 1 või Tase 2 või Tase 3.")
hin=hinne/kogus*100
if hin<60:
    print("Sinu hinne on 2.")
elif 60<= hin <75 :
    print("Sinu hinne on 3.")
elif 75<= hin<90:
    print("Sinu hinne on 4.")
elif hin>=90:
    print("Sinu hinne on 5.")
else: 
    print("Vale")