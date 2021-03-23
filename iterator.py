# Her next metodunu gönderdiğimizde 3ün bir sonraki kuvvetini almaya çalışacağız.
class Kuvvet3():

    # Max değeri 3ün kaçıncı değerine kadar alabileceğimizi gösteriyor. Kod üzerinde bunu belirticez.
    def __init__(self, max=0):
        # Fonskyiona argüman olarak göndereceğimiz sayıyı self.max değerine eşitliyoruz.
        self.max = max
        # 3ün 0ıncı kuvvetinden başlamamız için self.kuvvet özelliği tanımladık.
        self.kuvvet = 0

    # Fonksiyonumuz iterable olması için iter metodu tanımlıyoruz.
    def __iter__(self):
        return self  # iter Objemizi dönüyoruz.

    def __next__(self):
        # Kuvvet değerimiz max değere ulaşmamışsa, Bir sonraki kuvveti almaya devam edeceğiz.
        if (self.kuvvet <= self.max):
            # 3'ün self.kuvvet değerine göre kuvvetini alacağız. ve bunu da sonuç değişkenine atayacağız.
            sonuc = 3 ** self.kuvvet
#                                       self.kuvvet değerimiz ilk başta sıfır (0) olarak ayarlamıştık.
            # Daha sonrasında kuvvet değerimizi +1 arttıracağız.
            self.kuvvet += 1
            return sonuc  # Ardından sonucumuzu döneceğiz.

        else:  # Kuvvetimiz max değerini geçmişse, stopıtreratıon hatamızı döneceğiz.
            # Kuvvet max değerini geçmişse, kuvvet değerini 0'a eşitle..
            self.kuvvet = 0
            raise StopIteration


kuvvet = Kuvvet3(6)

#iteratorobjem = iter(kuvvet)
# print(next(iteratorobjem))
# print(next(iteratorobjem))

for i in kuvvet:
    print(i)

for j in kuvvet:
    print(j)

for k in kuvvet:
    print(k)
