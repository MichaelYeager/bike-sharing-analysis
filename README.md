Bike Sharing Analysis Dashboard ✨
Deskripsi
Dashboard ini merupakan proyek akhir dari Fundamental Analisis Data menggunakan Python di Dicoding. Proyek ini melakukan analisis data pada Bike Sharing Dataset untuk menemukan pola penyewaan sepeda berdasarkan kondisi cuaca dan waktu (jam kerja vs hari libur).  

Struktur Direktori
/dashboard: Berisi file utama dashboard.py dan data yang telah dibersihkan main_data.csv.  

/data: Berisi dataset asli dalam format .csv (day.csv dan hour.csv).  

notebook.ipynb: File Jupyter Notebook yang berisi proses lengkap Data Wrangling, EDA, dan Visualisasi.  

requirements.txt: Daftar library Python yang dibutuhkan untuk menjalankan proyek.  

url.txt: Link dashboard yang sudah di-deploy ke Streamlit Cloud.  

Setup Environment - Anaconda
Jika kamu menggunakan Anaconda, jalankan perintah berikut:

Bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
Setup Environment - Shell/Terminal
Jika kamu menggunakan terminal biasa/pipenv:

Bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pip install -r requirements.txt
Run Streamlit App
Untuk menjalankan dashboard secara lokal, masuk ke folder dashboard dan jalankan perintah:

Bash
streamlit run dashboard.py
