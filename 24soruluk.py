# Mevlüt Çelik - 30.10.2022


# Soru 1
# 1-  "Ingilizce, Almanca, Fransizca, Ispanyolca" elemanlarina sahip bir liste oluşturunuz.
liste = ["İngilizce", "Almanca", "Fransızca", "İspanyolca"]



# Soru 2
# 2-  Liste Kaç elemanlidir ?
print(f"Liste {len(liste)} elemanlıdır.")



# Soru 3
# 3-  Listenin ilk ve son elemani nedir ?
print(f"Listenin ilk elemanı: {liste[0]}")
print(f"Listenin son elemanı: {liste[-1]}")



# Soru 4
# 4-  Ispanyolca değerini Japonca ile değiştirin.
liste[3] = "Japonca"
print(liste)



# Soru 5
# 5-  Çince listenin bir elemani midir ?
print(liste.count("Çince")) # Eğer sonuç 0 ise eleman değildir.



# Soru 6
# 6-  Listenin -2 indeksindeki değer nedir ?
print(f"Listenin -2 indeksine sahip eleman: {liste[-2]}'dır.")



# Soru 7
# 7-  Listenin ilk 3 elemanini alin.
print(f"Listenin ilk üç elemanı: {liste[0:3]}")



# Soru 8
# 8-  Listenin son 2 elemani yerine "Japonca" ve "Rusca" değerlerini ekleyin.
liste[-1] = "Rusça"
liste[-2] = "Japonca"
print(liste)



# Soru 9
# 9-  Listenin üzerine "Cince" ve "Korece" değerlerini ekleyin.
liste.append("Çince")
liste.append("Korece")
print(liste)



# Soru 10
# 10- Listenin son elemanini silin.
liste.pop()
print(liste)



# Soru 11
# 11- Liste elemanlarini tersten yazdiriniz.
liste.reverse()
print(liste)



isimler = ['Ali', 'Nihal', 'Yigit', 'Bilge']
yillar = [1987, 1988, 2017, 2019]


# Soru 12
# 12-) Gokhan ismini listenin sonuna ekleyiniz.
isimler.append("Gökhan")
print(isimler)



# Soru 13
# 13-) Onur ismini listenin basina ekleyiniz.
isimler.insert(0, "Onur")
print(isimler)



# Soru 14
# 14-) Ali isminin indeks numarasini ekrana yazdiriniz.
print(f"Ali isminin indeks numarası {isimler.index('Ali')}'dir.")



# Soru 15
# 15-) Ali ismini listeden siliniz.
isimler.remove("Ali")
print(isimler)



# Soru 16
# 16-) Bayram ismi listenin bir elemani midir?
print(isimler.count("Bayram")) # Eğer sonuç 0 ise eleman değildir.


# Soru 17
# 17-) Liste elemanlarini ters ceviriniz.
isimler.reverse()
print(isimler)



# Soru 18
# 18-) Liste elemanlarini alfabetik olarak siralayiniz.
isimler.sort()
print(isimler)



# Soru 19
# 19-) araclar=['TOGG','Tesla'] listesini isimler listesine ekleyiniz.
isimler.append(["TOGG", "Tesla"])
print(isimler)



# Soru 20
# 20-) Yillar listesini artan sekilde siralayiniz.
yillar.sort()
print(yillar)



# Soru 21
# 21-) yillar dizisinin en buyuk ve en kucuk elemanlari nelerdir?
print(f"Yıllar dizisinin en büyük elemanı: {max(yillar)}")
print(f"Yıllar dizisinin en küçük elemanı: {min(yillar)}")



# Soru 22
# 22-) yillar dizisinde kac adet 2017 degeri vardir?
print(f"Yıllar dizisinde {yillar.count(2017)} adet 2017 değeri vardır.")



# Soru 23
# 23-) yillar dizisinin tum elemanlarini siliniz.
yillar.clear()
print(yillar)


# Soru 24
# 24-) Kullanicidan alacaginiz 5 adet tablet bilgisayar markasini bir listede saklayiniz. 
marka1 = input("Birinci tablet bilgisayar markasını giriniz: ")
marka2 = input("İkinci tablet bilgisayar markasını giriniz: ")
marka3 = input("Üçüncü tablet bilgisayar markasını giriniz: ")
marka4 = input("Dördüncü tablet bilgisayar markasını giriniz: ")
marka5 = input("Beşinci tablet bilgisayar markasını giriniz: ")

markaListesi = [marka1, marka2, marka3, marka4, marka5]
print(markaListesi)
