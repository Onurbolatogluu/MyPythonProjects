print("""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
""")
a = int(input("Birinci Sayı:")) # Birinci Sayıyı Alıyoruz.
b = int(input("İkinci Sayı:")) # İkinci Sayıyı Alıyoruz.

işlem =  input("İşlem Numarasını Giriniz:") # Buna göre koşullarımızı yazacağız.

if (işlem == "1"): # Toplama İşlemi

    print("{} ile {} 'nin toplamı {} dır.".format(a,b,a+b))

elif (işlem == "2"):

    print("{} ile {} 'nin farkı {} dır.".format(a, b, a - b))

elif (işlem == "3"):

    print("{} ile {} 'nin çarpımı {} dır.".format(a, b, a * b))

elif (işlem == "4"):

    print("{} 'nın {} 'e bölümü {} dır.".format(a, b, a / b))
else:

    print("Lütfen geçerli bir işlem giriniz...")






# Print ile uygulamamızın giriş bilgilendirme ekranını oluşturduk.
# Kullanıcıdan A ile B değişkenlerini string olarak istedik ardından inteeger'e çevirdik.
# Ardından kullanıcıdan işlem değişkeni istedik. Buna göre koşulları yazacağız.
# Ardından if ve elif parametreleri ile kodun içerisinde kullanıcıdan gelecek olan işlem değişkenine verilen değere
# - göre hangi işlemi yapılacak bu seçilecek.
# Ardından format parametresi ile A ile B'ye verilen değerler süslü parantez içine yazılacak ardından hangi işlem yapılcaksa
# - o işlem yapılıp en son süslü parantezin içerisine eklenecek.
