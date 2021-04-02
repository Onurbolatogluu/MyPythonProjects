import sys
import os # Dosya açma ve Dosya kaydetmek için os modülümüzü dahil etmemiz gerekiyor.
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QAction, qApp, QMainWindow



class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("Clear Area")
        self.ac = QPushButton("Open File")
        self.kaydet = QPushButton("Save File")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazialani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Notepad")

        self.temizle.clicked.connect(self.yazitemizle)
        self.ac.clicked.connect(self.dosyaac)
        self.kaydet.clicked.connect(self.dosyakaydet)

    def yazitemizle(self):
        self.yazialani.clear()

    def dosyaac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        with open(dosya_ismi[0],"r") as file:
            self.yazialani.setText(file.read())


    def dosyakaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazialani.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad() # Notepad sınıfından pencere adında bir obje oluşturduk ve bunu menü sınıfının altında yaptık.
        self.setCentralWidget(self.pencere) # Pencere objemizi Menu objemizin ortasına widget olarak ekledik.
        self.menuleriolustur()

    def menuleriolustur(self):
        menu = self.menuBar()
        dosya = menu.addMenu("File")
        dosyaac = QAction("Open File",self)
        dosyaac.setShortcut("Ctrl+O")
        dosyakaydet = QAction("Save File",self)
        dosyakaydet.setShortcut("Ctrl+S")
        temizle = QAction("Clear File",self)
        temizle.setShortcut("Ctrl+D")
        cikis = QAction("Quit",self)
        cikis.setShortcut("Ctrl + Q")

        dosya.addAction(dosyaac)
        dosya.addAction(dosyakaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)


        self.setWindowTitle("Notepad Plus")
        self.show()

    def response(self,action):
        if action.text() == "Open File":
            self.pencere.dosyaac() # Bu fonksiyonların zaten Notepad sınıfında tanımladık. Tekrar tekrar yazmak yerine o sınıfın fonksiyonlarını çağırabiliriz. Pencere objemiz Notepadd sınıfından türediği için. Pencere Objemiz üzerinden fonksiyonları çağırıyoruz.
        elif action.text() == "Save File":
            self.pencere.dosyakaydet()
        elif action.text() == "Clear File":
            self.pencere.yazitemizle()
        elif action.text() == "Quit":
            qApp.quit()

app = QApplication(sys.argv)

Menuapps = Menu()

sys.exit(app.exec_())
