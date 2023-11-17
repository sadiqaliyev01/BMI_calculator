import streamlit as st

height = float(st.number_input("Boyunuzu daxil edin (metr ilə: "))
mass = int(st.number_input("Kutlenizi daxil edin (kq ilə): "))
age = int(st.number_input("Yashinizi daxil edin: "))
sex = st.text_input("Cinsinizi daxil edin (kişi üçün m, qadın üçün f):")

def vki():
  result = mass/(height*height)
  return result

def funk():
  if vki() < 18.5:
    st.text('''
  Zəif
  Sağlam bir kilo almağa yönəldilməlidir.
  Balanslaşdırılmış qidalanma proqramını qəbul etmək vacibdir.
  Bir məşq proqramı yaratmaqla əzələ kütləsini artırmaq olar.''')

  elif 18.5<=vki()<25:
    st.text('''
  Normal ağırlıq
  Sağlam çəkidə qalmaq üçün balanslı bir pəhriz davam etdirilməlidir.
  Aktiv həyat tərzini saxlamaq vacibdir.
  Daimi məşq ümumi sağlamlığı dəstəkləyə bilər.''')

  elif 25<=vki()<30:
   st.text('''
  Artıq çəkili
  Sağlam kilo itkisi hədəflənməlidir.
  Balanslaşdırılmış pəhriz və idman proqramı həyata keçirilməlidir.
  Dəstək bir həkim və ya diyetoloqdan alına bilər.''')

  elif 30<=vki()<35:
   st.text('''
  Piylənmə (Piylənmə - I tip)
  Nəzarətli çəki itkisi hədəflənməlidir.
  Sağlam bir pəhriz və uzunmüddətli idman proqramını qəbul etmək vacibdir.
  Peşəkar səhiyyə işçisi ilə əməkdaşlıq edilə bilər.''')

  elif 35<=vki()<40:
   st.text('''
  Piylənmə (Piylənmə - II Tip)
  Proqressiv piylənmə halında həkim nəzarəti altında xüsusi sağlamlıq proqramı yaradıla bilər.
  Diyetisyen və ya sağlamlıq mütəxəssisi ilə əməkdaşlıq vacibdir.''')

  elif vki()>=40:
   st.text('''
  Piylənmə (Morbid Piylənmə - Tip III)
  Şiddətli piylənmə hallarında tibb işçiləri tərəfindən idarə olunan xüsusi müalicə planı tələb oluna bilər.
  Cərrahi müdaxilə kimi variantlar nəzərdən keçirilə bilər.''')



st.text(f'Sizin VKI-niz: {vki()}')


if 18<=age<=24:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(18.5 , 24.9, 18.5*(height*height), 24.9*(height*height)))

elif 25<=age<=34:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(18.5 , 24.9, 18.5*(height*height), 24.9*(height*height)))

elif 35<=age<=44:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(18.5 , 24.9, 18.5*(height*height), 24.9*(height*height)))

elif 45<=age<=54:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(18.5 , 24.9, 18.5*(height*height), 24.9*(height*height)))

elif 55<=age<=64:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(18.5 , 24.9, 18.5*(height*height), 24.9*(height*height)))

elif age>=65:
    funk()
    st.text('Sizin yaşınıza görə ideal VKI {} - {} araliginda olmalidir. Sizin ideal kutleniz {} - {} kq arasinda olmalidir'.format(22 , 27, 22*(height*height), 27*(height*height)))


#datalari input ele. vki hesabla. her vki araligina gore neticeni ve mesleheti, yasa ve cinsiyyete gore ideal cekini print ele.
#yas araliqlarina gore vki verilir. bu vki lere gore dusturdan mass tap. minimum maksimum
