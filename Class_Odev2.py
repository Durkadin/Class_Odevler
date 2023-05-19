class Insan():
    def __init__(self, ad="Durkadin", soyad="Zerdali", yas=25, ulke="Turkiye", sehir="Antalya"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenekEkle):
        self.yetenekler.append(yetenekEkle)
        return self


insan = Insan()
insan.yetenek_ekle("C#")
insan.yetenek_ekle("Karakalem")
insan.yetenek_ekle("Ata Binme")
insan.yetenek_ekle("Satranc")
insan.yetenek_ekle("Kayak")
print(insan.kisi_bilgileri())