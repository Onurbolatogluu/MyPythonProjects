import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  #QWidget'da tanımlı olan init fonksiyonundan miras alıyoruz.
        self.init_ui()  # __init__ fonskiyonu, fonksiyonumuz otomatik olarak çalıştığı için, kendimiz ek özellikler eklediğimiz,
                        # __init__ui özelliğimizi __init__ fonksiyonunun altına giriyoruz, çünkü bizim eklediğimiz özelliklerin de,
                        # fonskiyon çalışmaya başladığında otomatik olarak çalışmasını istiyoruz.
    def init_ui(self): #Yukarıda __init__ çalıştığında çalışmasını istediğimiz özelliğimizi init fonksiyonun altına girmiştik(self.__init_ui).
                        # otomatik olarak çalışması için, bu çalışmasını istediğimiz özelliğimizin ne iş yapacağını, neleri tanımlayacağımızı burada fonksiyon yazarak belirtiyoruz.
        self.yazi_alani = QtWidgets.QLineEdit() # Üzerine yazı yazabildiğimiz bir obje oluşturuyoruz.
        self.temizle = QtWidgets.QPushButton("Temizle") # Yeni bir buton objesi oluşturuyoruz.
        self.yazdir = QtWidgets.QPushButton("Yazdır")

        v_box = QtWidgets.QVBoxLayout() # Vertical bir obje oluşturuyoruz içerisine objelerimizi göndereceğiz.
        v_box.addWidget(self.yazi_alani) #Yazı alanımızı ekliyoruz.
        v_box.addWidget(self.temizle) # Temizle objemizi ekliyoruz.
        v_box.addWidget(self.yazdir) # Yazdır butonumuzu ekliyoruz.
        v_box.addStretch()

        self.setLayout(v_box) #Penceremize v_box objemizi ekliyoruz.

        self.temizle.clicked.connect(self.click) #temizle butonuna tıklandığında self.click fonksiyonumuz çalışacak.
        self.yazdir.clicked.connect(self.click) # yazdir butonuna tıklandığında self.click fonksiyonu çalışcak.


        self.show() #Penceremizi ekranda gösteriyoruz.
    
    def click(self):
        sender = self.sender() # qtwidgets içerisinde bulunan sender fonksiyonu ile hangi butona basıldığını tespit edebiliriz.

        if sender.text() == "Temizle": #Temizle butonuna basılmışsa..
            self.yazi_alani.clear() # Yazi alanini temizliyoruz.

        else:
            print(self.yazi_alani.text()) # Temizle butonuna basılmamışsa, yaziyi gösteriyoruz.



app = QtWidgets.QApplication(sys.argv)

penceremiz = Pencere()

sys.exit(app.exec_())
