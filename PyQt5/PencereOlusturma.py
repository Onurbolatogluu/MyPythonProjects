import sys # Eğer PyQt5 kodumuzu komut satırından çalıştırırsak, sys modülüne argümanlar vereceğiz ve bu da bizim uygulamamızı oluşturacak.
import os # Kodumuza görsel ekleyeceğimiz için, görselin bulunduğu dizini geçebilmemiz için os modülünden yararlanacağız.
from PyQt5 import QtWidgets,QtGui # qtwidgets bizim pencere ve butonlar yapmamıza yardımcı olan bir modüldür. qtgui ile uygulamamıza görsel yüklemek için ekliyoruz.

def Pencere(): # Fonskiyon oluşturuyoruz ve pencere ismini veriyoruz.


    os.chdir("C:\\Users\\sanal\\VSCode-WorkSpace\\WorkSpace-5\\PyQt5-Egitimi") 
# Görselimizin bulunduğu dizini belirtiyoruz.   

    app = QtWidgets.QApplication(sys.argv) 
# app adında bir obje oluşturuyoruz. qtwidgets içerisinde qApplication sınıfından obje oluşturmak istediğimizi belirtiyoruz.
# sys.argv ile komut satırından çalıştırdığımız da alacağı argümanları gönderiyoruz.
# Yani sys.argv ile komut satırından çalıştırdığımız da argüman gönderirsek göndereceğimiz argümanın buraya gelmesini söylüyoruz.

    pencere = QtWidgets.QWidget()
# pencere objesi oluşturuyoruz ve bunu qwidget sınıfından oluşturmak istediğimizi söylüyoruz.

    pencere.setWindowTitle("PyQt5 Ders 1")
# pencere objemize setwindowstle ile başlık giriyoruz.

    etiket_1 = QtWidgets.QLabel(pencere)
# QtWidgets.Qlabel sınıfından etiket_1 objesi oluşturuyoruz. Yazı ekleyebilmemiz için böyle bir obje oluşturduk.
# Ekleyeceğimiz yazıyı (yani etiket_1 objemizi) pencere objemiz üzerine yerleştirmemiz gerekiyor. Bu yüzden QLabel içerisine pencere objemizi gönderiyoruz.
# Böylelikle etiket_1 objemiz pencere objemize yapışmış olacak.

    etiket_1.setText ("Burası pencere objesinin ilk yazısıdır.")
# Etiket_1 objemize yazı ekliyoruz.

    etiket_1.move(150,30)
# Yazdığımız yazının pencere üzerindeki yerini değiştirdik.

    etiket_2 = QtWidgets.QLabel(pencere)
# etiket_2 objemizi oluşturduk ve bunuda QLabel sınıfından oluşturduk. Argüman olarak pencere objemizi verdik ve pencere objemize yapışmasını istedik.
# etiket_2 sınıfı ile birlikte penceremize yazı değil görsel ekleyeceğiz.

    etiket_2.setPixmap(QtGui.QPixmap("photo.jpg"))
# setpixmap ile etiket_2 objemize python.png görselini ekledik.
# qtgui içerisinde qpixmap sınıfını kullanarak "python.png" görselini içine al ve setpixmap ile görsel oluştur diyoruz.

    etiket_2.move(80,100)
# Görselimizin pencere objesi üzerindeki yerini move parametresi ile güncelledik.


    pencere.setGeometry(100,100,500,500) 
# Penceremizi başlattığımızda hangi büyüklükte ve ekranın ne kadarını kaplayacağını belirtiyoruz.
# 500-500 Pencerenin büyüklüğü.
# 100-100 Bilgisar ekranımızda nerede olacak bunu belirtiyoruz.


    pencere.show()
# pencere.show ile objemizi açıyoruz. Bellekte bir pencere oluşturulur ve daha sonra ekranda gösterilir.

    sys.exit(app.exec_())
# Uygulamamızı çalıştırdıktan sonra, sürekli çalışması için döngüye sokmamız gerekiyor.
# Biz bilerek ve isteyerek uygulamamızı kapatmadığımız sürece uygulamamızı sürekli çalışır durumda bırakıyor.


Pencere()


