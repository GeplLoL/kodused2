##1
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55

#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus!=o_vastus:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#    else:
#        break
#print("Õige vastus! Katsed oli ...",k )

#2

#x=0
#while True:
#    if x<3000:
#        if x%2==1:

#            print(x, end=" ")

#        x+=1
#    else:
#        break

#for x in range (1,30,2):
#    print(x, end=" ")

print("*** MÄNGUD KÜSIMUSED ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => ")))) #lisatud sulgudes
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Pole mõtet nulliga midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paarisnumbreid ja kui palju paarituid")
    print()
    c=b=a
    paaris = 0 #eemaldasin üleliigse võrdse
    paaritu = 0 #eemaldasin üleliigse võrdse
    while b > 0: #koolonid

        if b % 2 == 0: #lisatud võrdne
            paaris += 1
        else:
            paaritu += 1
        b = b // 10 #eemaldas üleliigse taandumise
    print("Numbrite arv:", paaris) #lisasin luti
    print("Paaritud numbrid:", paaritu) # lisasin luti
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörame sisestatud arvu ümber")
    print()
    b=0 #eemaldas üleliigse taandumise
    while a > 0: #koolonid
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Ümberpööratud* arv b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Kontrollime Syracuse hüpoteesi") #eemaldasin üleliigse sulguri
    print()
    if c % 2 == 0: #lisatud võrdne
        print("c - paarisarv. Jagame 2ga.")
    else:
        print("c - paaritu arv. Korrutame 3-ga, lisame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0: #lisatud võrdne
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(int(c), end=" ") #lisatud sepised
    print()
    print("Hüpotees on õige")
