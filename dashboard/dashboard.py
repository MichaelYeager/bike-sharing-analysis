import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Konfigurasi Dasar
st.set_page_config(page_title="Bike Sharing Analysis Dashboard", layout="wide")
sns.set(style='dark')

# 1. Load Data Aman
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "main_data.csv")
except NameError:
    file_path = "main_data.csv"

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
    
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=df["dteday"].min(),
        max_value=df["dteday"].max(),
        value=[df["dteday"].min(), df["dteday"].max()]
    )

main_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & 
            (df["dteday"] <= pd.to_datetime(end_date))]

# 3. Header & Metrics
st.title("Bike Sharing Performance Dashboard 🚲")
st.markdown(f"**Nama:** Michael Hartadi Ginting | **ID:** CDCC319D6Y1761")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=main_df.cnt.sum())
with col2:
    st.metric("Rata-rata Harian", value=round(main_df.cnt.mean()))
with col3:
    st.metric("Puncak Sewa (Data Terpilih)", value=main_df.cnt.max())

st.markdown("---")

# 4. Visualisasi Pertanyaan 1: Pengaruh Cuaca
st.subheader("1. Dampak Kondisi Cuaca terhadap Rata-rata Penyewaan")
fig, ax = plt.subplots(figsize=(10, 5))
weather_res = main_df.groupby("weathersit")["cnt"].mean().sort_values(ascending=False).reset_index()
sns.barplot(x="cnt", y="weathersit", data=weather_res, palette="viridis", ax=ax)
ax.set_xlabel("Rata-rata Penyewaan")
ax.set_ylabel(None)
st.pyplot(fig)

# 5. Visualisasi Pertanyaan 2: Pola Jam (WAJIB ADA)
# Pastikan main_data.csv adalah data dari hour_df (memiliki kolom 'hr' dan 'workingday')
st.subheader("2. Pola Penyewaan per Jam: Hari Kerja vs Hari Libur")
if 'hr' in main_df.columns:
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="hr", y="cnt", hue="workingday", data=main_df, palette="Set1", ax=ax2)
    ax2.set_xlabel("Jam (0-23)")
    ax2.set_ylabel("Rata-rata Penyewaan")
    ax2.set_xticks(range(0, 24))
    st.pyplot(fig2)
    st.info("Keterangan: (1) Hari Kerja | (0) Hari Libur/Weekend")
else:
    st.warning("Kolom 'hr' tidak ditemukan. Harap simpan data 'hour_df' ke dalam main_data.csv!")

# 6. Footer
st.caption(f"Copyright (c) 2026 Michael Hartadi Ginting")
