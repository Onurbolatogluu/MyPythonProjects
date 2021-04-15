from selenium import webdriver
import time # Web sayfasının aktif kalma süresini ayarlamak için.
import random # Link üzerinde random sayfalara gitmek için.
# Chrome ile bir browser açmasını söyledik.
browser = webdriver.Chrome(executable_path=('C://Users//sanal//Downloads//chromedriver.exe'))

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p=" # Gitmek istediğimiz url.

pageCount = 1 
entries = []

while pageCount <= 10: # 10 text verisi çekeceğiz.
    randomPage = random.randint(1,2091) # Linkteki sayfa sayısı kadar sayı ürettik.
    newUrl = url + str(randomPage) # url'nin sonuna randompage'den aldığımız rakamı giriyoruz.
    browser.get(newUrl) # Yeni url'e istek gönderiyoruz.
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3) # 3 saniye bekliyoruz.
    pageCount +=1 # pagecount'u 1 arttırıyoruz.

for entry in entries:
    print("***********************************************************************************************************************")
    print(entry)

browser.close()


"""
browser.get(url) # İlgili url'i aç.


time.sleep(5) # 10 saniye bekle.









elements = browser.find_elements_by_css_selector(".content")
# İlgili url üzerinde class'ı content olan tüm objeleri sorguluyoruz.




for element in elements:
    print("***************************")
    print(element.text) # Objenin içerisinde bulunan type'ı text olan veriyi ekrana bastırıyoruz.

browser.close()
"""
