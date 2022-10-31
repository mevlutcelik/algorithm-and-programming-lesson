# Mevlüt Çelik - 30.10.2022

# ÖDEV: Quiz 5 i (6. Ders Slide nın 2. sayfasındaki 5 soruyu) çözüp python dosyasını (tek dosya) yükleyiniz.

#########################################################################################

# Soru 1
'''
1-) Kullanicidan 5 kisilik bir ailenin bireylerinin yasini tek tek alip bunlari bir listeye ekleyen.
Daha sonra bu listeyi Buyukten Kucuge Dogru Siralayan, Sonrasinda da ekrana yazdiran programi yaziniz.
'''

# Çözüm 1
yas1 = int(input("1. Kişinin yaşını girin: "))
yas2 = int(input("2. Kişinin yaşını girin: "))
yas3 = int(input("3. Kişinin yaşını girin: "))
yas4 = int(input("4. Kişinin yaşını girin: "))
yas5 = int(input("5. Kişinin yaşını girin: "))

liste = [yas1, yas2, yas3, yas4, yas5]
liste.sort()
liste.reverse()

print(f"Liste: {liste}")

#########################################################################################

# Soru 2
'''
2-) 3 Farkli küpün uzunluklarını alıp bunları bir listeden tutan ve bu küplerin alanlarını ve hacimlerini ayrı ayrı
hesaplayarak ekrana yazdıran programı yazınız.
'''

# Çözüm 2
kup1 = float(input("1. Küpün kenar uzunluğunu giriniz: "))
kup2 = float(input("2. Küpün kenar uzunluğunu giriniz: "))
kup3 = float(input("3. Küpün kenar uzunluğunu giriniz: "))

alan1 = 6 * kup1 ** 2
alan2 = 6 * kup2 ** 2
alan3 = 6 * kup3 ** 2

hacim1 = kup1 ** 3
hacim2 = kup2 ** 3
hacim3 = kup3 ** 3

print("\nKÜP 1:\n")
print(f"1. Küpün Alanı: {alan1}\n1. Küpün Hacmi: {hacim1}")

print("\nKÜP 2:\n")
print(f"2. Küpün Alanı: {alan2}\n2. Küpün Hacmi: {hacim2}")

print("\nKÜP 3:\n")
print(f"3. Küpün Alanı: {alan3}\n3. Küpün Hacmi: {hacim3}")

#########################################################################################

# Soru 3
'''
3-) Bir öğrencinini 5 adet sınav notunu listede tutan. Daha sonrasında bu öğrencinin adını ve soyadını alarak listenin en
başına ekleyen ve öğrencinin not ortalamasını hesaplayarak adı ve soyadı ile birlikte kullanıcı dostu olarak ekrana
yazdıran programı yazınız.
'''

# Çözüm 3
not1 = float(input("1. Sınav notunu giriniz: "))
not2 = float(input("2. Sınav notunu giriniz: "))
not3 = float(input("3. Sınav notunu giriniz: "))
not4 = float(input("4. Sınav notunu giriniz: "))
not5 = float(input("5. Sınav notunu giriniz: "))

liste = [not1, not2, not3, not4, not5]

ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")

liste.insert(0, ad)
liste.insert(0, soyad)

ortalama = (not1 + not2 + not3 + not4 + not5) / 5

print(f"{ad} {soyad} adlı kişinin ortalaması: {ortalama}")

#########################################################################################

# Soru 4
'''
4-) Kullanıcıdan 8 adet sayı alıp bir listede tutan ve bu listenin ortanca elemanını bulup ekrana kullanıcı dostu bir
şekilde yazdıran programı yazınız.
'''

# Çözüm 4
sayi1 = float(input("1. Sayıyı giriniz: "))
sayi2 = float(input("2. Sayıyı giriniz: "))
sayi3 = float(input("3. Sayıyı giriniz: "))
sayi4 = float(input("4. Sayıyı giriniz: "))
sayi5 = float(input("5. Sayıyı giriniz: "))
sayi6 = float(input("6. Sayıyı giriniz: "))
sayi7 = float(input("7. Sayıyı giriniz: "))
sayi8 = float(input("8. Sayıyı giriniz: "))

liste = [sayi1, sayi2, sayi3, sayi4, sayi5, sayi6, sayi7, sayi8]

ortanca = (sayi4 + sayi5) / 2

print(f"Ortanca eleman: {ortanca}")

#########################################################################################

# Soru 5
'''
5-) 1010 1010 2 lik tabandaki sayısının 10 luk tabandaki karşılığı nedir? L1 ve L2 cache nedir?
'''

# Çözüm 5
x = 2 ** 1 + 2 ** 3 + 2 ** 5 + 2 ** 7
print(f"1010 1010 2 lik tabandaki sayının 10 luk tabandaki karşılığı: {x}")

print("L1 VE L2 CACHE (ÖNBELLEK) NEDİR?")
print('''
L2 (Seviye 2) önbellek, L1 önbellekten daha yavaş, ancak daha büyük boyuttadır. Yeni, güçlü CPU'lar geçme eğiliminde olsa da, boyutları genellikle 256 KB ile 8 MB arasında değişiyor. L2 önbellek, sonraki CPU tarafından erişilmesi muhtemel verileri tutar.
''')
#########################################################################################
