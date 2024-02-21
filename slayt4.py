# element değişkeninin altına 0dan 9a 1er artarak, value değişkeninin altına 2den 20ye 2şer artarak yaz.
x = 0
y = 2
print("element   value")
while x<10:
    print(x,"       ",y)
    x += 1
    y += 2

#Girilen 5 sayının ortalamasını bulan program?
x = 0
for i in range(5):
    sayi = int(input("sayı: "))
    x += sayi
ort = x/5
print("ortalama:", ort)

#Girilen 5 sayı içerisindeki minimum ve maksimum değerleri bulan program?
sayilar = []
for i in range(5):
    sayi = int(input("sayı: "))
    sayilar.append(sayi)
minimum = sayilar[0]
maksimum = sayilar[0]
for sayi in sayilar:
    if sayi<minimum:
        minimum = sayi
    if sayi>maksimum:
        maksimum = sayi
print("en küçük:", minimum, "en büyük:", maksimum)

#N’e kadar tek sayıları yazdıran program?
N = int(input("N: "))
for i in range(1, N+1, 2):
    print(i)

#Girilen sayının tam bölenlerini bulan program?
sayi = int(input("sayı: "))
for i in range(1, sayi+1):
    if sayi%i == 0:
        print(i)

# a^b yi açık hesaplayan program?
a = int(input("a: "))
b = int(input("b: "))
for i in range(1, b+1):
    sonuc = a**i
    print(sonuc)

#n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?
n = int(input("n: "))
tek = 0
cift = 1
for i in range(1, n+1):
    if i%2 == 0:
        cift *= i
    if i%2 == 1:
        tek += i
print("çiftlerin çarpımı:", cift, "teklerin toplamı:", tek)

