print("""****************
Bir sayının asal olup olmadığını bulma

Programdan çıkmak için 'q' ya basın.
****************
""")
#Fonsiyon Oluşuturma Alanı

def asal_mi(sayi):
    for i in range(2, sayi):
        if (sayi % i == 0):
            return False
    return True


#Koşulları Kontrol Etme Alanı

while True:
    yasaklı = "wertyuıopğüasdfghjklşizxcvbnmöç.,<>!'^%&()=?_-"

    sayi = input("Sayı:")

    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break

    elif sayi in yasaklı:
        print("Geçersiz İşlem")
        continue

    sayi = int(sayi)

    if (sayi == 1):
        print(sayi, "asal bir sayı değildir.")

    elif (sayi == 2):
        print(sayi, "asal bir sayıdır.")

    else:
        if (asal_mi(sayi)):
            print(sayi, "asal bir sayıdır.")
            
        else:
            print(sayi, "asal bir sayı değildir.")

# mesela sayi=5 girildi diyelim.

# python oncelikle if(asal_mi(sayi)): ifadesindeki asal_mi(5) kodunu gorur.
# asal_mi(5) ifadesi tanimli fonksiyona gider ve oradaki fonksiyon tanimina gore 5 sayisini sirasiyla 2, 3 ve 4 sayilarina boler.
# kalan herbirinde SIFIRdan farkli oldugundan o fonkisyondan return False satiri calisir.
# yani FALSE degeri doner.
# sonra if(asal_mi(sayi)): ifadesi if(false): haline gelir.
# bir if dongusu hep TRUE halinde calisir.
# biz if(false) elde ettigimizden bir alttaki satir olan else calisir.