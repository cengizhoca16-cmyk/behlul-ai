import streamlit as st
import time
import importlib

# Sayfa ayarları
st.set_page_config(page_title="Behlül AI", layout="centered", page_icon="🔐", initial_sidebar_state="collapsed")
st.markdown('<style>footer {visibility: hidden;}</style>', unsafe_allow_html=True)

# PIN doğrulama fonksiyonu
def PIN_dogrulama(pin):
    return pin == "1995"

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
    st.write("🎯 Behlül çekirdeği yüklendi.")
except Exception as e:
    st.error(f"Behlül çekirdeği yüklenemedi: {e}")
