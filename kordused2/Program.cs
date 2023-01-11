print("Arvuta peast! ...4*100-55")

o_vastus = 4 * 100 - 55

vastus = int(input("Lahenda ülesanne ..."))

k = 1

while vastus != o_vastus:

    print("Viga! Sisesta Õige vastus on ...", )

    vastus = int(input("Sisesta vastus ..."))

    k += 1

print("Õige vastus! Katsed oli ...", k)