from unicodedata import name


print()

# 7000TL olan bir ürünün %18 kdv'si kaç tl yapar bakalım.

print(7000 + (7000 * 0.18))
print(17500 + (17500 * 0.18))

# sürekli rakamları değştirmek yerine bir ad verip oradan tümünü değiştirebiliriz.

urun1=7000
urun2=17500
urun3=8500
kdv=0.18

print(urun1 + (urun1 * kdv))
print(urun2 + (urun2 * kdv))
print(urun3 + (urun3 * kdv))

# evet aynen bunu demek istemiştim :D
# değişkenler boşluk içeremez 
# değişkenler sayı ile başlayamaz
# ^türkçe karakter kullanmamaya dikkat edelim 

sayi=20
SAYİ=30
print(sayi)
print(SAYİ)
# ikisi farkli sayıdır. harfin büküklük ve küçüklüğü sonucu değiştirir 

a,b,c = 10,20,30
print(a,b,c)
# şu şekilde de değişkenler olabilir

x=1
y=2.5
print(type(x))
print(type(y))

name='YUSUF'
print(type(name))
