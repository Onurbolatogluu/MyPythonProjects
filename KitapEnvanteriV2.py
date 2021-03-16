import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

imlec = con.cursor() # imlec isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
# İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız.

############################################################################################


def tablo_oluştur():
    # Sorguyu çalıştırıyoruz.
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
    con.commit()

############################################################################################


def deger_ekle():
    imlec.execute("INSERT INTO kitaplık VALUES('İstanbul','Ahmet Candan','Kukla',2261)")
    con.commit()


############################################################################################



def kitap_bilgisi_gir(isim,yazar,yayinevi,sayfasayisi):
    imlec.execute("INSERT INTO kitaplık VALUES(?,?,?,?)", (isim,yazar,yayinevi,sayfasayisi))
    print("Kayit Girildi...")
    con.commit()
# ? işaretlerinin herbirinin yerine fonksiyona değer olarak gönderdiğimiz isim , yazar, yayıevi ve sayfa sayısı bilgileri gidiyor ve tablomuza bu şekilde veri ekleyebiliyoruz.

#isim = input("İsim:")
#yazar = input("Yazar:")
#yayinevi = input("Yayın Evi:")
#sayfasayisi = int(input("Sayfa Sayısı:"))


############################################################################################


def verileri_al():
    imlec.execute("Select * From kitaplık")  # Bütün bilgileri alıyoruz.
    # Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    data = imlec.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
    # con.commit() işlemine gerek yok. Çünkü tabloda herhangi bir güncelleme yapmıyoruz.



############################################################################################


def verileri_al_2():
    # Sadece İsim ve Yazar özelliklerini alıyoruz.
    imlec.execute("Select İsim,Yazar From kitaplık")
    data1 = imlec.fetchall()
    print("Tablo Aranıyor.....")
    for i in data1:
        print(i)


############################################################################################


def verileri_al_3(yayınevi):
    # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    imlec.execute("Select * From kitaplık where Yayınevi = ?", (yayınevi,))
    data2 = imlec.fetchall()
    print("Tablo Aranıyor.....")
    for i in data2:
        print(i)


############################################################################################


def verigüncelle(yayınevi):
    imlec.execute(
        "Update kitaplık set Yayınevi = ? where Yayınevi =  ?", ("Everest", yayınevi))
    con.commit()


############################################################################################


def verigüncelle_2(eskiyayinevi,yeniyayinevi):
    imlec.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeniyayinevi,eskiyayinevi))
    print("Güncelleme Yapılmıştır.. Yeni Yayın Evi {} olarak ayarlanmıştır.".format(yeniyayinevi))
    con.commit()


############################################################################################


def verilerisil(yazar):
    imlec.execute("Delete From kitaplık where Yazar = ?", (yazar,))
    print("Kitaplık Tablosu içerisinde bulunan,Yazarı {} olan veriler başarılı bir şekilde silinmiştir...".format(yazar))
    con.commit()


############################################################################################
######## Fonksiyon Çalıştırma Bloğu ########################################################

#verilerisil("Ahmet Candan")
#verigüncelle_2("At Kitapevi","Huzur Kitap")
#verigüncelle("Meyhane")
#verileri_al_3("Everest")
#verileri_al_2()
#verileri_al()
#deger_ekle()
#tablo_oluştur()
#kitap_bilgisi_gir(isim, yazar, yayinevi, sayfasayisi)

con.close() # Bağlantıyı koparıyoruz.

# Select * From kitaplık - Tablodaki tüm bilgileri almamızı sağlar.

# Select İsim, Yazar From kitaplık Tablodaki tüm bilgileri sadece İsim ve Yazar özelliklerini almamızı sağlar.

# Select * From kitaplık where Yayınevi = 'Everest' Sadece Yayınevi özelliği Everest olanları alır.

# Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap' -- Yayınevi 'Doğan Kitap' olan kitapların Yayınevi bilgilerini 'Everest' e günceller.

# Delete From kitaplık where Yazar = 'Ahmet Ümit' -- Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.
