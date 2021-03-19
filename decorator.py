# Ortalama fonksiyonumuza ek olarak decorator özellik ekliyoruz.
def ekstra(fonk):

    # Ortalamabul fonksiyonumuzda verdiğimiz sayılar buraya gelecek. Bu sayede istenilen sayıları bulabileceğiz.
    def wrapper(sayılar):
        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0
# Kodumuzda ihtiyacımız olan değişkenleri oluşturuyoruz.

        for sayı in sayılar:
            # sayıları sayı değişkeni üzerinde döngü olarak başlattık. sayılarımız çiftse çift sayılar değişkenine.
            # tekse tek sayılar değişkenine atayacağız.
            if (sayı % 2 == 0):  # sayımız çift mi? kontrol ediyoruz burada.
                # çiftler toplamına sayımız çift ise ekliyoruz.
                çiftler_toplamı += sayı
                # kaç adet çift sayı var bunu kontrol ediyoruz. eğer for döngümüzde o anki sayı çift ise +1 arttırıyoruz.
                çift_sayılar += 1

            else:  # Diğer durumlarda dogal olarak bu sayı tek sayıdır. O yüzden sayımız else duruma girerse. tek sayı ise eğer;
                # sayımızı tekler toplamına toplayarak ekliyoruz.
                tekler_toplamı += sayı
                # sayımız tek ise, tek sayılar değişkenimizi +1 arttırıyoruz.
                tek_sayılar += 1

# Bu sayede fonksiyona verdiğimiz sayı argümanlarının toplamlarını v.b öğrenmiş oluyoruz.

        # tekler toplamı ile tek sayıları bölerek ortalamayı buluyoruz.
        print("Teklerin Ortalaması:", tekler_toplamı / tek_sayılar)
        print("Çiftlerin Ortalaması:", çiftler_toplamı / çift_sayılar)

        fonk(sayılar)
        # fonk dediğimiz fonksiyon aslında aşağıda tanımladığımız ortalamabul fonksiyonumuz. extra fonksiyonuna fonk argümanına eşitlendi.
        # böylelikle ortalamabul fonksiyonumuzu çalıştırıyoruz.
        #   
        # wrapper fonksiyonumuz tamamlanmış oldu..

    return wrapper
# Decorator fonksiyonumuz içerisinden biz wrapper fonksiyonumuzu dönüyoruz.


@ekstra #Decorator fonksiyonumuzu ekliyoruz.
def ortalamabul(sayılar):

    # Sayı dizisindeki her bir sayıyı toplam dizisine ekleyeceğiz. daha sonra argüman olarak verdiğimiz sayıları toplam değişkenine böleceğiz.
    toplam = 0

    for sayı in sayılar:
        # Argüman olarak verdiğimiz sayıları burada toplamış ve toplam değişkenine atamış  olacağız.
        toplam += sayı
    print("Genel Ortalama:", toplam/len(sayılar))
# Toplam dizinindeki sayıları, verdiğimiz  argümanlara bölüyoruz.


ortalamabul([1, 2, 3, 4, 34, 60, 63, 32, 100, 105])
