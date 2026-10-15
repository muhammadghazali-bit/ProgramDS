import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats
import plotly.graph_objects as go
import plotly.io as pio

# =========================================================================
# 1. MEMBACA DATA 
url = 'https://raw.githubusercontent.com/Alam-A99/DATAAKSI/main/dataset_fiskal_97_hipoFull.csv'
df_all = pd.read_csv(url)

# Filter khusus untuk Kota Makassar
df = df_all[df_all['Kota'] == 'Kota Makassar'].copy()

print(f"Total data Makassar yang dianalisis: {len(df)} baris.\n")

# =========================================================================
# 2. MODEL REGRESI & UJI ASUMSI KLASIK

X = df[['bm_ekonomi', 'bm_perlindungan_sosial']]
Y = df['PENGANGGURAN']
X_sm = sm.add_constant(X)
model = sm.OLS(Y, X_sm).fit()

# Menampilkan Summary OLS
print(model.summary())

print("\n" + "="*50)
print("FUNGSI REGRESI:")
print(f"Y = {model.params['const']:.4f} + {model.params['bm_ekonomi']:.4f}(BM_Ekonomi) - {abs(model.params['bm_perlindungan_sosial']):.4f}(BM_Sosial)")
print("="*50)

print("\nHASIL UJI ASUMSI KLASIK")
# 1. Normalitas
shapiro_stat, shapiro_p = stats.shapiro(model.resid)
print(f"- Normalitas (Shapiro-Wilk) P-Value: {shapiro_p:.4f} (>=0.05 = Lolos)")

# 2. Multikolinearitas (VIF)
vif_data = pd.DataFrame()
vif_data["Variabel"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(f"- Multikolinearitas (VIF)            : {vif_data['VIF'].max():.4f} (<=10 = Lolos)")

# 3. Heteroskedastisitas
bp_test = sms.het_breuschpagan(model.resid, model.model.exog)
print(f"- Heteroskedastisitas (BP) P-Value   : {bp_test[1]:.4f} (>=0.05 = Lolos)")

# 4. Autokorelasi
dw_value = sm.stats.stattools.durbin_watson(model.resid)
print(f"- Autokorelasi (Durbin-Watson)       : {dw_value:.4f} (Mendekati 2 = Lolos)\n")


# =========================================================================
# 3. VISUALISASI 3D INTERAKTIF

# Membuat grid bidang regresi berdasarkan rentang data asli
x_range = np.linspace(df['bm_ekonomi'].min(), df['bm_ekonomi'].max(), 20)
y_range = np.linspace(df['bm_perlindungan_sosial'].min(), df['bm_perlindungan_sosial'].max(), 20)
x_grid, y_grid = np.meshgrid(x_range, y_range)

# Menghitung prediksi Z untuk permukaan bidang
z_grid = model.params['const'] + (model.params['bm_ekonomi'] * x_grid) + (model.params['bm_perlindungan_sosial'] * y_grid)

# Inisialisasi Plotly Figure
fig = go.Figure()

# Menambahkan Bidang Regresi Permukaan
fig.add_trace(go.Surface(
    x=x_grid,
    y=y_grid,
    z=z_grid,
    name='Bidang Regresi',
    colorscale='viridis',
    opacity=0.8,
    showscale=False
))

# Menambahkan Titik Data Aktual Asli
fig.add_trace(go.Scatter3d(
    x=df['bm_ekonomi'],
    y=df['bm_perlindungan_sosial'],
    z=df['PENGANGGURAN'],
    mode='markers',
    name='Data Aktual',
    marker=dict(size=6, color='red', line=dict(color='white', width=1))
))

# Mengatur Tampilan Layout Grafik
fig.update_layout(
    title=f"Plot Bidang Regresi 3D: Pengangguran terhadap BM Ekonomi & BM Sosial (Makassar) | R² = {model.rsquared:.2f}",
    template='plotly_dark',
    scene=dict(
        xaxis_title='BM Ekonomi',
        yaxis_title='BM Perlindungan Sosial',
        zaxis_title='Pengangguran'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Menampilkan kanvas interaktif
fig.show()



import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.stats.api as sms
from scipy import stats
import plotly.graph_objects as go


# input dataset
url = 'https://raw.githubusercontent.com/Alam-A99/DATAAKSI/main/dataset_fiskal_97_hipoFull.csv'
df_all = pd.read_csv(url)

# Filter khusus untuk Kota Makassar
df = df_all[df_all['Kota'] == 'Kota Makassar'].copy()


# ======================================================================================
# REGRESI LINEAR 2 VARIABEL (BM EKONOMI vs PENGANGGURAN)
# ======================================================================================

# 1. Menentukan Variabel (1 Independen X, 1 Dependen Y)
X_2v = df[['bm_ekonomi']]
Y_2v = df['PENGANGGURAN']

# Menambahkan konstanta dan melatih model
X_2v_sm = sm.add_constant(X_2v)
model_2v = sm.OLS(Y_2v, X_2v_sm).fit()

# 2. Output Ringkasan Model & Persamaan Regresi
print("="*50)
print("HASIL REGRESI 2 VARIABEL")
print("="*50)
print(model_2v.summary())

print("\n" + "="*50)
print("FUNGSI REGRESI 2 VARIABEL:")
print(f"Y = {model_2v.params['const']:.4f} + {model_2v.params['bm_ekonomi']:.4f}(BM_Ekonomi)")
print("="*50)

# 3. Uji Asumsi Klasik 
print("\nHASIL UJI ASUMSI KLASIK:")
shapiro_stat, shapiro_p = stats.shapiro(model_2v.resid)
print(f"- Normalitas (Shapiro-Wilk) P-Value: {shapiro_p:.4f} (>=0.05 = Lolos)")

bp_test = sms.het_breuschpagan(model_2v.resid, model_2v.model.exog)
print(f"- Heteroskedastisitas (BP) P-Value   : {bp_test[1]:.4f} (>=0.05 = Lolos)")

dw_value = sm.stats.stattools.durbin_watson(model_2v.resid)
print(f"- Autokorelasi (Durbin-Watson)       : {dw_value:.4f} (Mendekati 2 = Lolos)\n")


# 4. Visualisasi Grafik 2D Interaktif (Scatter Plot + Garis Regresi)
x_line = np.linspace(df['bm_ekonomi'].min(), df['bm_ekonomi'].max(), 100)
y_line = model_2v.params['const'] + (model_2v.params['bm_ekonomi'] * x_line)

fig_2d = go.Figure()

# Titik Data Aktual
fig_2d.add_trace(go.Scatter(
    x=df['bm_ekonomi'],
    y=df['PENGANGGURAN'],
    mode='markers',
    name='Data Aktual',
    marker=dict(size=10, color='red', line=dict(color='white', width=1))
))

# Garis Regresi Linear
fig_2d.add_trace(go.Scatter(
    x=x_line,
    y=y_line,
    mode='lines',
    name='Garis Regresi',
    line=dict(color='#00CC96', width=3)
))

# Layout Tampilan 2D
fig_2d.update_layout(
    title=f"Plot Regresi 2D: BM Ekonomi vs Pengangguran | R² = {model_2v.rsquared:.2f}",
    template='plotly_dark',
    xaxis_title='BM Ekonomi (X)',
    yaxis_title='Pengangguran (Y)',
    margin=dict(l=40, r=40, b=40, t=50)
)

# Menampilkan kanvas interaktif
fig_2d.show()