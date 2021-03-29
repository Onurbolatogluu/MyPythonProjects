import sys 
# Eğer PyQt5 kodumuzu komut satırından çalıştırırsak, sys modülüne argümanlar vereceğiz ve bu da bizim uygulamamızı oluşturacak.

from PyQt5 import QtWidgets

def Pencere(): # Pencere fonksiyonu oluşturuyoruz.

    app = QtWidgets.QApplication(sys.argv)
# Qapplication sınıfını kullanarak app objesi oluşturuyoruz.


    pencere = QtWidgets.QWidget()
# qwidget sınıfından pencere objesi oluşturuyoruz.

    pencere.setWindowTitle("PyQt5 Ders 3")
# pencere objemize setwindowtitle ile başlık giriyoruz.

    buton = QtWidgets.QPushButton(pencere) 
# QPushButton sınıfından buton objesi oluşturup, bunu pencere objesine bağlıyorum(ekliyorum).

    buton.setText("Burası bir butondur.")
# buton objemize isim veriyoruz. Buton üzerinde gözükecek.

    etiket = QtWidgets.QLabel(pencere)
# Qlabel sınıfından etiket objesi oluşturuyoruz. penceremize bağlıyorum. (Penceremize yazı eklemek için)


    etiket.setText("Merhaba Dünya")
# etiket objemize yazı ekliyoruz.

    etiket.move(200,30)
# move ile etiket objemizin pencere üzerinde yerini güncelliyoruz.

    buton.move(190,80)
# move ile buton objemizi penceremiz üzerinde yerini güncelliyoruz.



    pencere.setGeometry(100,100,500,500)
# pencere objemizi masaüstünde açılacak olan yerini ve büyüklüğünü değiştiriyoruz.

    pencere.show()

    sys.exit(app.exec_())


Pencere()


