from PIL import Image,ImageFilter # Kullanılacak olan modülümüzü import ediyoruz. Bu modül sayesinde resimleri açabileceğiz ve değişik işlemler yapabileceğiz.
import os

os.chdir ("C:\\Users\\sanal\\VSCode-WorkSpace\\WorkSpace-5\\ikinci-proje") # Görsellerimizin bulunduğu dizine geliyoruz.

image = Image.open("kuş.jpg") # kuş.jpg dosyasını image.open fonskiyonunu kullanarak açıyoruz.

image.save("kuş2.jpg") # Görseli farklı bir isimle çoklayıp, farklı bir dosya haline getirebiliyoruz.

image.rotate(180).save("kuş3.jpg") # Görseli 180 derece döndürüp, görseli farklı olarak kaydediyoruz.


image.rotate(90).save("kuş4.jpg") # Görseli 90 derece döndürdük. ve kuş4 adında bir dosya oluşturduk.

image.convert(mode = "L").save("kuş5.jpg") # Görseli siyah-beyaz hale çevirip, .save ile bunu farklı bir dosya olarak kaydediyoruz.

degistir = (960,600) # Görseli kırpmak için, yeni boyutlarımızı belli bir demet haline getirmemiz gerekiyor.


image.thumbnail(degistir) # Görselimizin boyutlarını degistir değişkenine göre güncellemek istediğimizi burada söylüyoruz.

image.save("kuş6.jpg") # Başka bir isimle görselimizi kaydediyoruz.

image.filter(ImageFilter.GaussianBlur(10)).save("kuş8.jpg") # Görselimizi blur'lama işlemini yapıyoruz ve farklı bir görsel olarak kaydediyoruz.


kırpılacak_alan = (340,0,950,600) # Görselin kırpılacak olan alanını bir demet halinde bir değişkene tanımlıyoruz. (sol üst köşe - sağ alt köşe)


image2 = Image.open("atatürk.jpg") # Yeni görselimizi açıyoruz ve image2 değişkenine atıyoruz.
image2.crop(kırpılacak_alan).save("ataturk2.jpg") # crop fonksiyonu ile verdiğimiz ölçülere göre görselimizi kırpıyoruz ve farklı bir dosya olarak kaydediyoruz.


