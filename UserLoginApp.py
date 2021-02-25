print("**********\nKullanıcı Girişi\n**********\n")

kull_adi = "Onur"
kull_parola = "12345"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanici Adininizi Giriniz:")
    parola = input("Parolanızı Giriniz:")

    if (kullanici_adi != kull_adi and parola == kull_parola):
        print("Kullanıcı Adınız Hatalı.")
        giris_hakki -= 1
        print("Giriş Hakkı", giris_hakki)

    elif (kullanici_adi == kull_adi and parola != kull_parola):
        print("Parola Hatalı.")
        giris_hakki -= 1
        print("Giriş Hakkı", giris_hakki)

    elif (kullanici_adi != kull_adi and parola != kull_parola):
        print("Kullanıcı Adı ve Parola Hatalı.")
        giris_hakki -= 1
        print("Giriş Hakkı", giris_hakki)

    else:
        print("Başarıyla giriş yaptınız.")
        break

    if (giris_hakki == 0):
        print("Giriş Hakkınız Bitti.")
        break
