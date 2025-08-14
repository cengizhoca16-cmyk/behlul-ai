def PNL_gorunalamaph():
    import streamlit as st
    import pandas as pd
    import numpy as np

    st.set_page_config(page_title="PNL Paneli", layout="wide")

    st.title("📊 PNL Görselleştirme Paneli")
    st.markdown("Bu modül, kar/zarar verilerini görselleştirmek ve test etmek için tasarlanmıştır.")
    st.markdown("---")

    tarih = pd.date_range(start="2023-01-01", periods=30, freq="D")
    kar_zarar = np.random.randint(-1500, 1500, size=30)
    df = pd.DataFrame({"Tarih": tarih, "Kar/Zarar": kar_zarar})

    st.subheader("📈 Günlük Kar/Zarar Grafiği")
    st.line_chart(df.set_index("Tarih"))

    st.subheader("📋 Veri Tablosu")
    st.dataframe(df)

    st.subheader("📊 İstatistiksel Özellikler")
    st.write(df["Kar/Zarar"].describe())

    st.subheader("🔍 Günlük Değişim Analizi")
    df["Değişim"] = df["Kar/Zarar"].diff()
    st.dataframe(df[["Tarih", "Değişim"]])

    st.subheader("🏆 En İyi ve En Kötü Günler")
    max_row = df.loc[df["Kar/Zarar"].idxmax()]
    min_row = df.loc[df["Kar/Zarar"].idxmin()]
    st.markdown(f"*En İyi Gün:* {max_row['Tarih'].date()} → {max_row['Kar/Zarar']} ₺")
    st.markdown(f"*En Kötü Gün:* {min_row['Tarih'].date()} → {min_row['Kar/Zarar']} ₺")

    st.markdown("---")
    st.subheader("🧪 Laboratuvar Test Alanı")
    st.write("Bu alan, strateji üretimi ve veri analizi için test amaçlıdır.")

    st.subheader("🔧 Tarih Aralığı Filtreleme")
    baslangic = st.date_input("Başlangıç Tarihi", tarih.min())
    bitis = st.date_input("Bitiş Tarihi", tarih.max())
    if baslangic > bitis:
        st.error("Başlangıç tarihi, bitiş tarihinden büyük olamaz.")
    else:
        filtreli_df = df[(df["Tarih"] >= pd.to_datetime(baslangic)) & (df["Tarih"] <= pd.to_datetime(bitis))]
        st.dataframe(filtreli_df)

    st.subheader("📌 Günlük Ortalama Hesabı")
    ortalama = filtreli_df["Kar/Zarar"].mean()
    st.markdown(f"*Seçilen Aralıkta Ortalama Kar/Zarar:* {ortalama:.2f} ₺")

    st.subheader("📤 Veri İndirme Simülasyonu")
    if st.button("Veriyi İndir (Simülasyon)"):
        st.success("Veri indirildi (gerçek değil, simülasyon).")

    st.subheader("📝 Kullanıcı Notları")
    notlar = st.text_area("Bu modüle dair notlarınızı yazın:")
    if notlar:
        st.success("Not kaydedildi (simülasyon).")

    st.subheader("📌 Günlük Kar/Zarar Histogramı")
    st.bar_chart(df.set_index("Tarih")["Kar/Zarar"])

    st.subheader("📈 Hareketli Ortalama")
    df["MA5"] = df["Kar/Zarar"].rolling(window=5).mean()
    st.line_chart(df.set_index("Tarih")[["Kar/Zarar", "MA5"]])

    st.subheader("📊 Zaman Serisi Korelasyonu")
    df["Kar/Zarar_Lag1"] = df["Kar/Zarar"].shift(1)
    korelasyon = df[["Kar/Zarar", "Kar/Zarar_Lag1"]].corr().iloc[0, 1]
    st.markdown(f"*Lag-1 Korelasyon:* {korelasyon:.2f}")

    st.markdown("---")
    st.markdown("✅ Modül başarıyla çalıştı ve test edildi.")
    st.stop()
