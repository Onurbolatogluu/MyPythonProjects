import sys

from PyQt5 import QtWidgets

# Pencere sınıfımızın özellikleri Qwidget sınıfından miras almasını istiyoruz.
class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
# init fonksiyonumuzu Qwitgets ile aynı kullanmak istediğimiz için init fonksiyonumuzu miras aldık.
        super().__init__()
# Objemize self parametresi ile ek fonksiyon ekliyoruz.
        self.init_ui() 
# Objemize yukarıda eklediğimiz fonksiyonun tanımlarını giriyoruz(fonskiyonumuzu oluşturuyoruz).
    def init_ui(self):
        self.yazi_alani = QtWidgets.QLabel("Bana Henüz Tıklanmadı.") # Penceremize yazi eklemek için bir özellik tanımlıyoruz.
        self.buton = QtWidgets.QPushButton("Bana Tıkla.") # Penceremize buton eklemek için özellik tanımlıyoruz.
        self.say = 0 # Butona tıklamalarımızı sayması için bir özellik daha ekliyoruz.

# QBoxlayout sınıfından v_box objesini (buton) ve h_box objesini oluşturuyoruz ve özelliklerimizi bu objemize gönderiyoruz.
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()


        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

#Burada buton 'a tıklandığında ne olacağını söylüyoruz. Bizim Örneğimiz de connect özelliği ile self.click fonksiyonuna gidiyoruz.
#Bu fonksiyonu aşağıda tanımladık. Bu fonksiyon her çağrıldığında yani butona her bastıgımızda self.say özelliğimizi +1 arttırp,
# Yazı alanını objemizi setText ile güncelliyoruz.(Tıklama sayımızı yazıyoruz.)
        self.buton.clicked.connect(self.click) 

        self.setLayout(h_box)  # Penceremize butonlarımızı dahil ettik.
        self.show()  # Penceremizi gösteriyoruz.

    def click(self):
        self.say += 1
        self.yazi_alani.setText("Bana " + str(self.say) + " Defa Tıklandı.")


        


app = QtWidgets.QApplication(sys.argv)

penceremiz = Pencere()

sys.exit(app.exec_())
