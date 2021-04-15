from selenium import webdriver
import time  # Web sayfasının aktif kalma süresini ayarlamak için.
import random  # Link üzerinde random sayfalara gitmek için.
# Chrome ile bir browser açmasını söyledik.
browser = webdriver.Chrome(executable_path=('C://Users//sanal//Downloads//chromedriver.exe'))

# Gitmek istediğimiz url.
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:  # 10 text verisi çekeceğiz.
    # Linkteki sayfa sayısı kadar sayı ürettik.
    randomPage = random.randint(1, 2091)
    # url'nin sonuna randompage'den aldığımız rakamı giriyoruz.
    newUrl = url + str(randomPage)
    browser.get(newUrl)  # Yeni url'e istek gönderiyoruz.
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)  # 3 saniye bekliyoruz.
    pageCount += 1  # pagecount'u 1 arttırıyoruz.

with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("***********************************\n")
        entryCount += 1

browser.close()
