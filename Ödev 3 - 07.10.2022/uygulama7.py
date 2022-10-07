# Mevlüt Çelik
# 07.10.2022
# Kullanıcıdan Adını soyadını, yaşını alıp, Kişinin evlenebileceği kişinin maksimum yaşını 2x-20  denklemine göre hesaplayan programı yazınız. (x = kişinin kendi yaşı)


adsoyad = input("Adınızı ve Soyadınızı giriniz: ")
yas = int(input("Yaşınızı giriniz: "))


evlenecegiMaxYas = str(2 * yas - 20)


print("Sn. " + adsoyad + " evlenebileceğiniz kişinin maksimum yaşı: " + evlenecegiMaxYas)