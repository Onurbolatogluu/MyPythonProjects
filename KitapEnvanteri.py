import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

imlec = con.cursor() # imlec isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
# İmleç oluşturmak için cursor() adlı bir metottan yararlanacağız.

def tablo_oluştur():
    # Sorguyu çalıştırıyoruz.
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
    # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
    con.commit()


def deger_ekle():
    imlec.execute("INSERT INTO kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',261)")
    con.commit()

def kitap_bilgisi_gir(isim,yazar,yayinevi,sayfasayisi):
    imlec.execute("INSERT INTO kitaplık VALUES(?,?,?,?)", (isim,yazar,yayinevi,sayfasayisi))
    print("Kayit Girildi...")
    con.commit()
# ? işaretlerinin herbirinin yerine fonksiyona değer olarak gönderdiğimiz isim , yazar, yayıevi ve sayfa sayısı bilgileri gidiyor ve tablomuza bu şekilde veri ekleyebiliyoruz.

isim = input("İsim:")
yazar = input("Yazar:")
yayinevi = input("Yayın Evi:")
sayfasayisi = int(input("Sayfa Sayısı:"))

kitap_bilgisi_gir(isim,yazar,yayinevi,sayfasayisi)



#deger_ekle()
#tablo_oluştur()

con.close() # Bağlantıyı koparıyoruz.
