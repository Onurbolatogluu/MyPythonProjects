import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout
# Kullanılacak modülleri projeye dahil ettik.


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("işaretleme Alanı")
        self.yazialani = QLabel("")
        self.buton = QPushButton("Tıklama Alanı")

        v_box = QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazialani))
# buton objesine tıklandıysa,
# İşaretleme alanının işaretlenip, işaretlenmediğini kontrol ediyoruz. 
# lambda sayesinde fonksiyon objesi haline getirdik satırımızı.
# Checkbox işaretlenmişse, true olacak, işaretlenmediyse false olacak.
        self.show()

    def click(self,checkbox,yazialani): # Fonksiyonumuz yukarıdaki 2 parametreyi(fonksiyon objesini) alıyor.
        if checkbox: # Checkbox işaretlenmişse, yani lambda fonskiyonu true değer döndüyse buradaki if durumuna girecek kodumuz.
            yazialani.setText("İşaretleme alanını başarıyla işaretledin.")
        
        else: # False durumunda kod bu bloğa girecek.
            yazialani.setText("İşaretleme alanını işaretlemedin kral.")

app = QApplication(sys.argv)

penceremiz = Pencere()

sys.exit(app.exec_())
