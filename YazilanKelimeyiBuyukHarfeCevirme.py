kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Küçük ve Büyük harflerin bulunduğu birer karakter dizisi oluşturduk.
# Bunun sebebi küçük harflerin büyük harfler dizisinde hangi sırada olduğunu bulabilmekti.

kelime = input("Kelime Giriniz:")
# Kullanıcıdan bir kelime alıyoruz ve bunu kelime değişkenine atıyoruz.

yeni_kelime = ""

for i in kelime:
    # Kullanıcıdan aldığımız kelimeyi parçaladık. Yani her bir karakterini sırayla i değişkenine atadık.
    # Çünkü bu i değişkeninde bulunan harfi aratıp büyük harfler dizisinde hangi index'de olduğuna bakacağız.
    if i in kucuk_harfler:
        # Bu harfin küçük harfler dizisinde olup olmadığını kontrol ettik. Eğer yoksa farklı olan bu karakteri direkt olarak yeni oluşturduğumuz "yeni kelime" değişkenine ekledik.
        for index in range(len(kucuk_harfler)):
            # Var olması durumunda ise metot kullanmadan index numarasını bulabilmek için sırayla numara denedik. Bu numaraları ise range fonksiyonu sayesinde ürettik.
            # Rannge fonksiyonuna vermiş olduğumuz len fonksiyonu sayesinde küçük harfler dizisinin index uzunluğu kadar sayı üretebildik ve denedik.
            if kucuk_harfler[index] == i:
                INDEX = index
                # i değişkenine eşit olan index numarsını kayıtta tutabilmek için INDEX adındaki değişkeni oluşturduk.
                break
                #Ardından döngüyü kırıp gereksiz işlem yükünden kurtulduk.

        yeni_kelime += buyuk_harfler[INDEX]
        #Yeni kelimemize büyük harfler dizisindeki INDEX değerinde bulunan karakterleri ekledik. Bu sayede yeni kelimemizi oluşturmaya başlamış olduk. Döngü devam ettikçe yeni kelimemiz tamamlanmış oldu.
    else:
        yeni_kelime += i

print(yeni_kelime)
#Ve son olarak ekrana basılmış oldu.