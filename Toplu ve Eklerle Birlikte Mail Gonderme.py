# Kullanıcı Bilgilerimi Dosyadan okumak için bu modülü ekliyorum.
from decouple import config
# Mail gönderme ve mail sunucusuna bağlanmak için bu modülü ekliyoruz.
import smtplib
from email.message import EmailMessage
import imghdr #Dosyamızın detaylarını tanımlamıza yarıyor.
import os

#Kullanıcı bilgilerinin bulunduğu değerleri çektik.

USER = config("USER")
PASS = config("KEY")

#Mail İçeriğini Oluşturduk

mesaj = EmailMessage()

kisiler = ["onur@onurbolatoglu.com","onrb@onurbolatoglu.com"]

mesaj["Subject"] = "Toplu Mail"
mesaj["From"] = USER
# mesaj["To"] = USER
mesaj["To"] = kisiler
mesaj.set_content("Toplu Mail içeriği..")

# Ek oluşturmak ve Maile dahil etmek. 

os.chdir("C:\\Users\\sanal\\VSCode-WorkSpace\\WorkSpace-5\\Kurcalamalar") #Ekimizin bulunduğu dizine geçiyoruz.

eklistesi = ["photo.jpg", "ob.jpg"] #Toplu ekleri bu şekilde listeye ekleyip for döngüsüne sokabiliriz.
for ekler in eklistesi:
    with open(ekler, "rb") as file: # Dosyamızı okuyoruz.
        image_name = file.name
        image_type = imghdr.what(file.name) #Maile eklemek istediğimiz ekin ismini gönderiyoruz.
        image_data = file.read()
# Ek özellikler tanımlıyoruz.
    mesaj.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)
#Ekimizi mailimize dahil ediyoruz.



#Farklı türde bir ek ekledik.

with open("test.py", "rb") as file2:  # Dosyamızı okuyoruz.
    file_name = file2.name
    # Maile eklemek istediğimiz ekin ismini gönderiyoruz.
    file_data = file2.read()
# Ek özellikler tanımlıyoruz.
mesaj.add_attachment(file_data, maintype="application",subtype="octet=stream", filename=file_name)
#Ekimizi mailimize dahil ediyoruz.





#SMTP ERİŞİMİ

mail = smtplib.SMTP("mail.onurbolatoglu.com", 587)
#smtplib.SMTP sınıfından obje oluşturup içerisinde smtp bilgisini ve port bilgisini yazıp bağlanıyoruz. ve bunu değişkene atıyorum.
mail.ehlo()
#Bağlanacağımız için ehlo parametresi gönderiyoruz.
mail.starttls()
#Kullanıcı adı ve şifremizi şifrelenmesi için starttls parametresini kullanıyoruz.
mail.login(USER, PASS)

#Toplu Mail Atacağımız için FOR döngüsü kuruyoruz.

for her_bir_mail in kisiler:
    mail.sendmail(mesaj["From"], her_bir_mail, mesaj.as_string())
    print("{} adresine mail gönderildi..".format(her_bir_mail))
    print("Mailler başarıyla gönderildi...")
mail.close()



#SMTP server'a login oluyoruz.
#    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
#Mailimizi sendmail parametresi ile gönderiyoruz.
# print("Mail Başarıyla Gönderildi...)
# mail.close()
