import streamlit as st
import requests

# Sayfa ayarları
st.set_page_config(page_title="Şifre Değiştir", layout="centered")

# Sabit PIN (geliştirme aşamasında)
CORRECT_PIN = "1984"

# Oturum durumu
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "token" not in st.session_state:
    st.session_state.token = None

# PIN doğrulama
def verify_pin(pin_input):
    return pin_input == CORRECT_PIN

# Giriş fonksiyonu
def login(username, password):
    try:
        response = requests.post(
            'https://example.com/api/login',
            json={'username': username, 'password': password}
        )
        response.raise_for_status()
        return response.json().get('token')
    except requests.RequestException as e:
        st.error(f"Giriş başarısız: {e}")
        return None

# Şifre değiştirme fonksiyonu
def change_password(token, new_password):
    try:
        response = requests.post(
            'https://example.com/api/change-password',
            headers={'Authorization': f'Bearer {token}'},
            json={'new_password': new_password}
        )
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        st.error(f"Şifre değiştirilemedi: {e}")
        return False

# Arayüz
st.title("🔐 Şifre Değiştirme Paneli")

# PIN doğrulama ekranı
if not st.session_state.authenticated:
    st.subheader("Private Erişim için PIN Girin")
    pin_input = st.text_input("PIN", type="password")
    if st.button("PIN Doğrula"):
        if verify_pin(pin_input):
            st.session_state.authenticated = True
            st.success("PIN doğrulandı ✅")
        else:
            st.error("PIN hatalı ❌")
    st.stop()

# Giriş ekranı
st.subheader("Kullanıcı Girişi")
username = st.text_input("Kullanıcı Adı")
password = st.text_input("Mevcut Şifre", type="password")

if st.button("Giriş Yap"):
    token = login(username, password)
    if token:
        st.session_state.token = token
        st.success("Giriş başarılı ✅")
    else:
        st.error("Giriş başarısız ❌")

# Şifre değiştirme ekranı
if st.session_state.token:
    st.subheader("Yeni Şifre Belirle")
    new_password = st.text_input("Yeni Şifre", type="password")
    if st.button("Şifreyi Değiştir"):
        if change_password(st.session_state.token, new_password):
            st.success("Şifre başarıyla değiştirildi!")
        else:
            st.error("Şifre değiştirilemedi.")

# Modül önerisi (örnek)
st.markdown("---")
st.caption("🧠 Sistem önerisi: Giriş sonrası kullanıcıya özel modül önerisi sunulabilir.")
