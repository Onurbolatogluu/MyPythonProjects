from decouple import config #Kullanıcı Bilgilerimi Dosyadan okumak için bu modülü ekliyorum.
import smtplib # Mail gönderme ve mail sunucusuna bağlanmak için bu modülü ekliyoruz.
from email.message import EmailMessage 
#Kullanıcı bilgilerinin bulunduğu değerleri çektik.

USER = config("USER")
PASS = config("KEY")

#Mail İçeriğini Oluşturduk

mesaj = EmailMessage() 
mesaj["Subject"] = "Deneme Mesajı"
mesaj["From"] = USER
mesaj["To"] = USER
mesaj.set_content("Burası Mailin içeriği..")


#SMTP ERİŞİMİ

mail = smtplib.SMTP("mail.onurbolatoglu.com", 587)
#smtplib.SMTP sınıfından obje oluşturup içerisinde smtp bilgisini ve port bilgisini yazıp bağlanıyoruz. ve bunu değişkene atıyorum.
mail.ehlo()
#Bağlanacağımız için ehlo parametresi gönderiyoruz.
mail.starttls()
#Kullanıcı adı ve şifremizi şifrelenmesi için starttls parametresini kullanıyoruz.
mail.login(USER, PASS)
#SMTP server'a login oluyoruz.
mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
#Mailimizi sendmail parametresi ile gönderiyoruz.
print("Mail Başarıyla Gönderildi....")
mail.close()



