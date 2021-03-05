import random
import msvcrt
import time


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        print("Kumanda Oluşturuluyor...")

        self.tv_ses = tv_ses
        self.tv_durum = tv_durum
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def sesi_azalt_artir(self):
        while True:
            karakter = input(
                "Azaltmak için '<' Artırmak İçin '>' Tamam ise 'q' ya basın:")
            if (karakter == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif (karakter == ">"):
                if (self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            elif (karakter == "q"):
                print("Çıkış Yapılıyor...")
                print("Ses:", self.tv_ses)
                break
            else:
                print("Geçersiz Tuş Kombinasyonu")
                break

    def tv_kapat(self):
        if (self.tv_durum == "Açık"):
            print("Tv Kapatılıyor.")
            time.sleep(3)
            self.tv_durum = "Kapalı" 
        
        else:
            (self.tv_durum == "Kapalı")
            print("Tv Zaten Kapalı Durumda")

    def tv_aç(self):
        if (self.tv_durum == "Kapalı"):
            print("Tv Açılıyor.\n")
            time.sleep(3)
            self.tv_durum = "Açık"

        else:
            (self.tv_durum == "Açık")
            print("Tv Zaten Açık Durumda.")

    def __str__(self):
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal:", self.kanal)

    def kanal_ekle(self, kanal):
        print("Kanal Eklendi ", kanal)
        self.kanal_listesi.append(kanal)


kumanda = Kumanda()
print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

Çıkmak için 'q' ya basın.

*******************""")
print(kumanda)

while True:
    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (işlem == "1"):
        kumanda.tv_aç()
        print(kumanda)
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        print(kumanda)
    elif (işlem == "4"):
        print("Kanal Sayısı: ", len(kumanda))
    elif (işlem == "5"):
        kanallar = input(
            "Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        kumanda.sesi_azalt_artir()
    else:
        print("Geçersiz İşlem...")
