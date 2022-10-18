# Dizideki maksimum değere sahip elemanı alır
print(max(["a","h","ç","r","i"]))
print(max([3,653,6,8,78,22]))



# Dizideki minimum değere sahip elemanı alır
print(min(["a","h","ç","r","i"]))
print(min([3,653,6,8,78,22]))



# Dizi'de işlemler
arr = [1,2,5,6,8,10,5]



# Dizide eleman güncelleme
arr[5] = 23
print(arr)



# Dizinin sonuna eleman ekleme
arr.append(3)
print(arr)



# Dizinin istenen indexine eleman ekleme
arr.insert(3,98)
print(arr)



# Dizinin başına eleman ekleme
arr.insert(0, 18)
print(arr)



# Dizinin belirtilen indexindeki elemanı siler
arr.pop()
print(arr)


arr.pop(5)
print(arr)



# Dizideki belirtilen elemanı siler
arr.remove(98) #98 değerine sahip elemanı belirttik
print(arr)



# Dizideki elemanları ters çevirme
arr.reverse()
print(arr)



# Diziyi temizleme
#arr.clear()
#print(arr)
