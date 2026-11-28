# ============================================================
# TAHAP 3 - HAPUS DUPLIKAT
# Tujuan : menghapus baris yang sama persis. Dilakukan setelah
#          teks distandarisasi supaya duplikat yang tadinya
#          "tersembunyi" (beda spasi/huruf) ikut terdeteksi.
# Input  : 02_hasil_isi_data_kosong.csv
# Output : 03_hasil_hapus_duplikat.csv
# ============================================================
import os
import pandas as pd

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca hasil tahap sebelumnya
df = pd.read_csv(os.path.join(FOLDER, "02_hasil_isi_data_kosong.csv"))

# Hitung dan hapus duplikat
print("Jumlah duplikat:", df.duplicated().sum())
df = df.drop_duplicates()
print("Ukuran data setelah hapus duplikat:", df.shape)

# Simpan hasil tahap ini
df.to_csv(os.path.join(FOLDER, "03_hasil_hapus_duplikat.csv"), index=False)
