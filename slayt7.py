# n satırlı m sütunlu 0 matrisi
m =3
n =4
a = [[0 for x in range(n)] for x in range(m)]
print(a)


# İki matrisin toplamını bul.
def MatrisiEkranaYaz(Matris,Ad):
   print(Ad)
   for i in range(len(Matris)):  # satır
       for j in range(len(Matris[i])):  # sütun
           print(Matris[i][j], end=" ")
       print()
import random
boyut = int(input("Boyut Giriniz:"))
A =[[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
MatrisiEkranaYaz(A,'A')

B =[[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
MatrisiEkranaYaz(B,'B')

C =[[0 for i in range(boyut)]for j in range(boyut)]
for i in range(boyut): # satır
   for j in range(boyut): #sütun
       C[i][j] = A[i][j]+B[i][j]
MatrisiEkranaYaz(C,'C')


# Matrisin satır ve sütun toplamlarını hesapla
import random
def MatrisiEkranaYaz(Matris,Ad):
   print(Ad)
   for i in range(len(Matris)):  # satır
       for j in range(len(Matris[i])):  # sütun
           print(Matris[i][j], end=" ")
       print()

boyut = int(input("Boyut Giriniz:"))
A =[[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
MatrisiEkranaYaz(A,'A')

satirtop = []
sutuntop = []
for j in range(len(A)):  # sütun
    top1 = 0
    top2 = 0
    for i in range(len(A)):  # satır
       top1 += A[i][j]
       top2 += A[j][i]
    satirtop.append(top1)
    sutuntop.append(top2)
print("satır toplamı: ", satirtop)
print("sütun toplamı: ", sutuntop)


# Matristeki en büyük sayıyı bul.
# çözüm1
import random
def MatrisiEkranaYaz(Matris, Ad):
    print(Ad)
    max_number = None
    for i in range(len(Matris)):  
        for j in range(len(Matris[i])):  
            print(Matris[i][j], end=" ")
            if max_number is None or Matris[i][j] > max_number:
                max_number = Matris[i][j]
        print()
    if max_number is not None:
        print("Matristeki en büyük sayı:", max_number)
    else:
        print("Matris boş, en büyük sayı bulunamıyor.")
boyut=int(input("Boyut giriniz:"))
A = [[int(10*random.random()) for i in range(boyut)] for j in range(boyut)]
MatrisiEkranaYaz(A, 'A')

# çözüm2
def yazdir(matris, ad):
    print(ad)
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()
import random
boyut=int(input("Boyut giriniz:"))
matris = [[int(random.random()*10)for i in range(boyut)]for j in range (boyut)]
yazdir(matris, "matris")
max = matris[0][0]
for satir in matris:
        for sayi in satir:
            if sayi > max :
                 max = sayi
print("Matristeki en büyük sayı:", max)


# matris izini (diyagonal toplamı) bul
import random
def matris_izi(matris, ad):
    print(ad)
    iz = 0
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
        iz += matris[i][i]
    return iz
boyut = int(input("Boyut giriniz:"))
A = [[int(10*random.random())for i in range(boyut)]for j in range(boyut)]
print("Matrisin İzi:", matris_izi(A, "A"))


# Verilen sayıyı matrisin k. indeksine yerleştir?
def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris[i])):
            print(matris[i][j], end = " ")
        print()
import random
boyut = int(input("Boyut giriniz:"))
sayi = int(input("Yerleştirilecek sayıyı giriniz:"))
satir = int(input("İndeks satırı:"))
sütün = int(input("İndeks sütünü:"))
matris = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
yazdir(matris)
print()
for i in range(boyut):
    for j in range(boyut):
        if i == satir and j == sütün:
            matris[i][j] = sayi
yazdir(matris)


# Matrisin transpozunu alın.
def transpoz(matris,ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print()
import random
boyut = int(input("boyut giriniz: "))
A = [[int(10*random.random())for i in range(boyut)]for j in range(boyut)]
transpoz(A, "A")
print()
for i in range(boyut):
    for j in range(i, boyut):
        A[i][j],A[j][i] = A[j][i],A[i][j]
print("transpozu")
transpoz(A, "A")


# İki matrisin çarpımını hesaplayan prog?
def matrisi_yaz(matris, ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris)):
            print(matris[i][j], end=" ")
        print()
import random
boyut = int(input("boyut giriniz: "))
A = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
matrisi_yaz(A, "A")
B = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
matrisi_yaz(B, "B")
C = [[0 for i in range(boyut)]for j in range(boyut)]
for i in range(boyut):
    for j in range(boyut):
        C[i][j] = A[i][j]*B[i][j]
matrisi_yaz(C, "C")


# Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.
def matrisi_yaz(matris, ad):
    print(ad)
    for i in range(len(matris)):
        for j in range(len(matris)):
            print(matris[i][j], end=" ")
        print()
boyut = int(input("boyut giriniz: "))
A = [[0 for i in range(boyut)]for j in range(boyut)]
n = 1
for i in range(boyut):
    for j in range(boyut):
        A[i][j] = n
        n += 1
matrisi_yaz(A, "A")


# 0-1 değerlerini içeren bir matristeki nesnenin alanını hesapla.
def nesne_alanini_bul(matris):
    alan = 0
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            if matris[i][j] == 1:
                alan += 1
    return alan
import random
boyut = int(input("boyut giriniz: "))
A = [[(random.randint(0,1))for i in range(boyut)]for j in range(boyut)]
for i in A:         #bu for döngüsü alt alta yazdırma için
    print(i)
print("nesne alanı:", nesne_alanini_bul(A))


# 0-1 değerlerini içeren bir matristeki nesnenin kenarlarını hesapla.
def kenar_hesapla(matris):
    kenar_uzunlugu = 0
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and matris[i][j] == 1:
                kenar_uzunlugu += 1
    return kenar_uzunlugu
import random
boyut = int(input("boyut giriniz: "))
A = [[(random.randint(0,1))for i in range(boyut)]for j in range(boyut)]
for i in A:
    print(i)
kenar_uzunlugu = kenar_hesapla(A)
print("Kenar Uzunluğu:", kenar_uzunlugu)


# Matristeki şekli n kat büyüten programı yazınız?
def matrisi_buyut(matris, n):
    satir_sayisi = len(matris)
    sutun_sayisi = len(matris[0])
    yeni_matris = []
    for satir in matris:
        yeni_satir = []
        for eleman in satir:
            for _ in range(n):
                yeni_satir.append(eleman)
        for _ in range(n):
            yeni_matris.append(yeni_satir[:])
    return yeni_matris
import random
boyut = int(input("boyut giriniz: "))
A = [[(random.randint(0,1))for i in range(boyut)]for j in range(boyut)]
for i in A:
    print(i)
buyut = int(input("Matrisi kaç kat büyütmek istiyorsunuz? "))
yeni_matris = matrisi_buyut(A, buyut)
print("Yeni Matris:")
for satir in yeni_matris:
    print(satir)
