# 1
print("\n\n")
a = int(input("Bir sayı girin: "))
if a > 0 and a < 100:
    print(f"{a} sayısı 0 ile 100 arasındadır.")
else:
    print(f"{a} sayısı 0 ile 100 arasında değildir.")


# 2
if a%2 == 0 and a >= 0:
    print(f"{a} sayısı pozitif çift sayıdır.")
else:
    print(f"{a} sayısı pozitif çift sayı değildir.")


# 3
print("\n\n")
email = input("E-posta adresinizi girin:")
password = input("Şifrenizi girin:")

if email == "admin@gmail.com" and password == "123456":
    print("Hoşgeldin admin")
else:
    print("E-posta veya şifre hatalı")


# 4
print("\n\n")
x = float(input("1. Sayıyı girin: "))
y = float(input("2. Sayıyı girin: "))
z = float(input("3. Sayıyı girin: "))

if x > y and x > z:
    print(f"Girdiğiniz sayılardan en büyüğü {x} dir")
elif y > x and y > z:
    print(f"Girdiğiniz sayılardan en büyüğü {y} dir")
else:
    print(f"Girdiğiniz sayılardan en büyüğü {z} dir")


# 5
print("\n\n")
adsoyad = input("Adınızı ve soyadınızı girin: ")
boy = float(input("Boyunuzu metre cinsinden girin: "))
kilo = float(input("Kilonuzu kilogram girin: "))

bki = kilo / boy ** 2

if bki >= 0 and bki <= 18.4:
    print(f"Tebrikler {adsoyad}. Zayıfsın 🎉 -> {bki}")
elif bki >= 18.5 and bki <= 24.9:
    print(f"Tebrikler {adsoyad}. Gayet normalsin ✨ -> {bki}")
elif bki >= 25 and bki <= 29.9:
    print(f"{adsoyad} biraz fazla kilolusun ✨ -> {bki}")
else:
    print(f"{adsoyad} dikkat etmelisin. Obezsin!!! 💥 -> {bki}")


