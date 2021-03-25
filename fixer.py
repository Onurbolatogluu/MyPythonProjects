import requests

url = "http://data.fixer.io/api/latest?access_key=APIKEY"
response = requests.get(url)
json_verisi = response.json()

bir = input("Döviz Giriniz: ")
iki = input("Karşılaştırılacak Para Birimi: ")
miktar = float(input("Miktarı Giriniz:"))
bir = bir.upper()
iki = iki.upper()

deger = json_verisi["rates"][iki]/json_verisi["rates"][bir] * miktar

print("Toplam Tutar:",deger)



