import math
import time
from typing import Match
print("""Gelişmiş Hesap Makinesine Hoşgeldiniz... ^^
*****************************Tuşlar ve Fonksiyonları*****************************
*   Toplama işlemi için hesap makinesinin "+" tuşunu                            *
*   Çıkarma işlemi için hesap makinesinin "-" tuşunu                            *
*   Bölme işlemi için hesap makinesinin "/" tuşunu                              *
*   Çarpma işlemi için hesap makinesinin "*" tuşunu                             *
*   Faktöriyel işlemi için hesap makinesinin "fak" tuşunu                       *
*   Bölümden kalanı hesaplama işlemi için hesap makinesinin "böl" tuşunu        *
*   Log işlemi için hesap makinesinin "log" tuşunu(x tabanında)                 *
*   Mutlak Değer Hesaplamak için hesap makinesinin "mutlakd" tuşunu             *
*   Ebob işlemi için hesap makinesinin "ebob" tuşuna                            *
*   Programdan çıkmak veya işlemleri sonlandırmak için "q" tuşunu kullanınız    *
*                                                                               *       
*********************************************************************************
      """)

sayı1 = 0
sayı2 = 0
işlem = 0

while True:
    işlem = input("işlem giriniz:")

    if işlem == "+":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        sayı1 += sayı2
        print(sayı1)

    elif işlem == "-":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        sayı1 -= sayı2
        print(sayı1)

    elif işlem == "*":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        sayı1 *= sayı2
        print(sayı1)

    elif işlem == "/":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        sayı1 /= sayı2
        print(sayı1)

    elif işlem == "fak":
        sayı1 = int(input("Sayıyı Giriniz:"))
        sayı1 = math.factorial(sayı1)
        print(sayı1)

    elif işlem == "böl":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        math.fmod(sayı1, sayı2)
        print(math.fmod(sayı1, sayı2))

    elif işlem == "mutlakd":
        sayı1 = int(input("Sayıyı Giriniz:"))
        sayı1 = math.fabs(sayı1)
        print(sayı1)

    elif işlem == "ebob":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        print(math.gcd(sayı1, sayı2))

    elif işlem == "log":
        sayı1 = int(input("1.Sayıyı Giriniz:"))
        sayı2 = int(input("2.Sayıyı Giriniz:"))
        sayı1 = math.log(sayı1, sayı2)
        print(sayı1)

    elif işlem == "q":
        print("Uygulama Kapatılıyor...")
        time.sleep(5)
        break

    else:
        print("Geçersiz İşlem.")
