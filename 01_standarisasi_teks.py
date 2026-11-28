# ============================================================
# TAHAP 1 - STANDARISASI TEKS
# Tujuan : merapikan spasi berlebih dan menyamakan format huruf
#          agar kategori yang sama terbaca konsisten.
# Input  : cybersecurity_threat_detection_logs.csv (data mentah)
# Output : 01_hasil_standarisasi_teks.csv
# ============================================================
import os
import pandas as pd

FOLDER = os.path.dirname(os.path.abspath(__file__))

# Baca data mentah
df = pd.read_csv(os.path.join(FOLDER, "cybersecurity_threat_detection_logs.csv"), sep=";")

# Semua kolom teks: hapus spasi berlebih di awal/akhir dengan str.strip()
kolom_teks = ["source_ip", "dest_ip", "protocol", "action",
              "threat_label", "log_type", "user_agent", "request_path"]
for k in kolom_teks:
    df[k] = df[k].str.strip()

# Kolom kategori: samakan format huruf dengan str.title()
# (IP, user_agent, dan request_path tidak di-title agar isinya tidak rusak)
kolom_kategori = ["protocol", "action", "threat_label", "log_type"]
for k in kolom_kategori:
    df[k] = df[k].str.title()

# Simpan hasil tahap ini (index=False agar index tidak jadi kolom baru)
df.to_csv(os.path.join(FOLDER, "01_hasil_standarisasi_teks.csv"), index=False)
print("Selesai. Ukuran data:", df.shape)
