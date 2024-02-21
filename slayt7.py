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
buyutme_faktoru = int(input("Matrisi kaç kat büyütmek istiyorsunuz? "))
yeni_matris = matrisi_buyut(A, buyutme_faktoru)
print("Yeni Matris:")
for satir in yeni_matris:
    print(satir)