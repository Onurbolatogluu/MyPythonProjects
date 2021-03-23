def fibonacci():  # Fibonacci isimli fonksiyon oluşturuyoruz.

    a = 1  # A değişkenini oluşturup değerimizi 1 e eşitliyoruz.
    b = 1  # B değişkeni oluşturup değerimizi 1 e eşitliyoruz.
    yield a
    yield b #Değerlerimizi yield ile üretiyoruz.

# a ve b değerlerimize göre fibonacci sayımızı oluşturmaya çalışacağız.

    while True: #Döngümüzü oluşturuyoruz.

        a,b = b, a+b # Her döngü de, her a değerimiz b nin eski değeri olacak. her b değerimiz de a+b ye eşit olacak.

        yield b # yukarıda oluşturduğumuz, yeni b Değerimizi ürettik.


for sayı in fibonacci():

    if (sayı > 100000):
        break
    print(sayı)
