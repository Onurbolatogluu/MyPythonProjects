import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)
    okay = QtWidgets.QPushButton("Tamam") # okay adında bir buton oluşturuyoruz ve içerisine "Tamam" yazıyoruz.
    cancel = QtWidgets.QPushButton("İptal") # cancel adında bir buton oluşturuyoruz ve içerisine "İptal" yazıyoruz.

    # Butonlarımızı pencereye yerleştirmiyoruz. Layout'lara yerleştiriyoruz ve layoutları penceremize yerleştiriyoruz.

    h_box = QtWidgets.QHBoxLayout() # Objelerimizi yatay olarak yerleştirmemize imkan tanır.(objelerimizi dikey olarak ortalamış oluyoruz)

    h_box.addStretch() # Butonlarımızı pencerenin sağına sıfırladık.(bu fonksiyonu buton objelerinin neresinde kullanırsak obje o tarafa dogru ortalanır)
    h_box.addWidget(okay) # Objelerimizi layout'a tanımlıyouz.
    h_box.addWidget(cancel) # Objelerimizi layout'a tanımlıyoruz.


    v_box = QtWidgets.QVBoxLayout() # Objelerimizi dikey olarak yerleştirmemize imkan tanır.
    v_box.addStretch() # Objelerimizi sağ aşağıda tutmak istediğimiz için, layout'a objelerimizi eklemeden önce strectch ile v_box objemizi aşağıda olmasını söyledik. eğer, ekledikten sonra girseydik bu fonksiyonu, O zaman da ekranın yukarısında olacaktı objelerimiz.
    v_box.addLayout(h_box) # h_box objesini v_box objemize gönderdik. böylelikle iç içe kullanabiliriz.


    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setLayout(v_box) # Pencere objemize layoutlarımızı gönderdik.

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


Pencere()


