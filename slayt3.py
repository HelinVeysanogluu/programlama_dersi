#Girilen tamsayının sıfır, pozitif ya da negatif olup olmadığını bulan program?
sayi = int(input("sayı giriniz: "))
if sayi == 0:
    print("sayınız sıfır")
elif sayi > 0:
    print("sayınız pozitif")
else:
    print("sayınız negatif")

#Vize ve Final notu girilen öğrencinin geçip geçmediğini hesaplayan program (vizenin %40,finalin %60’ı hesaplanır. Final en az 55, ortalama en az 50 olmak zorundadır)
vize = int(input("vize notunuz: "))
final = int(input("final notunuz: "))
ort = (vize*40/100) + (final*60/100)
if ort >= 50 and final >=55:
    print("dersten geçtiniz.")
else:
    print("dersten kaldınız.")

#Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program?(sayılar eşit olmayacak)
sayi1 = int(input("1.sayı: "))
sayi2 = int(input("2.sayı: "))
sayi3 = int(input("3.sayı: "))
if sayi1>sayi2 and sayi1>sayi3:
    print("en büyük sayı sayı1")
elif sayi2>sayi1 and sayi2>sayi3:
    print("en büyük sayı sayı2")
else:
    print("en büyük sayı sayı3")

#Girilen sayının 6'nın katı olduğunu bulan program?
sayi = int(input("sayı giriniz: "))
if sayi%2==0 and sayi%3==0:
    print("sayı 6'nın katı")
else:
    print("sayı 6'nın katı değil")

#İşçi maaşı ve çocuk sayısı verilmektedir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zam yaparak yeni maaşı hesaplayınız?
maas = int(input("maaşınızı giriniz: "))
cocuk_sayisi = int(input("çocuk sayısı giriniz: "))
if cocuk_sayisi == 1:
    yeni_maas = maas + (maas*5/100)
elif cocuk_sayisi == 2:
    yeni_maas = maas + (maas*10/100)
else:
    yeni_maas = maas + (maas*15/100)
print("yeni maaşınız:", yeni_maas)

#Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
print("1.toplama \n2.çıkarma \n3.çarpma \n4.bölme")
sayi1 = int(input("1.sayıyı giriniz: "))
sayi2 = int(input("2.sayıyı giriniz: "))
islem = int(input("istediğiniz işlemi giriniz: "))
if islem == 1:
    sonuc = sayi1+sayi2
elif islem == 2:
    sonuc = sayi1-sayi2
elif islem == 3:
    sonuc = sayi1*sayi2
else:
    sonuc = sayi1/sayi2
print("sonuç:", sonuc)

#Çizgi daireyi kesiyor mu, yoksa teğet mi sonucunu bulan program? 
#Çizgi: ax+by+c=0    Daire: (dx,dy,r) 
import math
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
dx = int(input("dx= "))
dy = int(input("dy= "))
r = int(input("r= "))
d = abs(a*dx+b*dy+c)/math.sqrt(a**2+b**2)
if d>r:
    print("çizgi daireyi kesmiyor")
elif d==r:
    print("çizgi daireye teğet")
else:
    print("çizgi daireyi kesiyor")
