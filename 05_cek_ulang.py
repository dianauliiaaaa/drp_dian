# ============================================================
# TAHAP 5 - CEK ULANG DATA BERSIH
# Tujuan : memastikan data final sudah bersih (tidak ada kosong,
#          tidak ada duplikat, tipe data sudah benar).
# Input  : 04_data_bersih.csv
# Catatan: hanya memeriksa, tidak ada file .csv baru.
# ============================================================
import os
import pandas as pd

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca data bersih; parse_dates agar timestamp terbaca sebagai tanggal
df = pd.read_csv(os.path.join(FOLDER, "04_data_bersih.csv"), parse_dates=["timestamp"])

print("Ukuran data:", df.shape)
print("\nData kosong per kolom:")
print(df.isna().sum())
print("\nJumlah duplikat:", df.duplicated().sum())
print("\nStatistik data:")
print(df.describe())
