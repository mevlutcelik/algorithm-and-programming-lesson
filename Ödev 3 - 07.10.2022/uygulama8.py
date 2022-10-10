# Mevlüt Çelik
# 07.10.2022
# ASCII tabloya göre klavyeden basılan 2 tuşunun 16 lık tabandaki karşılığı nedir?


# Klavye'den basılan 2 tuşunun karşılıkları:
# Decimal (10 luk taban) = 50
# Hexadecimal (16 lık taban) = 32
# Binary (2 lik taban) = 1100110
# Octal (8 lik taban) = 62
# Char (Karakter, Klavyede basılan tuş) = 2


sayi = input("Sayı giriniz: ")

hexadecimal = hex(int(ord(sayi)))

print("Girdiğiniz sayının 16 lık tabandaki karşılığı: " + str(hexadecimal))