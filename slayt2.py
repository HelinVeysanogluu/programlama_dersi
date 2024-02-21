# V=I*R formülünü kullanarak verilen I ve R değerine göre V yi hesaplayan program?
ı = int(input("ı= "))
r = int(input("r= "))
v = ı*r
print("sonuç ", v)

# Kısa ve uzun kenarı girilen dikdörtgenin alanını ve çevresini  hesaplayan program?
kısa = int(input("kısa kenar: "))
uzun = int(input("uzun kenar: "))
alan = kısa*uzun
cevre = 2*(kısa+uzun)
print("alan:", alan)
print("çevre:", cevre)

# Yarıçapı verilen çemberin alanını hesaplayan program (pi = 3,14)?
r = int(input("yarıçap giriniz:"))
alan = (3.14)*(r**2)
print("alan:", alan)

# Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan program?
gun = int(input("gün giriniz: "))
yıl = gun//365
ay = gun//30
print(f"{gun} gün {yıl} yıl'dır")
print(f"{gun} gün {ay} ay'dır")

# Girilen 3 basamaklı bir sayıyı tersine çeviren program? (573 ==> 375)
sayi = int(input("3 basamaklı sayıyı giriniz: "))
birler = (sayi%100)%10
onlar = (sayi//10)%10
yuzler = sayi//100
yeni = birler*100 + onlar*10 + yuzler
print("yeni sayı:", yeni)

# 100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz?
not1 = int(input("sınav notunuzu giriniz: "))
donustur = not1/20
print("yeni notu:", donustur)

# Fiyat ve kdv oranı girilen ürünün toplam fiyatını ekrana yazdıran program?
fiyat = int(input("fiyat giriniz: "))
kdv = int(input("kdv oranı giriniz: "))
kdv_hesabı = fiyat*kdv/100
tutar = kdv_hesabı + fiyat
print(f"toplam {tutar} tl")

# Bir ürünün alış fiyatı, vergi ve kar oranlarını kullanılarak satış fiyatını hesaplayan program?
alis = int(input("alış fiyatı: "))
vergi = int(input("vergi oranı giriniz: "))
kar = int(input("kar oranı giriniz:"))
satis_fiyati = alis + (alis*vergi/100) + (alis*kar/100)
print("satış fiyatı:", satis_fiyati)

# Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?
sayi = int(input("3 basamaklı sayı giriniz: "))
birler = (sayi%100)%10
onlar = (sayi//10)%10
yuzler = sayi//100
print(f"birler basamağı {birler}, onlar basamağı {onlar}, yüzler basamağı {yuzler}")

# A ve B değişken değerlerini üçüncü bir değişken kullanmadan yer değiştiriniz?
A = int(input("A: "))
B = int(input("B: "))
A,B = B,A
print("A:", A, "\nB:", B)

# Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?
n = int(input("n: "))
k = int(input("k: "))
sonuc = (n*(n+1)/2)*k
print("sonuç:", sonuc)

# Çizginin başlangıç ve orta nokta koordinatları veriliyor. Diğer uç noktanın koordinatlarını bulunuz?
baslangic_x = int(input("x koordinatının başlangıç noktası: "))
baslangic_y = int(input("y koordinatının başlangıç noktası: "))
orta_nokta_x = int(input("x koordinatının orta noktası: "))
orta_nokta_y = int(input("y koordinatının orta noktası: "))
uc_nokta_x = baslangic_x + orta_nokta_x
uc_nokta_y = baslangic_y + orta_nokta_y
print("x:", uc_nokta_x, "y:", uc_nokta_y)
