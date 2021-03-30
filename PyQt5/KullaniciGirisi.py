from sqlite3.dbapi2 import connect
import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()

        self.dbconnect()
        self.init_ui()

    def dbconnect(self): 
        connect = sqlite3.connect("userappdb.db") # Database oluşturuyoruz. (Mevcut da varsa ona bağlanacak..)
        self.imlec = connect.cursor() # Database üzerinde işlem yapabilmek için cursor fonskiyonu yardımıyla obje oluşturuyoruz.
        self.imlec.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")
        # Tablo ve tablo içerisinde 2 sutün oluşturuyoruz.
        connect.commit() # İşlemleri kaydediyoruz.

    def init_ui(self):
        self.kullaniciadi = QtWidgets.QLineEdit () # QlineEdit ile input alanı özelliğine sahip obje oluşturuyoruz.
        self.parola = QtWidgets.QLineEdit() # QlineEdit ile input alanı özelliğine sahip obje oluşturuyoruz.
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) # Yazılan parolayı kullanıcıya göstermiyoruz. (facebook da olduğu gibi örneğin)
        self.girisyap = QtWidgets.QPushButton("Giriş Yap") # Buton oluşturduk. 
        self.yazialani = QtWidgets.QLabel("") # Yazı alanı objemizi oluşturduk.
        self.kaydol = QtWidgets.QPushButton("kaydol")
        
# Objelerimizin penceremize yerleşim yerini belirtiyoruz.
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullaniciadi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazialani)
        v_box.addStretch() # Objelerimiz arası boşluk bırakıyoruz.
        v_box.addWidget(self.kaydol)
        v_box.addWidget(self.girisyap)

# Uygulamamızı penceremize ortalamak için sağı ve solunu boş bırakmamızı söylüyoruz.
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch() # Solu boş bırak.
        h_box.addLayout(v_box) # h_box objemize, v_box objemizi gönderiyoruz.
        h_box.addStretch() # Sağı boş bırak.


        self.setLayout(h_box) # Penceremize objelerimizi atıyoruz.
        self.setWindowTitle("User Login App") # Penceremize başlık giriyoruz.
        self.kaydol.clicked.connect(self.register)
        self.girisyap.clicked.connect(self.login) # Giriş yap butonuna tıklandığında self.login fonksiyonunu gideceğiz.
        self.show() # Pencereyi açıyoruz.

    def login(self):
        adi = self.kullaniciadi.text() # Kullanici Adi objesine girilen değeri adi değişkenine atıyoruz.
        passw = self.parola.text() # Parola objesine girilen değeri (yaziyi) passw değişkenine atıyoruz.
# Burada aldığımız 2 değeri db' üzerinde sorgulayacağız.
        self.imlec.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,passw)) 
        # Kullanıcıdan alınan değerler database üzerinde üyeler tablosunda mevcut mu? Bunu kontrol ediyoruz.
        # Mevcutsa değerlerimiz aşağıda liste halinde data değişkenine atamış olduk.
        # Mevcut değilse, listemiz boş dönecektir. Biz de kullanicinin girdiği değerleri liste boyunu if ile kontrol ederek tespit edebiliriz.
        data = self.imlec.fetchall() # Sorgudan dönen değerleri liste halinde alıyoruz.

        if len(data) == 0:
            self.yazialani.setText("Böyle Bir Kullanici Yok..\nLütfen Tekrar Deneyin.") # Liste boyu sıfırsa alınan değer yanlış demektir. Ve bunu kullaniciya belirtiyoruz.

        else:
            self.yazialani.setText(adi + " Hoşgeldiniz!")


    def register(self):
        adi = self.kullaniciadi.text()
        sifre = self.parola.text()
        
        if(len(adi) != 0 or len(sifre) != 0):
                connect = sqlite3.connect("userappdb.db")
                self.imlec = connect.cursor()
                self.imlec.execute("insert into üyeler values(?, ?)", (adi,sifre))
                connect.commit()
                self.yazialani.setText("kayıt işleminiz başarıyla gerçekleşti..")

        else:
                self.yazialani.setText("lütfen kullanici adi ve şifre girin")



app = QtWidgets.QApplication(sys.argv)

penceremiz = Pencere()

sys.exit(app.exec_())
