# Mevlüt Çelik - 28.09.2022
# Macbook ve Ayakkabı fiyatlarının KDV'li fiyatlarını hesapladım


macbook = 20465.06
ayakkabi = 700

kdv = 0.23


print("Normalde macbook fiyatı: " + str(macbook) + "₺")
print("KDV'li macbook fiyatı: " + str(macbook + (macbook * kdv)) + "₺")


print("############")


print("Normalde ayakkabı fiyatı: " + str(ayakkabi) + "₺")
print("KDV'li ayakkabı fiyatı: " + str(ayakkabi + (ayakkabi * kdv)) + "₺")