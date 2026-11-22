import pandas as pd

# 1. Input & pembacaan data
df = pd.read_csv("cybersecurity_threat_detection_logs.csv", sep=";")
print(df.shape)
print(df.head())

# 2. CEK DATA
df.info()
print(df.isna().sum())
print("jumlah duplikat:", df.duplicated().sum())
print(df["protocol"].value_counts())
print(df["bytes_transferred"].describe().round(2).to_string())

# 3. PERBAIKAN DATA
# rapikan spasi di kolom teks
kolom_teks = ["source_ip", "dest_ip", "protocol", "action",
              "threat_label", "log_type", "user_agent", "request_path"]
for k in kolom_teks:
    df[k] = df[k].str.strip()

# isi data kosong
df["request_path"] = df["request_path"].fillna("unknown")

# hapus duplikat (setelah strip)
df = df.drop_duplicates()

# ubah timestamp ke tipe tanggal
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 4. CEK ULANG
print(df.shape)
print(df.isna().sum())
print(df.describe())