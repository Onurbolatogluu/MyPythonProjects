def ekstra(fonk):

    def wrapper(sayılar):
        print("*****Mükemmel Sayılar*****")
        for sayı in sayılar:
            bölenler = list()
            for bölen in range(1, sayı):
                if sayı % bölen == 0:
                    bölenler.append(bölen)
            toplam = 0 
            for j in bölenler:
                toplam += j
            if toplam == sayı:
                print(sayı) 
        fonk(sayılar) 
    return wrapper
 
@ekstra
def asal_sayılar(sayılar):
    print("*****Asal Sayılar*****")
    for sayı in sayılar:
        x = 0
        if sayı == 0 or sayı ==1:
            continue

        elif sayı == 2:
            print(sayı)

        else:
            for bölen in range(2,sayı): 
                if sayı % bölen == 0:
                    x += 1 
            if x == 0:
                print(sayı)
                 
asal_sayılar(range(2,1001))