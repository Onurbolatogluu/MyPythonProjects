def not_hesapla(satır):
    # Fonksiyon oluşturduk ve bu fonksiyon içerisine her bir satırı göndereceğiz.
    satır = satır[:-1]
    # Dosyamızın içerisinde bulunan satırların her birinin sonunda print işlemi gereğince varsayılan olarak \n karakteri var.
    # Durum böyle olunca satırlarımızın sonunda bir boşluk oluşuyor. Bunun önüne geçmek adına biz satırın tamamını almak yerine,
    # Son karakteri almadan devam ediyoruz yani \n karakterini almıyoruz. ve bunu da tekrar satır değişkenine atıyoruz.

    liste = satır.split(",")
# Dosyamızın içerisinde bulunan isim ile notları ayrı ayrı alıp kullanacağız.
# split fonksiyonumuza (,) vererek isim ve notları ayrı ayrı alabilmek için parçalıyoruz. ve her bir elemanı ayrı ayrı aynı listeye atayacak.
# Yani dosyamızın içerisnde bulunan (,) değerlerine split ile (,) göndererek parçalıyoruz. Dosyamızın içerisinde bulunan (,) işareti (,)le göre ayrıştırıyoruz.
# Yani isimleri ve sınav notlarını teker teker alabiliriz.
    isim = liste[0]
# Dosya içerisinde bulunan değerleri ayrı ayrı almayı yukarıda split ile yaptık. Split bize her bir(,) ile ayrılmış değerleri
# String olarak ayrıştırdı. Dosyamızın her bir satırında bulunan 0'ıncı elemanı isimlerin bulunduğu yerdir.
# Böylelikle biz liste değişkenin 0'ıncı elamınlarına gidip isimleri alıyoruz ve bunları isim değişkenine kaydediyoruz.
    not1 = int(liste[1])
# Satırların(dosyamızın) içerisinde bulunan 1'inci elemanı not1 değişkenine kaydettik.
# (Dosyamızı fonksiyon bloğumuz içerisinde liste değişkenine atadık)(yukarıda)
    not2 = int(liste[2])
# Satırların(dosyamızın) içerisinde bulunan 2'inci elemanı not2 değişkenine kaydettik.
# (Dosyamızı fonksiyon bloğumuz içerisinde liste değişkenine atadık)(yukarıda)
    not3 = int(liste[3])
# Satırların(dosyamızın) içerisinde bulunan 3'uncu elemanı not3 değişkenine kaydettik.
# (Dosyamızı fonksiyon bloğumuz içerisinde liste değişkenine atadık)(yukarıda)

# 4 DEĞERİMİZİ DE YUKARIDA ALMIŞ OLDUK, İSİM,NOT1,NOT2,NOT3

    son_not = (not1*(0.3)+not2*(0.3)+not3*(0.4))
# Notlarımızı ayrı ayrı alıp değişkenlere atadığımıza göre harf notu hesaplayabiliriz.
# Not1'in %30u son notumuza etki etmesi için (not1 * (3/10 ifadesini kullandık.))
# Not2'mizin %30u, Not3ün %40ının etki etmesini istedik ve yukarıdaki işlemlerin sonucunu son_not değişkenine atadık.
    if (son_not >= 90):
        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"
# Notları son_not değişkenimize göre koşul ile kontrol ediyoruz.

    return isim + "------------------> " + harf + "\n"
# Fonksiyonumuzun işlemler sonucunda döneceği değeri burada belirtiyoruz.
# Hem isim hem de az önce kontroller sonucunda elde ettiğimiz harf değişkenlerimizi koşullara göre return ile dönüyoruz.
# Bunu yaptığımızda her bir satırımızın değerini bulmuş olacağız. ve bu değeri return ile dönmüş olacağız.
# \n ile satırlar arası boşluk bırakmak için kullanıyoruz.


with open("C://Users/sanal/VSCode-WorkSpace/WorkSpace-5/ilk-proje/dosya.txt", "r", encoding="utf-8") as file:
    # Türkçe karakterler bulundurduğu için utf-8'i kullanacağız ve dosyayı okuyacağımız için "r" parametresini kullanıyoruz.
    eklenecekler_listesi = []
# Eklenecekler Listesini boş olarak oluşturuyoruz ve aşağıda fonksiyon çalıştığında dönen değerleri bu listeye "append" yönetim ile tek tek ekliyoruz.
# Yani not_hesapla fonksiyonumuzdan dönen her bir değeri bu listeye ekleyeceğiz.
    for i in file:
        # Dosyamızın içersinde bulunan her satırı fonksiyona göndermek için döngümüzü başlatıyoruz.
        # Yani dosyamızın içerisinde bulunan her bir satırı ben bu for döngüsüyle okumak istediğimi söylüyorum.
        eklenecekler_listesi.append(not_hesapla(i))
# Daha sonra not hesapla fonksiyonuna ben (i) değerimi göndereceğim.
# Böyle bir işlem yaptığımızda dosyamızda bulunan her satırı fonksiyonumuza göndermiş oluyoruz.
# Her döngüde dönen değeri burada eklenecekler_listesine her bir satırı göndermiş oluyoruz ve o satıra karşılık gelen her bir değeri burada listeye atmış oluyoruz.
    with open("notlar.txt", "w", encoding="utf-8") as file2:
        # Bu listenin içerisinde bulunan her bir elamanı notlar.txt dosyasına yazmak istersek. Yeni bir dosya oluşturuyoruz ve "w" parametresi ile oluşturuyoruz.
        # Ve bu dosyamızı döngüde kullanabilmek için file2 değişkenine atıyoruz.
        for i in eklenecekler_listesi:
            file2.write(i)
# Dosyamızın her bir satırını eklenecekler_listesi elamanını eklemek istiyoruz.. Bu yüzden..
# For döngüsü ile eklenecekler listesi üzerinde "i" değeri ile geziniyoruz. ve (i) değerimizi (yani dosyamızın içerisindeki her satırı)
# File2 değişkenimize (i)mizin içindeki her bir elemanı .write parametresi ile yazıyoruz.
with open("KursNotlari", "w", encoding="utf-8") as file3:
    for i in eklenecekler_listesi:
        file3.write(i)
