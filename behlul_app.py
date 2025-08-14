import streamlit as st
import time
import importlib
import os

# --- Ayarlar ---
st.set_page_config(page_title="Behlül AI", layout="centered", page_icon="🤖", initial_sidebar_state="collapsed")
st.markdown("<style>footer{visibility:hidden;}</style>", unsafe_allow_html=True)

# --- PIN Doğrulama ---
def pin_dogrula(pin_input):
    return pin_input == os.getenv("BEHLUL_PIN", "4269")  # Ortam değişkeni varsa onu kullan, yoksa varsayılan

# --- Giriş Ekranı ---
if "dogrulandi" not in st.session_state:
    st.session_state.dogrulandi = False

if not st.session_state.dogrulandi:
    st.title("🔐 Behlül AI Giriş")
    pin = st.text_input("PIN kodunu girin", type="password")
    if st.button("Giriş Yap"):
        if pin_dogrula(pin):
            st.session_state.dogrulandi = True
            st.success("Giriş başarılı ✅")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("PIN hatalı ❌")
    st.stop()

# --- Ana Arayüz ---
st.title("🧠 Behlül AI Asistanı")
st.markdown("Modül tetikleme, test ve strateji üretimi için sade arayüz.")

# --- Modül Yükleme ---
try:
    behlul_core = importlib.import_module("behlul_core")
except ModuleNotFoundError:
    st.error("❗ 'behlul_core.py' dosyası bulunamadı.")
    st.stop()

# --- Modül Tetikleme ---
if st.button("🔄 Modül Tetikle"):
    try:
        sonuc = behlul_core.modul_tetikle()
        st.success(f"Modül çalıştı: {sonuc}")
    except Exception as e:
        st.error(f"Hata oluştu: {e}")

# --- Laboratuvar Testi ---
if st.button("🧪 Laboratuvar Testi Başlat"):
    try:
        test_sonucu = behlul_core.laboratuvar_test()
        st.info(f"Test sonucu: {test_sonucu}")
    except Exception as e:
        st.error(f"Test hatası: {e}")

# --- Gizli Mod ---
with st.expander("⚙ Gelişmiş Ayarlar"):
    st.markdown("Buraya ileride modül kombinasyonu, öneri motoru ve strateji ayarları eklenecek.")
