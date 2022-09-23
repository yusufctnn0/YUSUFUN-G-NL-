#veri tipleri 

#int tam sayı olanlar 1,2,3,4,5
#float ondalıklı sayı olanlar 1.2,2.4,5.6
#str karakter olanlar yusuf,midyat,cetin gibi 
#bool evet, hayır, doğru, yanlış
# bunlardan ayrı olarak öğrenci kısmı isStudent olarak başlatılır.

from functools import singledispatchmethod
from unittest import result


name ='yusuf'
age= 18
weight=59.6
isStudent= False

print(type(name))
print(type(age))
print(type(weight))
print(type(isStudent))

# int to float
result= int(weight)
print(result)

# float to int
result= float(age)
print(result)

#bool to str
result=str(isStudent)
print(isStudent)

result=int(isStudent)
print(result)
print(type(result))
