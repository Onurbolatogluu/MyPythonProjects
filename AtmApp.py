print("******************************\n\nKOPARAN BANK\nHoşgeldiniz\n\n******************************")


print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Çıkış yapmak için 'q' tuşuna basınız...

""")

Hesaplimiti = 5000

while True:
    işlem = input("işlemi Giriniz:")

    if (işlem == "q"):
        print("Sizi görmek güzeldi.")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {}'dır".format(Hesaplimiti))

    elif (işlem == "2"):
        tutar = int(input("Yatırmak istediğiniz tutarı:"))
        Hesaplimiti += tutar

    elif (işlem == "3"):
        tutar == int(input("Çekmek istediğiniz tutar:"))
        if (Hesaplimiti - tutar < 0):
            print("{} kadar bakiyeniz bulunmamaktadır.".format(tutar))
            print("Bakiyeniz {} TL".format(Hesaplimiti))
            continue
        Hesaplimiti -= tutar
        print ("Kalan Bakiye {} TL".format(Hesaplimiti))

    else:
        print("Geçersiz İşlem")
