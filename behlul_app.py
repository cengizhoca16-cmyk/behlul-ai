import streamlit as st
import importlib
import time

# Sayfa ayarları
st.set_page_config(page_title="Behlül AI", layout="centered", page_icon="🤖", initial_sidebar_state="collapsed")
st.markdown("<style>footer{visibility:hidden;}</style>", unsafe_allow_html=True)

# PIN doğrulama fonksiyonu
def PIN_dogrulama(pin_input):
    try:
        return pin_input == "1995"
    except:
        return False

# Oturum durumu
if "dogrulandi" not in st.session_state:
    st.session_state.dogrulandi = False

# Giriş ekranı
if not st.session_state.dogrulandi:
    st.title("🔐 Behlül AI Giriş")
    pin_input = st.text_input("PIN kodunu girin", type="password", key="pin_input")
    giris = st.button("Giriş Yap")

    if giris:
        if PIN_dogrulama(pin_input):
            st.session_state.dogrulandi = True
            st.success("Giriş başarılı ✅")
            time.sleep(1)
        else:
            st.error("PIN hatalı ❌")
    st.stop()

# Giriş başarılıysa devam et
try:
    behlul_core = importlib.import_module("behlul_core")
    behlul = behlul_core.Behlul()
    behlul.modul_ekle("Basit_Strateji", behlul_core.basit_strateji)
    behlul.modul_ekle("Rastgele_Strateji", behlul_core.rastgele_strateji)
except Exception as e:
    st.error(f"Çekirdek modül yüklenemedi: {e}")
    st.stop()

# Mod seçimi
mod = st.radio("Mod Seçimi:", ["📉 Basit Analiz", "📈 Gelişmiş Panel"])

# 📉 Basit Analiz
if mod == "📉 Basit Analiz":
    st.title("📉 Basit Analiz")
    st.markdown("Modül tetikleme ve test için sade analiz.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Modülü Tetikle"):
            try:
                sonuc = behlul_core.modul_tetikle()
                st.success(f"Modül çalıştı: {sonuc}")
            except Exception as e:
                st.error(f"Hata oluştu: {e}")
    with col2:
        if st.button("🧪 Laboratuvar Testi Başlat"):
            try:
                test_sonucu = behlul_core.laboratuvar_test()
                st.info(f"Test sonucu: {test_sonucu}")
            except Exception as e:
                st.error(f"Test hatası: {e}")

    with st.expander("⚙ Gelişmiş Ayarlar"):
        st.markdown("Buraya ilerde modül kombinasyonu, öneri motoru ve strateji ayarları eklenecek.")

# 📈 Gelişmiş Panel
elif mod == "📈 Gelişmiş Panel":
    st.title("📈 Gelişmiş Panel")
    st.markdown("Gelişmiş analiz ve test için detaylı panel.")

    veri = st.number_input("Veri girin", value=12)
    veri_seti = st.text_input("Veri seti (virgülle):", value="10,15,20")
    try:
        veri_listesi = [int(x.strip()) for x in veri_seti.split(",") if x.strip().isdigit()]
    except:
        st.error("Veri seti hatalı formatta.")
        veri_listesi = []

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🧪 Laboratuvar Testi"):
            try:
                sonuc = behlul.laboratuvar_testi(veri, veri_listesi)
                st.write("Test Sonuçları:")
                st.json(sonuc)
            except Exception as e:
                st.error(f"Test hatası: {e}")

    with col2:
        if st.button("📊 Öneri Motoru"):
            try:
                motor = behlul_core.OneriMotoru(behlul.moduller)
                st.write("📌 Öneri:", motor.rastgele_oner())
                analiz = motor.analiz_et(veri, veri_listesi)
                st.write("📈 Analizler:")
                st.json(analiz)
            except Exception as e:
                st.error(f"Motor hatası: {e}")

    with col3:
        if st.button("📁 Test Geçmişi"):
            try:
                st.code(behlul.test_ozeti(), language="json")
            except Exception as e:
                st.error(f"Özet alınamadı: {e}")
