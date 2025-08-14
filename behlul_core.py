import json
import random
import datetime

class Behlul:
    def _init_(self):
        self.moduller = {}
        self.gecmis_testler = []
        self.pin_kodu = "3947"  # PIN koruması için örnek

    def pin_dogrula(self, girilen_pin):
        return girilen_pin == self.pin_kodu

    def modul_ekle(self, ad, strateji_fonksiyonu):
        self.moduller[ad] = strateji_fonksiyonu

    def strateji_calistir(self, ad, veri):
        if ad in self.moduller:
            return self.moduller[ad](veri)
        return "Modül bulunamadı."

    def laboratuvar_testi(self, veri_seti):
        sonuc = {}
        for ad, fonk in self.moduller.items():
            try:
                skor = fonk(veri_seti)
                sonuc[ad] = skor
                self.gecmis_testler.append({
                    "modul": ad,
                    "tarih": str(datetime.datetime.now()),
                    "skor": skor
                })
            except Exception as e:
                sonuc[ad] = f"Hata: {str(e)}"
        return sonuc

    def modul_oner(self):
        if not self.gecmis_testler:
            return "Henüz test verisi yok."
        skorlar = {}
        for test in self.gecmis_testler:
            ad = test["modul"]
            skorlar[ad] = skorlar.get(ad, 0) + test["skor"]
        sirali = sorted(skorlar.items(), key=lambda x: x[1], reverse=True)
        return [modul for modul, _ in sirali[:3]]

# Örnek modül fonksiyonu
def basit_strateji(veri):
    return sum(veri) / len(veri)

# Kullanım
behlul = Behlul()
behlul.modul_ekle("Basit Ortalama", basit_strateji)

# PIN doğrulama örneği
if behlul.pin_dogrula("3947"):
    test_sonucu = behlul.laboratuvar_testi([10, 20, 30])
    print("Test Sonucu:", test_sonucu)
    print("Modül Önerisi:", behlul.modul_oner())
else:
    print("PIN doğrulama başarısız.")
