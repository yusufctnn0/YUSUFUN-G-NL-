from dataclasses import replace


yazi = 'benim adım Yusuf Çetin,Mardinde yaşıyorum'

#sonuc=yazi.upper() #bütün kelimeleri büyük yazar.
#sonuc=yazi.lower() #bütün kelimeleri küçük yapar.
#sonuc=yazi.title() #kelimelerin başlarını büyük yapar.
#sonuc=yazi.capitalize() #cümlenin ilk harfini büyük olarak değiştirir.
#sonuc=yazi.islower() # is soru eki olduğu için burda harflerin hepsi küçük mü diye sorduk.
# sonuc=yazi.isupper() #burda da hepsi büyük mü diye sorduk.
#sonuc=yazi.strip() #strip ise cümlenin başında ve sonunda olan boşluğu kaldırıyor.
#sonuc=yazi.split(',') #burda ise cümleyi kelimelere bölüyor. ve isteğimiz yerden de bölebiliriz
#sonuc='-'.join(yazi) #burda da her harfin başına tire(-) koymasını istiyoruz.
#sonuc=yazi.index('Yusuf') #burda da yazımızın içinde bu kelime geçiyor mu diye kontrol edeceğiz geçiyorsa kaçıncı indexte başlıyor yazar.
#sonuc=yazi.startswith('b') #burda cümlemimizin hangi harfle başadığını sorgulayabiliyoruz.
# sonuc=yazi.endswith('m') #burda cümlemimizin hangi harfle bittiğini sorgulayabiliyoruz.
# sonuc=yazi.replace('Mardin','almanya') #burda da iteğimiz kelimeyi değiştiryoruz. 
sonuc=yazi.replace('ı','i').replace('ş','s') #burda ise istediğimiz harfi değiştiriyoruz.

print(sonuc) 

