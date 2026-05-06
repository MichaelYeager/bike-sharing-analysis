import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Konfigurasi Dasar
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style='dark')

# 1. Load Data Aman
# Menggunakan logika agar bisa jalan di Lokal, Streamlit Cloud, atau Colab
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "main_data.csv")
except NameError:
    file_path = "main_data.csv"

# Memastikan file ada sebelum dibaca
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
else:
    st.error(f"File {file_path} tidak ditemukan. Pastikan sudah upload main_data.csv!")
    st.stop()

# 2. Sidebar Filter
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.header("Filter Rentang Waktu")
    
    # Mengambil filter tanggal
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=df["dteday"].min(),
        max_value=df["dteday"].max(),
        value=[df["dteday"].min(), df["dteday"].max()]
    )

# Filter dataframe utama
main_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & 
            (df["dteday"] <= pd.to_datetime(end_date))]

# 3. Header & Metrics
st.title("Bike Sharing Analysis Dashboard 🚲")
st.markdown(f"Menampilkan data dari **{start_date}** hingga **{end_date}**")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=main_df.cnt.sum())
with col2:
    st.metric("Rata-rata Harian", value=round(main_df.cnt.mean()))
with col3:
    st.metric("Penyewaan Tertinggi", value=main_df.cnt.max())

st.markdown("---")

# 4. Visualisasi: Pengaruh Cuaca (Menjawab Pertanyaan Bisnis 1)
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="weathersit", 
    y="cnt", 
    data=main_df, 
    palette="viridis", 
    ax=ax,
    ci=None # Menampilkan rata-rata sesuai saran reviewer
)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig)

# 5. Visualisasi: Tren Harian (Opsional untuk pelengkap)
st.subheader("Tren Penyewaan Harian")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(main_df["dteday"], main_df["cnt"], color="#2E86C1", linewidth=2)
plt.xticks(rotation=45)
st.pyplot(fig)

# 6. Footer
st.caption(f"Copyright (c) 2026 Michael Hartadi Ginting - CDCC319D6Y1761")
