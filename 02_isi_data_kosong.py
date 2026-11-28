# ============================================================
# TAHAP 2 - ISI DATA KOSONG
# Tujuan : mengisi nilai kosong agar tidak mengganggu analisis.
# Input  : 01_hasil_standarisasi_teks.csv
# Output : 02_hasil_isi_data_kosong.csv
# ============================================================
import os
import pandas as pd

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca hasil tahap sebelumnya
df = pd.read_csv(os.path.join(FOLDER, "01_hasil_standarisasi_teks.csv"))

# Kolom request_path yang kosong diisi "unknown"
print("Kosong sebelum diisi:", df["request_path"].isna().sum())
df["request_path"] = df["request_path"].fillna("unknown")
print("Kosong sesudah diisi:", df["request_path"].isna().sum())

# Simpan hasil tahap ini
df.to_csv(os.path.join(FOLDER, "02_hasil_isi_data_kosong.csv"), index=False)
print("Selesai. Ukuran data:", df.shape)
