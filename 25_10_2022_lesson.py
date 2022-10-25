sehirler = ["Mersin", "Muş", "Antalya"]
plakalar = [33,49,7]


print(plakalar[sehirler.index("Mersin")])


plakalar = { "key": "value" } # Key: anahtar, Value: değer


plakalar = {
    "Mersin"    : 33,
    "Muş"       : 49,
    "Antalya"   : 7
}

print(plakalar)
print(plakalar["Mersin"])


ID = {
    "tc"        : "11111111111",
    "adsoyad"   : "Mevlüt Çelik"
}

print(ID)





users = {
    "mevlüt" : {
        "yas"       : 19,
        "email"     : "mevlutcelik@eposta.com",
        "adres"     : "Mersin",
        "telefon"   : "+90 (555) 555 55 55"
    },
    "hava" : {
        "yas"       : 21,
        "email"     : "havaince@eposta.com",
        "adres"     : "Mersin",
        "telefon"   : "+90 (555) 555 66 66"
    }
}


print(users["mevlüt"])
print(users["mevlüt"]["telefon"])
