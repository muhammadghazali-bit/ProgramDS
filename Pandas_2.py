import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Gunakan format URL "Raw" dari GitHub
url = 'https://raw.githubusercontent.com/Alam-A99/DATAAKSI/main/dataset_fiskal_97_hipoFull.csv'
df = pd.read_csv(url)

print(df.head(11))
print(df.iloc[11:22])

df['no'] = range(1, len(df) + 1)
print(df.head(10))

# Filter khusus untuk Kota Makassar
df_makassar = df[df["Kota"] == "Kota Makassar"]
print(df_makassar)

# Membuat visualisasi tren tingkat kemiskinan
plt.figure(figsize=(10, 5))
sns.lineplot(
    data=df_makassar,
    x="Tahun",
    y="KEMISKINAN",
    marker="o",
    color="crimson",
    linewidth=2.5,
    markersize=8,
)

# Menambahkan judul, label, dan grid
plt.title(
    "Tren Tingkat Kemiskinan di Kota Makassar (2014-2024)",
    fontsize=14,
    fontweight="bold",
    pad=15,
)

plt.xlabel("Tahun", fontsize=11)
plt.ylabel("Tingkat Kemiskinan (%)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)

# Memberikan label angka di setiap titik grafik agar mudah dibaca
for _, row in df_makassar.iterrows():
    plt.annotate(
        f"{row['KEMISKINAN']:.2f}%",
        (row["Tahun"], row["KEMISKINAN"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
    )

plt.tight_layout()
plt.show()