websitesi = "https://www.btkakademi.gov.tr"
ders = "Yazılım hareketi kapsamında sadece size özel açılmış olan ders."

#1
print(" Hello World!  ".strip())


#2
newWebSitesi = websitesi.replace("https://www.","")
newWebSitesi = websitesi.replace(".gov.tr","")
print(newWebSitesi)



#3
print(ders.lower())


#4
print(websitesi.count("a"))



#5
if (websitesi[0:3] == "www") and (websitesi[len(websitesi):-3] == ".com"):
    print("websitesi değişkeni www ile başlayıp .com ile bitiyor")
else:
    print("websitesi değişkeni www ile başlayıp .com ile bitmiyor")



#6
if websitesi.find(".com") != -1:
    print("websitesi değişkeni içinde .com var")
else:
    print("websitesi değişkeni içinde .com yok")



#7
print(ders.isalpha())



#8
print("ICERIK".center(len("ICERIK")+50, "*"))



#9
print(ders.replace(" ", "--"))


#10
print("Herkese Merhaba".replace("Merhaba", "Günaydın"))


#11
print(ders.split())
