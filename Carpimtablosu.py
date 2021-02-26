for i in range(1, 11):
    print("-" * 20)
    print(i, "'ler")

    print("-" * 20)
    for k in range(1, 11):
        print(i, "x", k, "=", i*k)


# Öncelikler 1 den başlayıp 11’e kadar(11 dahil değil) bir döngü açmalısınız. Bu döngü i döngüsü olsun. Daha sonra hemen i döngüsü içine yine 1 den başlayıp 11 e kadar olan ikinci bir döngü açmalısınız. Bu döngü ise k döngüsü olsun.

# i döngüsünün alacağı her değer için k döngüsü 10 defa tekrarlanacaktır. k değişkeni sıra ile 1 den 10 a kadar değer alacaktır.

# komutu ile ekrana 1×1=1, 1×2=2 … ifadeleri alt alta olacak bir şekilde yazılacaktır. Daha sonra i değişkeni 2 değerini alacak ve k değişkeni i değişkeninin 2 olduğu zaman 10 defa dönecektir. ve ekrana 2×1=2, 2×2=4 … ifadeleri alt alta yazılacaktır.

# print (“-“*20) komutu ile aralara çizgi ekleyerek daha güzel bir görüntü elde edebilirsiniz.