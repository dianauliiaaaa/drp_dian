# ============================================================
# TAHAP 4 - UBAH TIPE DATA
# Tujuan : mengubah kolom timestamp dari teks menjadi tipe tanggal.
# Input  : 03_hasil_hapus_duplikat.csv
# Output : 04_data_bersih.csv (data final)
# ============================================================
import os
import pandas as pd

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca hasil tahap sebelumnya
df = pd.read_csv(os.path.join(FOLDER, "03_hasil_hapus_duplikat.csv"))

# Ubah timestamp ke tipe datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])
print(df["timestamp"].dtype)

# Simpan data bersih final
df.to_csv(os.path.join(FOLDER, "04_data_bersih.csv"), index=False)
print("Selesai. Ukuran data:", df.shape)
