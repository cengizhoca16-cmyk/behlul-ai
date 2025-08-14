import streamlit as st
import importlib
import time

# Sayfa ayarları
st.set_page_config(page_title="Behlül AI", layout="centered", page_icon="🤖", initial_sidebar_state="collapsed")
st.markdown("<style>footer{visibility:hidden;}</style>", unsafe_allow_html=True)

# PIN doğrulama
def pin_dogrula(pin_input):
    return pin_input == "1995"

# Oturum durumu
if "dogrulandi" not in st.session_state:
    st.session_state.dogrulandi = False

# Giriş ekranı
if not st.session_state.dogrulandi:
    st.title("🔐 Behlül AI Giriş")
    pin = st.text_input("PIN kodunu girin", type="password")
    giris = st.button("Giriş Yap")

    if giris and pin_dogrula(pin):
        st.session_state.dogrulandi = True
        st.success("Giriş başarılı ✅")
        time.sleep(1)
    elif giris:
        st.error("PIN hatalı ❌")
    st.stop()

# Mod seçimi
mod = st.radio("Mod Seçimi:", ["🔓 Basit Arayüz", "🔐 Gelişmiş Panel"])

# Behlül çekirdeğini yükle
try:
    behlul_core = importlib.import_module("behlul_core")
    behlul = behlul_core.Behlul()
    behlul.modul_ekle("Basit_Strateji", behlul_core.basit_strateji)
    behlul.modul_ekle("Rastgele_Strateji", behlul_core.rastgele_strateji)
except Exception as e:
    st.error(f"Çekirdek modül yüklenemedi: {e}")
    st.stop()

# 🔓 Basit Arayüz
if mod == "🔓 Basit Arayüz":
    st.title("🤖 Behlül AI Asistanı")
    st.markdown("Modül tetikleme ve test için sade arayüz.")

    if st.button("🔄 Modülü Tetikle"):
        try:
            sonuc = behlul_core.modul_tetikle()
            st.success(f"Modül çalıştı: {sonuc}")
        except Exception as e:
            st.error(f"Hata oluştu: {e}")

    if st.button("🧪 Laboratuvar Testi Başlat"):
        try:
            test_sonucu = behlul_core.laboratuvar_test()
            st.info(f"Test sonucu: {test_sonucu}")
        except Exception as e:
            st.error(f"Test hatası: {e}")

    with st.expander("⚙ Gelişmiş Ayarlar"):
        st.markdown("Buraya ilerde modül kombinasyonu, öneri motoru ve strateji ayarları eklenecek.")

# 🔐 Gelişmiş Panel
else:
    st.title("🤖 Behlül AI Komut Paneli")
    st.markdown("Modül tetikleme, test ve öneri motoru için gelişmiş arayüz.")

    veri = st.number_input("Veri girin", value=12)
    veri_seti = st.text_input("Veri seti (virgülle):", value="10,15,20")
    veri_listesi = [int(x.strip()) for x in veri_seti.split(",") if x.strip().isdigit()]

    if st.button("🧪 Laboratuvar Testi"):
        sonuc = behlul.laboratuvar_testi(veri, veri_listesi)
        st.write("Test Sonuçları:")
        st.json(sonuc)

    if st.button("📊 Öneri Motoru"):
        motor = behlul_core.OneriMotoru(behlul.moduller)
        st.write(motor.rastgele_oner())
        analiz = motor.analiz_et(veri, veri_listesi)
        st.write("Analizler:")
        st.json(analiz)

    if st.button("📁 Test Geçmişi"):
        st.code(behlul.test_ozeti(), language="json")
