# Mevlüt Çelik - 28.09.2022
# Kullanıcıdan yarıçap bilgisini alıp dairenin alanını ve çemberini hesaplayan program

PI = 3.14
r = float(input("Yarıçapı giriniz...:"))

alan = PI * (r ** 2)
cevre = 2 * PI * r


print("Alan: " + str(alan))
print("Çevre: " + str(cevre))