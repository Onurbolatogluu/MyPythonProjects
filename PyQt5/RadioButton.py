import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout

# Radio Button, bize sunulan birden fazla seçenekten birini seçmemize imkan tanıyor. 

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radioyazi = QLabel("Hangi Dili Seviyorsun?")
        self.javabutonu = QRadioButton("Java")
        self.pythonbutonu = QRadioButton("Python")
        self.phpbutonu = QRadioButton("PHP")
        self.yazialani = QLabel("")
        self.buton = QPushButton("Cevabı Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radioyazi)
        v_box.addWidget(self.javabutonu)
        v_box.addWidget(self.pythonbutonu)
        v_box.addWidget(self.phpbutonu)
        v_box.addStretch()
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.buton.clicked.connect(lambda: self.click(self.javabutonu.isChecked(),self.pythonbutonu.isChecked(),self.phpbutonu.isChecked(),self.yazialani))


        self.setWindowTitle("Çoktan Seçmeli")
        self.show()

    def click(self,javabutonu,pythonbutonu,phpbutonu,yazialani):
        if javabutonu:
            yazialani.setText("JAVA Seçildi.")
        if pythonbutonu:
            yazialani.setText("PYTHON Seçildi.")
        if phpbutonu:
            yazialani.setText("PHP Seçildi.")


app = QApplication(sys.argv)

penceremiz = Pencere()

sys.exit(app.exec_())
