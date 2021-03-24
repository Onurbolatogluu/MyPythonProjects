import requests
from bs4 import BeautifulSoup

#Kullanılacak olan modülleri kodumuza dahil ettik.

url = "https://www.trt1.com.tr/" #Verileri aldığımız site.
response = requests.get(url) #Modülümüzün get metodunu kullanıyoruz. Ve response değişkenine sonucumuzu atıyoruz.
print(response) #Ekrana bastırıyoruz.

html_icerigi = response.content # içeriklere erişmek için response.content kullanıyoruz ve bunu bir değişkene aktarıyoruz.
#requests_get metodu sayesinde response değişkenine content özelliğini kullanabiliriz.

soup = BeautifulSoup(html_icerigi,"lxml") #BeautifulSoup sınıfından obje elde edip bunu soup değişkenine atıyoruz.
#Ve böylelikle web sayfasını html olarak çekebileceğiz.
#lxml özelliği sayesinde web sitesinin içeriklerini aldık.
print(soup)

for i in soup.find_all("a"): # Find ile, sadece a etiketi ile başlayan içerikleri aldık.
    #İstediğimiz web site etiketlerini find_all özelliği ile alabiliyoruz.
    print(i.get("href")) # ve for döngüsü sayesinde tek tek içerikleri alıp düzgün olarak bastırdık.
    # i.get "href" ile i'ye get isteğinde bulunup href parametrelerinin değerlerini almış olduk.
    print("*****************")
    print(i.text) # A etiketi içerisinde bulunan yazıları aldık.
    print("*****************")
    
print(soup.find_all("div",{"class":"col-lg-12 col-md-12 col-sm-12 col-xs-12"}))
#Sadece belirli bir  div classı almak istersek, bunu yukarıdaki gibi belirtebiliriz. yani classı "col-lg-12 col-md-12 col-sm-12 col-xs-12" olanları ekrana getir diyoruz.

