import streamlit as st
import importlib

# Sayfa ayarları
st.set_page_config(page_title="Behlül Komut Paneli", layout="centered", page_icon="🧠")

st.title("🧠 Behlül Komut Ekranı")
st.markdown("Modül tetikleme ve test için sade mobil arayüz.")

# Behlül çekirdeğini yükle
try:
    behlul_core = importlib.import_module("behlul_core")
    behlul = behlul_core.Behlul()
    behlul.modul_ekle("Basit_Strateji", behlul_core.basit_strateji)
    behlul.modul_ekle("Rastgele_Strateji", behlul_core.rastgele_strateji)
except Exception as e:
    st.error(f"Çekirdek modül yüklenemedi: {e}")
    st.stop()

# Komut ekranı
veri = st.number_input("Veri girin", value=10)
veri_seti = st.text_input("Veri seti (virgülle):", value="12,18,25")
veri_listesi = [int(x.strip()) for x in veri_seti.split(",") if x.strip().isdigit()]

if st.button("🧪 Test Et"):
    sonuc = behlul.laboratuvar_testi(veri, veri_listesi)
    st.write("Test Sonucu:")
    st.json(sonuc)

if st.button("📊 Modül Öner"):
    motor = behlul_core.OneriMotoru(behlul.moduller)
    st.write("Önerilen Modül:")
    st.write(motor.rastgele_oner())
