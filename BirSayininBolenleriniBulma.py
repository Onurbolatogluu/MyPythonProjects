print("""****************
Bir sayının bölenlerini bulma

Programdan çıkmak için 'q' ya basın.
****************
""")

def bolenleri_bul(sayi):
    bolen_listesi = []
    for i in range(1,sayi+1): #Sayinin kendisini de for döngüsüne dahil etmek için +1 ekledik. eklemeseydik 99'a kadar sorgulayacaktı.
        if (sayi % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi

while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print(bolenleri_bul(sayi))

# Burada range(1, sayi+1) yaptık çünkü sayının 0’dan değil 1’den başlamasını ve sayi dahil sayi’ya kadar hesaplamasını istedik. 
# Eğer sayi+1 yerine sayi yazsaydık verdiğimiz sayiyi hesaplamayacktı. 
# X sayısı her zaman kendisinin bir tam böleni olduğu için bu sayi+1 şart değil.
