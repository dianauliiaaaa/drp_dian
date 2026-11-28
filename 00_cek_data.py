# ============================================================
# TAHAP 0 - CEK DATA MENTAH
# Tujuan : melihat kondisi awal data (ukuran, tipe, nilai kosong,
#          duplikat) sebelum dibersihkan.
# Catatan: tahap ini hanya memeriksa, tidak mengubah data,
#          jadi tidak ada file .csv baru yang disimpan.
# ============================================================
import os
import pandas as pd

# Folder tempat file ini berada (supaya path file selalu benar)
FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca data mentah (pemisah kolom di file ini adalah titik koma)
df = pd.read_csv(os.path.join(FOLDER, "cybersecurity_threat_detection_logs.csv"), sep=";")

# Ukuran data (baris, kolom) dan 5 baris pertama
print("Ukuran data:", df.shape)
print(df.head())

# Tipe data tiap kolom
df.info()

# Jumlah data kosong per kolom
print("\nData kosong per kolom:")
print(df.isna().sum())

# Jumlah baris duplikat
print("\nJumlah duplikat:", df.duplicated().sum())

# Sebaran kolom protocol
print("\nSebaran protocol:")
print(df["protocol"].value_counts())

# Statistik kolom bytes_transferred
print("\nStatistik bytes_transferred:")
print(df["bytes_transferred"].describe().round(2).to_string())
