# Kullanıcıdan alınan sayıya kadar faktöriyel yazdıran program?
def faktoriyel(n):
    if (n == 0 or n == 1):
        return 1
    else:
        fak = n*faktoriyel(n-1)
        return fak
sayi = int(input("sayı giriniz: "))
for i in range(sayi+1):
    print((i), "! = ", faktoriyel(i))

# İlk N asal sayısını listeleyen program?
def asal_mi(n):
    x = 1
    for i in range(2, n):
            if n%i == 0:
                x = 0
                break
    return x
sayi = int(input("sayı giriniz: "))
a = 2
asal_sayi = 0
while asal_sayi < sayi:
    if asal_mi(a) == 1:
        asal_sayi += 1
        print(str(asal_sayi) + ". asal sayı: " + str(a))
    a += 1


# Girilen sayının kaç faktöriyel olduğunu bulan program? (720=6!)
def faktoriyel_hesapla(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel_hesapla(n-1)
sayi=int(input("sayı giriniz:"))
faktoriyel = 1
i = 1
while faktoriyel < sayi:
    i += 1
    faktoriyel = 1
    for j in range(1, i+1):
        faktoriyel *= j
if faktoriyel == sayi:
    print(f"{sayi} bir faktöriyeldir. {i}. faktöriyeldir.")
else:
    print(f"{sayi} bir faktöriyel değildir.")


# Listede en fazla tekrar eden elemanı silen program?
def enfazlatekrarsil(liste):
    sozluk = {}
    for eleman in liste:
        if eleman in sozluk:
            sozluk[eleman] += 1
        else:
            sozluk[eleman] = 1
    tekrarliste = []
    maxtekrar = 0
    for eleman in sozluk:
        tekrar = sozluk[eleman]
        if tekrar > maxtekrar:
            maxtekrar = tekrar
            tekrarliste = [eleman]
        elif tekrar == maxtekrar:
            tekrarliste.append(eleman)
    yeni_liste = []
    for eleman in liste:
        if eleman not in tekrarliste:
            yeni_liste.append(eleman)
    return yeni_liste
liste = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7, 2, 8, 9, 2]
print(enfazlatekrarsil(liste))

# Girilen sayının Güçlü (1! + 4! + 5!  = 1 + 24 + 120 = 145) olup olmadığını bulan program?
def faktoriyel(n):
    fak = 1
    for i in range(1, n+1):
        fak *= i
    return fak
sayi = int(input("sayı giriniz: "))
toplam = 0
gercek_sayi = sayi   #kullanıcının girdiği orijinal sayının bir kopyasıdır ve basamaklarına erişmek için kullanılır.
while gercek_sayi>0 :
    basamak_sayisi = gercek_sayi%10
    gercek_sayi //= 10
    toplam += faktoriyel(basamak_sayisi)
if sayi == toplam:
    print(sayi, "güçlü sayıdır")
else:
    print(sayi, "güçlü sayı değildir")

# PASCAL üçgeninin n. satırını üretiniz? (c=n!/(n-r)!*r!)
def faktoriyel(sayi):
    fak = 1
    for i in range(1, sayi+1):
        fak *= i
    return fak
n = int(input("n: "))
for r in range(n):
    pay = faktoriyel(n-1)
    payda = faktoriyel(n-1-r) * faktoriyel(r)
    print(pay/payda, end=" ")
