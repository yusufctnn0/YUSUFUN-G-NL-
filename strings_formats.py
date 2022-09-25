import numbers
from unittest import result


name='Yusuf'
surname= 'Çetin'
age= 18

print( 'My name is {} {}'. format(name,surname))
print( 'My name is {} {} {} years old'. format(name,surname,age))

#indeks içine yazdğığın rakamdan başlar.
print( 'My name is {1} {0} {2} years old'. format(name,surname,age))
print( 'My name is {0} {1} {2} years old {2}'. format(name,surname,age))

#sayılar ile de bu değişkeni kullanabiliriz.

number=50*2
print('the result {n}'.format(n=number))

# format kısmını küçültebilirizde onu da şu şekil kullanıyoruz.

print(f'My name is {name} {surname} I am {age} years old ')



