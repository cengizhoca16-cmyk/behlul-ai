import json
import random
import datetime

# 🧠 Strateji sınıfı: modül etkisi ve analiz
class Strateji:
    @staticmethod
    def moduli_etkile(deger):
        return round(deger * 1.2, 2)

    @staticmethod
    def moduli_onemli(skor):
        if skor > 25:
            return "🔍 Kritik strateji"
        elif skor > 15:
            return "📈 Orta seviye strateji"
        else:
            return "📊 Düşük etki"

# 🧩 Örnek modül fonksiyonları
def basit_strateji(veri, veri_seti=None):
    ortalama = sum(veri_seti) / len(veri_seti) if veri_seti else 0
    return round((veri + ortalama) * 0.8, 2)

def rastgele_strateji(veri, veri_seti=None):
    return round(random.uniform(10, 30), 2)

# 📱 Mobil öneri motoru
class OneriMotoru:
    def _init_(self, mevcut_moduller):
        self.moduller = mevcut_moduller

    def rastgele_oner(self):
        if not self.moduller:
            return "Modül bulunamadı."
        secim = random.choice(list(self.moduller.keys()))
        return f"📌 Önerilen modül: {secim}"

    def analiz_et(self, veri, veri_seti):
        analiz = {}
        for ad, fonk in self.moduller.items():
            try:
                skor = fonk(veri, veri_seti)
                analiz[ad] = {
                    "skor": skor,
                    "önem": Strateji.moduli_onemli(skor)
                }
            except Exception as e:
                analiz[ad] = f"Hata: {str(e)}"
        return analiz

# 🔐 Behlül çekirdeği
class Behlul:
    def _init_(self):
        self.moduller = {}
        self.gecmis_testler = []
        self.pin_kodu = "3947"

    def pin_dogrula(self, girilen_pin):
        return girilen_pin == self.pin_kodu

    def modul_ekle(self, ad, strateji_fonksiyonu):
        self.moduller[ad] = strateji_fonksiyonu

    def strateji_calistir(self, ad, veri):
        if ad in self.moduller:
            try:
                return self.moduller[ad](veri)
            except Exception as e:
                return f"Hata: {str(e)}"
        return "Modül bulunamadı."

    def laboratuvar_testi(self, veri, veri_seti):
        sonuc = {}
        for ad, fonk in self.moduller.items():
            try:
                skor = fonk(veri, veri_seti)
                sonuc[ad] = {
                    "skor": skor,
                    "tarih": datetime.datetime.now().isoformat()
                }
                self.gecmis_testler.append((ad, skor))
            except Exception as e:
                sonuc[ad] = f"Hata: {str(e)}"
        return sonuc

    def test_ozeti(self):
        return json.dumps(self.gecmis_testler, indent=2)

# 🔄 Basit mod için ek fonksiyonlar
def modul_tetikle():
    return "Modül tetiklendi."

def laboratuvar_test():
    return "Test tamamlandı."

# 🚀 Mobil uyumlu kullanım
if _name_ == "_main_":
    behlul = Behlul()
    behlul.modul_ekle("Basit_Strateji", basit_strateji)
    behlul.modul_ekle("Rastgele_Strateji", rastgele_strateji)

    if behlul.pin_dogrula("3947"):
        print("✅ PIN doğrulama başarılı")

        veri = 12
        veri_seti = [10, 15, 20]

        test_sonuclari = behlul.laboratuvar_testi(veri, veri_seti)
        print("🧪 Test sonuçları:")
        for ad, detay in test_sonuclari.items():
            print(f" - {ad}: {detay}")

        motor = OneriMotoru(behlul.moduller)
        print(motor.rastgele_oner())

        analiz = motor.analiz_et(veri, veri_seti)
        print("📊 Öneri analizleri:")
        for ad, detay in analiz.items():
            print(f" - {ad}: {detay}")

        print("📁 Test geçmişi:")
        print(behlul.test_ozeti())
    else:
        print("❌ PIN doğrulama başarısız")
