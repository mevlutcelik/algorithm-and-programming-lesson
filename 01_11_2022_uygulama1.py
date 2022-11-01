sayi1 = float(input("1. Sayıyı girin: "))
sayi2 = float(input("2. Sayıyı girin: "))
sayi3 = float(input("3. Sayıyı girin: "))

liste = []

if sayi1 % 2 == 0:
    liste.append(sayi1)
if sayi2 % 2 == 0:
    liste.append(sayi2)
if sayi3 % 2 == 0:
    liste.append(sayi3)

print(liste)


plakalar = {
    "ankara": 6
}

il1 = input("Şehir girin: ")
plaka1 = input("Plaka girin: ")


il2 = input("Şehir girin: ")
plaka2 = input("Plaka girin: ")


il3 = input("Şehir girin: ")
plaka3 = input("Plaka girin: ")


il4 = input("Şehir girin: ")
plaka4 = input("Plaka girin: ")


il5 = input("Şehir girin: ")
plaka5 = input("Plaka girin: ")


plakalar[il1] = plaka1
plakalar[il2] = plaka2
plakalar[il3] = plaka3
plakalar[il4] = plaka4
plakalar[il5] = plaka5

if plakalar["izmir"]: # tüm değerlerin küçük girildiğini varsayalım
    plakalar.pop("izmir")
print(plakalarü)
