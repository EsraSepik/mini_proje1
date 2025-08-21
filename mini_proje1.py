
class Hayvan:
    def __init__(self,isim,yas,cinsiyet):
        self.isim = isim
        self.yas = yas
        self.cinsiyet = cinsiyet


    def ses_çıkar(self):
        return "Hayvan ses cıkarıyor."

    def hareket_et(self):
        return "Hayvan hareket ediyor."

    def yemek_ye(self):
        return "Hayvan yemek yiyor."

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş:{self.yas}, Cinsiyet:{self.cinsiyet}"


class Köpek(Hayvan):
    def __init__(self,isim,yas,cinsiyet,irk,egitim_durumu):
        super().__init__(isim,yas,cinsiyet)
        self.irk = irk
        self.egitim_durumu = egitim_durumu

    def ses_çıkar(self):
        return "Hav! sesi çıkarır."

    def egitim_durumu_goster(self):
        return f"{self.isim} isimli köpeğin eğitim durumu: {self.egitim_durumu}"

class Kus(Hayvan):
    def __init__(self,isim,yas,cinsiyet,kanat_açıklığı,ucmak):
        super().__init__(isim,yas,cinsiyet)
        self.kanat_acıklıgı = kanat_açıklığı
        self.ucmak = ucmak

    def ses_cıkar(self):
        return "Cik cik! sesi cıkarır."

    def ucma_durumu(self):
        if(self.ucmak):
            return f"{self.isim}: uçabiliyor"
        else:
            return f"{self.isim}: uçamıyor"

class At(Hayvan):

    def __init__(self,isim,yas,cinsiyet,yarısı_sevme,hız):
        super().__init__(isim,yas,cinsiyet)
        self.yarısı_sevme = yarısı_sevme
        self.hız = hız

    def ses_cıkar(self):
        return "Brushh! sesi cıkarır."

    def yarısa_hazır_mı(self):
        if self.yarısı_sevme:
            return f"{self.isim} yarısa hazır!"
        else:
            return f"{self.isim} yarısa hazır degil"


    def hız_bilgisi(self):
        return f"{self.isim} şu anda {self.hız} km/s hızla koşuyor."

kopek = Köpek("Latte",3,"Kız","Süs Kopegi","Eğitimli")
at = At("Kara",2,"Erkek",True,50)
kus = Kus("Abdülrezzak",4,"Erkek",50,True)

print(kopek.bilgileri_goster())
print(kopek.ses_çıkar())
print(kopek.egitim_durumu_goster())

print("\n")

print(kus.bilgileri_goster())
print(kus.ses_cıkar())
print(kus.ucma_durumu())

print("\n")

print(at.bilgileri_goster())
print(at.ses_cıkar())
print(at.yarısa_hazır_mı())
print(at.hız_bilgisi())

