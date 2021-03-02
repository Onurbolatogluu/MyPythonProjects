import time
import random
print("""****************************

Sayı Tahmin Oyununa Hoşgeldiniz

1 ile 10 arasında(1 ve 10 dahil) rastgele tahmin edin.
****************************""")
tahmin_hakkı = 7
rastgele_sayı = random.randint(1, 10)

while True:
    tahmin = int(input("Tahmininiz:"))

    if (tahmin == rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler!")
        print("Sayı", rastgele_sayı)
        break
    elif(tahmin < rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:", tahmin_hakkı)
    else:
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:", tahmin_hakkı)
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti. Üzgünüz")
        print("Sayımız:", rastgele_sayı)
        break

# 1,2 satırlarda uygulamada kullanacağımız modülleri kodumuza import ettik.
# 9 satırda uygulamamıza tahmin hakkı tanımladık. tahmin hakkı bitince while döngüsünü durduracağız.
# 10.satırda random.randint fonksiyonu sayesinde 1 ile 10(bu sayi aralığı değişebilir elbette) arasında rastgele sayı üretiyoruz.
# 15.satırda her while döngüsünün başında tahmin almak istiyoruz ve bunu integer olarak istediğimizi belirtiyoruz. Ardından kullanıcının verdiği tahmini tahmin değişkenine atıyoruz.
# Örnek olarak 21. satırdan 26 satıra kadar kodun açıklaması şöyle..
# 1-tahmin rastgele sayımızdan büyükse, ekrana bilgiler sorgulanıyor yazdır. time modulü sayesinde 1 saniye beklet. ardından tahmin ile rastgele sayı uyuşmadığı için,
# tahmin hakkı değişkenimizden yani tahmin hakkımızdan -1 düşür. ve ekrena daha yüksek bir sayı söyleyin yazısı ve kalan tahmin hakkını bastıralım.
# 28 satırdan 32 ye kadar da yukarıdaki işlemlerin aynısını kontrol ediyoruz olarak düşünebilirsiniz tek fark bu sefer kullanıcı rastgele sayıdan daha yüksek sayı söylerse. bu koşul çalışacak.
# 33 satırdan 36 ya kadar da kullanıcının tahmin hakkı 0'a eşitse yani kalmamışsa while döngüsünü break ile durduruyoruz.
# 15 ile 20 satır arasında ise rastgele sayı ile kullanıcıdan alınan sayı değeri eşitse. ekrana tebrikler yazdırıp yine break ile kodu sonlandırıyoruz.
