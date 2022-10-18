studentA = ["Yiğit", "Özdemir", 2010, [70,60,70]]
studentB = ["Bilge", "Özdemir", 1999, [80,80,70]]
studentC = ["Ali", "Özdemir", 1998, [80,70,90]]

yıl = 2022


print("ÖĞRENCİ BİLGİLERİ".center(len("ÖĞRENCİ BİLGİLERİ")+50, "*"))
print(f"Ad Soyad: {studentA[0]} {studentA[1]}")
print(f"Yaş: {yıl - studentA[2]}")
print(f"Not ortalaması: {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3}")
print("\n\n")


print("ÖĞRENCİ BİLGİLERİ".center(len("ÖĞRENCİ BİLGİLERİ")+50, "*"))
print(f"Ad Soyad: {studentB[0]} {studentB[1]}")
print(f"Yaş: {yıl - studentB[2]}")
print(f"Not ortalaması: {(studentB[3][0] + studentB[3][1] + studentB[3][2]) / 3}")
print("\n\n")


print("ÖĞRENCİ BİLGİLERİ".center(len("ÖĞRENCİ BİLGİLERİ")+50, "*"))
print(f"Ad Soyad: {studentC[0]} {studentC[1]}")
print(f"Yaş: {yıl - studentC[2]}")
print(f"Not ortalaması: {(studentC[3][0] + studentC[3][1] + studentC[3][2]) / 3}")
print("\n\n")
