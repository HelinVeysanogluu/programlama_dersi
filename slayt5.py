#Girilen 5 sayının ortalamasını bulan program?
toplam = 0
for i in range(5):
    sayi = int(input("sayı: "))
    toplam += sayi
ortalama = toplam/5
print("ortalama:", ortalama)

#Girilen 5 sayının standart sapmasını bulan program?
toplam = 0
liste = []
for i in range(5):
    sayi = int(input("sayı: "))
    toplam += sayi
    liste.append(sayi)
ort = toplam/5
ss = 0
for j in liste:
    ss += (j-ort)**2
sonuc = (ss/4)**0.5
print("standart sapma:", sonuc)

#Girilen sayının listede olup olmadığını bulan program?
liste = [2,4,6,8,10]
sayi = int(input("sayı: "))
kontrol = 0
for i in liste:
    if i == sayi:
        kontrol = 1
        break
if kontrol == 1:
    print("sayı listede var")
else:
    print("sayı listede yok")

#Elemanları sıralayan program?
liste = [3, 1, 2, 5, 4]
for i in range(len(liste)):
    for j in range(len(liste) - 1):
        if liste[j] > liste[j + 1]:
            temp = liste[j]
            liste[j] = liste[j + 1]
            liste[j + 1] = temp
print("Sıralı liste:", liste)

#Her elemanın tekrar sayısını bulan program?
liste = [2,7,7,6,9,2,8,3,6,9,2,1,8,3,4,0,4,9,3,]
sozluk = {}
for i in liste:
    tekrar = 0
    for j in liste:
        if i == j:
            tekrar += 1
    sozluk[i] = tekrar
print(sozluk)

#Girilen yazıdaki boşluk karakter sayısını bulan program?
cumle = input("cümle: ")
bosluk = 0
for i in cumle:
    if i == " ":
        bosluk += 1
print("boşluk sayısı:", bosluk)

#Girilen iki yazıyı karşılaştıran (eşit olup olmadığını bulan) program?
yazi1 = input("1.yazı: ")
yazi2 = input("2.yazı: ")
if yazi1 == yazi2:
    print("iki yazı aynı")
else:
    print("iki yazı farklı")

#Girilen yazının büyük yazılıp yazılmadığını bulan program?
yazi = input("yazı: ")
buyuk_harf = 0
kucuk_harf = 0
for harf in yazi:
    if "A" <= harf <= "Z":
        buyuk_harf = 1
    elif "a" <= harf <= "z":
        kucuk_harf = 1
if buyuk_harf == 1 and kucuk_harf == 0:
    print("yazının hepsi büyük harfli")
elif buyuk_harf == 0 and kucuk_harf == 1:
    print("yazının hepsi küçük harfli")
else:
    print("yazıda büyük-küçük harf karışık")

#Girilen yazının k. karakteriyle r. karakteri arasını kopyalayan programı yazınız?
yazi = input("yazı: ")
k = input("k: ")
r = input("r: ")
yeni_yazi = ""
kopyala = 0
for harf in yazi:
    if harf == k:
        kopyala = 1
    if kopyala:
        yeni_yazi += harf
    if harf == r:
        break
print(yeni_yazi)

#Girilen yazıdaki kelime, rakam ve karakter sayısını bulan program?
yazi = input("yazı: ")
rakamlar = "0123456789"
karakterler = "!'^+%&/=?>_#*$|-.,<"
kelime = 0
rakam = 0
karakter = 0
for i in yazi:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        kelime += 1
    elif i in rakamlar:
        rakam += 1
    elif i in karakterler:
        karakter += 1
print("kelime sayısı:", kelime, "rakam sayısı:", rakam, "karakter sayısı:", karakter)

#Girilen yazıdaki aranan kelimenin önüne ve arkasına TIRNAK sembolünü ekleyen program?
yazi = input("yazı: ")
kelime = input("kelime: ")
yeni = ""
i = 0
while i < len(yazi):
    if yazi[i:i+len(kelime)] == kelime:
        yeni += '"' + kelime + '"'
        i += len(kelime)
    else:
        yeni += yazi[i]
        i += 1
print(yeni)

#Girilen yazıdaki bir karakteri sil
yazi = input("yazı: ")
sil = input("silmek istediğiniz karakter: ")
yeni = ""
for i in yazi:
    if i == sil:
        continue
    yeni += i
print(yeni)

#Girilen yazıdaki bir kelimeyi sil
yazi = input("yazı: ")
kelime = input("silmek istediğiniz kelime: ")
yeni = ""
i = 0
while i < len(yazi):
    if yazi[i:i+len(kelime)] == kelime:
        i += len(kelime)
    else:
        yeni += yazi[i]
        i += 1
print(yeni)

#Girilen yazıdaki noktalama işaretlerini sil
yazi = input("yazı: ")
noktalama = ".,:;!_-/?'"
yeni = ""
for i in yazi:
    if i not in noktalama:
        yeni += i
print(yeni)

#Girilen onluk sayıyı ikili sayıya dönüştürünüz?
onluk_sayi = int(input("Onluk sayı giriniz: "))
ikilik_sayi = ""
while onluk_sayi > 0:
    kalan = onluk_sayi%2
    ikilik_sayi += str(kalan)
    onluk_sayi //= 2
ikilik = ""
for i in range(len(ikilik_sayi)-1,-1,-1):
    ikilik += str(ikilik_sayi[i])
print(ikilik)