#Girilen sayının faktöriyelini hesaplayan program?
sayi = int(input("sayı: "))
faktoriyel = 1
for i in range(1, sayi+1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")

#Girilen n değerine göre Fibonacci serisinin ( 0 1 1 2 3 5 8 … ) ilk n terimini hesaplayınız?
n = int(input("n: "))
liste = []
if n>=1 :
    liste.append(0)
if n>=2:
    liste.append(1)
for i in range(2, n):
    fibonacci = liste[i-1] + liste[i-2]
    liste.append(fibonacci)
print(liste)

#Girilen n adet sayı içerisinden pozitif, negatif ve sıfır sayısının kaçar adet tekrarlandığını bulan program?
n = int(input("n: "))
pozitif = 0
negatif = 0
sifir = 0
for i in range(n):
    sayi = int(input("sayı: "))
    if sayi > 0:
        pozitif += 1
    elif sayi < 0:
        negatif += 1
    else:
        sifir += 1
print("pozitif:", pozitif, "negatif:", negatif, "sıfır:", sifir)

#Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?
ilk_eleman = int(input("ilk elemanı giriniz: "))
eleman_sayisi = int(input("toplam eleman sayısını giriniz: "))
artis_degeri = int(input("artış değeri giriniz: "))
toplam = 0
for i in range(eleman_sayisi):
    toplam += ilk_eleman
    ilk_eleman += artis_degeri
print(toplam)

#f(x)=x^2-2x-3 fonksiyonunun x eksenini kestiği nokta sayısını bulunuz?
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
delta = b**2-4*a*c
if delta<0:
    print("reel kök yok")
elif delta==0:
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
    print("tek kök var:", x1)
else:
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
    print("çift kök var:", x1,",", x2)

#Girilen bir sayının asal olup olmadığını bulunuz?
sayi = int(input("sayı giriniz: "))
kontrol = 0
for i in range(2, sayi):
    if sayi%i == 0:
        kontrol = 1
        break
if kontrol == 0:
    print("sayı asal")
else:
    print("sayı asal değil")

#Girilen bir sayının asal çarpanlarını bulan program?
sayi = int(input("sayı giriniz: "))
carpanlar=[]
carpan=2
while sayi>1:
    if sayi%carpan==0:
        carpanlar.append(carpan)
        sayi/=carpan
        continue
    else:
        carpan+=1
print(carpanlar)

#Girilen sayının basamak değerleri çarpımını bulunuz?
sayi = int(input("sayı giriniz: "))
carpim = 1
while sayi > 0:
    deger = sayi%10
    carpim *= deger
    sayi //= 10
print(carpim)

#Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?
sayi=int(input("sayı giriniz: "))
k=int(input("k: "))
while sayi>0:
    deger = sayi % 10
    if deger!=k:
        print(deger)
    sayi //= 10

#Girilen sayının basamak sayısını ekrana yazdıran program?
sayi=int(input("sayı giriniz: "))
basamak = 0
while sayi>0:
    deger = sayi%10
    if deger>=0:
        basamak += 1
    sayi //= 10
print(basamak)

#TC kimlik noyu doğru girmeye zorlayınız? (11 karakter ve tamamı sayı)
tc = input("tc: ")
rakam = ("0","1","2","3","4","5","6","7","8","9")
basamak = 0
while tc>=0:
    deger = tc%10
    if deger>=0:
        basamak += 1
    tc //= 10
print(basamak)
if tc != rakam and basamak != 11:
    print("yanlış veya eksik tc")
else:
    print("tc doğru")

#Girilen cümleyi tersten yazdırın?
cumle = input("cumle: ")
yeni_cumle = ""
for i in range(len(cumle)-1,-1,-1):
    yeni_cumle += cumle[i]
print(yeni_cumle)

#Girilen cümledeki sesli ve sessiz harf sayısını bulun?
cumle = input("cümle: ")
sesli = "AaEeIıİiOoÖöUuÜü"
sessiz = "BbCcÇçDdFfGgĞğHhJjKkLlMmNnPpRrSsŞşTtVvYyZz"
sesli_harf = 0
sessiz_harf = 0
for harf in cumle:
    if harf in sesli:
        sesli_harf += 1
    else:
        sessiz_harf += 1
print("sesli harfler:", sesli_harf, "sessiz harfler:", sessiz_harf)

#Girilen cümledeki harflerin adetlerini ekrana yazın?
cumle = input("cümle: ")
sozluk = {}
for i in cumle:
    harf = 0
    for j in cumle:
        if i==j:
            harf += 1
            sozluk[i] = harf
print(sozluk)

#Girilen cümledeki harf adedini bulunuz?
cumle = input("cümle: ")
harfler = "AaBbCcÇçDdEeFfGgĞğHhIıİiJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz"
adet = 0
for i in cumle:
    if i in harfler:
        adet += 1
print("harf adedi:", adet)

#Girilen iki sayının OKEK (ortak katların en küçüğü) hesaplayan program?
sayi1 = int(input("1.sayı: "))
sayi2 = int(input("2.sayı: "))
carpim = sayi1*sayi2
for i in range(1, carpim+1):
    if i%sayi1 == 0 and i%sayi2 == 0:
        okek = i
        break
print(f"{sayi1} ve {sayi2}'nin OKEK'i {okek}")

#Girilen iki sayının OBEB (ortak bölenlerin en büyüğü) hesaplayan program?
sayi1 = int(input("1.sayı: "))
sayi2 = int(input("2.sayı: "))
if sayi1>sayi2:
    en_kucuk = sayi2
else:
    en_kucuk = sayi1
for i in range(1, en_kucuk+1):
    if sayi1%i == 0 and sayi2%i == 0:
        obeb = i
print(f"{sayi1} ve {sayi2}'nin OBEB'i {obeb}")

#1 ile 10 arasında sayı tahmin oyunu
import random
hedef = random.randint(1,10)
sayi = int(input("sayı giriniz: "))
if sayi > hedef:
    print("tahmininiz sayıdan büyük, hedef:", hedef)
elif sayi < hedef:
    print("tahmininiz hedeften küçük, hedef:", hedef)
else:
    print("doğru tahmin ettiniz, hedef:", hedef)

#Harf tahmin oyunu
import random
harfler = "QqWwEeRrTtYyUuIıOoPpĞğÜüAaSsDdFfGgHhJjKkLlŞşİiZzXxCcVvBbNnMmÖöÇç"
hedef = random.choice(harfler)
harf = input("harf giriniz: ")
if harf == hedef:
    print("tahmininiz doğru, hedef:", hedef)
else:
    print("tahmininiz yanlış, hedef:", hedef)

#Bir top X metre yükseklikten bırakılıyor. Her sıçrayışta  önceki yüksekliğini %20 kaybediyor. 1 metreden daha az olana kadar aldığı toplam yolu ve sıçrama sayısını hesaplayınız?
x = int(input("x: "))
alinan_yol = x
sicrama_sayisi = 0
while x>1:
    kaybolan = x*20/100
    alinan_yol += 2*(x-kaybolan)
    sicrama_sayisi += 1
    x -= kaybolan
print("alınan yol:", alinan_yol, "sıçrama sayısı:", sicrama_sayisi)

#Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne alındığında üçgenin çizilip çizilemeyeceğini, çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), alanını(heron alan formulü) ve çevresini hesaplayan program?
a = int(input("1.kenar: "))
b = int(input("2.kenar: "))
c = int(input("3.kenar: "))
if a+b>c and a+c>b and b+c>a:
    print("bu üçgen çizilebilir")
    if a==b==c:
        print("bu üçgen eşkenardır")
    elif a==b or a==c or b==c:
        print("bu üçgen ikizkenardır")
    else:
        print("bu üçgen çeşitkenardır")
else:
    print("bu üçgen çizilemez")
cevre = a+b+c
print("çevre:", cevre)
u = (a+b+c)/2
alan = (u*(u-a)*(u-b)*(u-c))**0.5
print("alan:", alan)

#Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz?
sayi = int(input("sayı giriniz: "))
kontrol = 0
for i in range(1,sayi):
    if i*(i+1) == sayi:
        kontrol = 1
        break
if kontrol == 1:
    print("bu sayı pronic sayıdır")
else:
    print("bu sayı pronic sayı değildir")

#Girilen sayının Harshad (sayının kendisi rakamları toplamına bölünüyor) olup olmadığını bulunuz?
sayi = int(input("sayı giriniz: "))
liste = []
for i in str(sayi):
    liste.append(int(i))
toplam = 0
for j in liste:
    toplam += j
if sayi%toplam == 0:
    print("bu sayı harshad sayıdır")
else:
    print("bu sayı harshad sayı değildir")

#Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz? 
sayi = int(input("sayı giriniz: "))
liste = []
for i in str(sayi):
    liste.append(int(i))
kontrol = 0
for j in range(0, len(liste)):
    if liste[j]-liste[j-1]>1 or liste[j-1]-liste[j]>1:
        kontrol = 1
        break
if kontrol == 1:
    print("bu sayı jumbled sayı değildir")
else:
    print("bu sayı jumbled sayıdır")
