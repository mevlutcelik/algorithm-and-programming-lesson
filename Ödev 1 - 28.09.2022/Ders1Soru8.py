# Mevlüt Çelik - 29.09.2022
# Kullanıcıdan bir kenar verisini alıp tek satırda küpün hacmini ve alanını hesaplayan programı yazdım


# Tek satır yazmamızı söylemişsiniz hocam fakat tek satırda değişken kullanmadan yapamıyoruz. Bu yüzden değişken alıp işlemi tek satırda yaptım
# print("Hacim: " + str(float(input("Kenar uzunluğunu giriniz...:"))**3))


kenar = float(input("Kenar uzunluğunu giriniz...:"))

print("Hacim: " + str(kenar ** 3) + "\nAlan: " + str(6 * (kenar ** 2)))