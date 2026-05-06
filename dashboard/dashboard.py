import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Page Title
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# 1. Load Data
# Dashboard akan membaca file main_data.csv yang sudah Anda simpan sebelumnya
df = pd.read_csv("main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# 2. Sidebar (Filter)
st.sidebar.header("Filter Data")
start_date, end_date = st.sidebar.date_input(
    "Rentang Waktu",
    [df["dteday"].min(), df["dteday"].max()]
)

# Filter Dataframe berdasarkan input sidebar
main_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & 
            (df["dteday"] <= pd.to_datetime(end_date))]

# 3. Main Dashboard
st.title("Bike Sharing Analysis Dashboard 🚲")

# Layout Kolom untuk Metric
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", main_df.cnt.sum())
with col2:
    st.metric("Rata-rata Harian", round(main_df.cnt.mean()))
with col3:
    st.metric("Penyewaan Maksimum", main_df.cnt.max())

# Visualisasi Tren
st.subheader("Tren Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x="dteday", y="cnt", data=main_df, ax=ax, color="#2E86C1")
plt.xticks(rotation=45)
st.pyplot(fig)

st.caption("Proyek Analisis Data - Michael Hartadi Ginting")
