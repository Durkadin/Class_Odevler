class Ogrenci():

    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


class Soru(Ogrenci):
    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        net_sayisi = dogru_sayisi - (yanlis_sayisi / 4)
        print("Ogrencinin Yaptigi Net Sayisi :", net_sayisi)
        return self.hesapla(net_sayisi)

    def hesapla(self, net_sayisi):
        puan = net_sayisi * 2
        print("Öğrencinin adi : {}\nÖğrencinin soyadi : {}\nÖğrencinin sinifi {}\nOgrencinin puani : {}".format
              (self.ogrenci_adi, self.ogrenci_soyadi, self.ogrenci_sinif, puan))


ogrenci_adi = str(input("Ogrenci Adini Giriniz:"))
ogrenci_soyadi = str(input("Ogrenci Soyadini Giriniz:"))
ogrenci_sinif = str(input("Ogrenci'nin Sinifini Giriniz :"))
dogru_sayisi = int(input("Ogrenci'nin Sinavdaki Doğru Sayisini Giriniz:"))
yanlis_sayisi = int(input("Ogrenci'nin Sinavdaki Yanlis Sayisini Giriniz:"))
soru_sayisi = dogru_sayisi + yanlis_sayisi
if (soru_sayisi == 50):
    Soru(ogrenci_adi, ogrenci_soyadi, ogrenci_sinif).net_sayisi(dogru_sayisi, yanlis_sayisi)
else:
    print("Girilen Toplam Soru Sayisi Dogru değildir.Sistem'den cikarildiniz!!!!")
    exit()
