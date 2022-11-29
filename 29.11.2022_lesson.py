sayilar = [1,3,5,7,9,11,13,22]

print("Üçün katı olan sayılar: ")
for i in sayilar:
    if i % 3 == 0:
        print(i)


toplam = 0
for i in sayilar:
    toplam += i
print(f"Sayılar listesindeki sayıların toplamı: {toplam}")


for i in sayilar:
    if i % 2 == 1:
        print(f"{i} sayısının karesi: {i**2}")



sehirler = ["istanbul", "ankara", "izmir", "mus", "cankiri"]

for i in sehirler:
    if len(i) <= 5:
        print(i)


urunler = [
    {"isim": "sansung6", "price": "3000"},
    {"isim": "sansung7", "price": "4000"},
    {"isim": "sansung8", "price": "5000"},
    {"isim": "sansung9", "price": "6000"},
    {"isim": "sansung10", "price": "7000"}
]

urunlerToplami = 0
for i in urunler:
    urunlerToplami += int(i["price"])
    if int(i["price"]) <= 5000:
        print(i["isim"])
print(f"Ürünler listesindeki ürünlerin fiyatı toplamı: {urunlerToplami}")
