import requests
import sys
#Kullanacağımız modülleri projemize dahil ediyoruz.

#Json objeleri sözlükler ile aynı yapıya sahiptirler. 

# Verileri alacağımız site adresi.
url = "https://api.exchangeratesapi.io/latest?base="

birinci_doviz = input("Birinci Döviz:") #Kullacıdan değer alıyoruz. ve birinci_doviz değişkenine atıyoruz.
ikinci_döviz = input("İkinci Döviz:") #Kullanıcıdan değer alıyoruz. ve ikinci_doviz değişkenine atıyoruz. 
#birinci döviz'i ikinci_doviz' çevireceğiz.
miktar = float(input("Miktar:")) # Çevirmek istediği miktarı kullanıcıya soruyoruz.


response = requests.get(url + birinci_doviz) # response değişkeni tanımlayıp, requests.get ile url'e istek atıyoruz ve +birinci_dovız yazıyoruz.
#get istedğimiz şu şekilde olacak, (http://api.fixer.io/latest?base=USD) toplama yaptığımız için birinci dovız'e girilen değer url'nin sonuna eklendi.
#Böylelikle kullanıcı USD girerse birinci döviz'e siteden usd bilgileri almış olacağız.

json_verisi = response.json() # Response objemizi json objemize döndürmemiz gerekiyor. Çünkü istek gönderdiğimiz,
#site üzerinde TRY değerini json belgesi üzerinde arayacağız. Böylelikle çektiğim veri json formatına dönüyor. ve bunu da bir değişkene eşitliyorum.

try:
    print(json_verisi["rates"][ikinci_döviz] * miktar) 
    # json verisi içerisinde "rates" anahtarını arıyoruz. Çünkü para birimlerimiz bu sınıfın altında, 
    # böylelikle 2.dövizimizi rates altında arayabiliriz. böylelikle sadece istediğimiz para birimi karşımıza gelecek.
    # İstenilen miktarı da, ikinci döviz'e karşılık gelen değerle çarparak toplam tutarı öğrenebileceğiz..

except KeyError: # Olmayan para birimi girilmesi durumunda, fırlatılacak hata..
    sys.stderr.write("Lütfen para birimlerini doğru girin.") 
    sys.stderr.flush()









