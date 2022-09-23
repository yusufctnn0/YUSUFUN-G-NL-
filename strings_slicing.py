name='yusuf'
surname='cetin'
age='18'
 
text= 'Benim adım ' + name + ' Soyadım ' + surname + ' yaşım ise ' + age 
print(text)

# burada ise bir yerden bir yere kadar almak için : işaretini kullanacağız. yada tam sayı verdiğimiz karakteri.

print(text[1])
print(text[0:7])
print(text[8:18])
print(text[:20]) #başlangıç belirtmeden sonuna kadar almak.
print(text[0:]) #son belirtmeden sonuna kadar almak.

print(text[-19:-1])
print(text[:-1])
print(text[-20:])

# burda ise sonra ki : işareti 2'şer defa atlayarak gitmesini sağladım 
print(text[0:20:2])
print(text[0:20:3])

#burda ise hem başlangıç hemde bitiş yerini belirlemeden 2'şer artmasını sağlayacağız.
print(text[::2])
print(text[::-1])
