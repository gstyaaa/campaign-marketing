# ============================================
# IMPORT LIBRARY
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ============================================
# LOAD DATASET
# ============================================

df = pd.read_csv("marketing_campaign.csv", sep="\t")

# ============================================
# DATA UNDERSTANDING
# ============================================

print("===== 5 DATA PERTAMA =====")
print(df.head())

print("\n===== INFO DATASET =====")
print(df.info())

print("\n===== STATISTIK DATA =====")
print(df.describe())

print("\n===== MISSING VALUE =====")
print(df.isnull().sum())

# ============================================
# PREPROCESSING
# ============================================

# Menghapus missing value
df = df.dropna()

# ============================================
# BUSINESS UNDERSTANDING
# ============================================

"""
Tujuan bisnis:
Perusahaan ingin memahami perilaku customer
berdasarkan income dan spending untuk membantu
strategi marketing.
"""

# ============================================
# MODELING - KMEANS CLUSTERING
# ============================================

# Mengambil fitur
X = df[['Income', 'MntWines']]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)

df['Cluster'] = kmeans.fit_predict(X_scaled)

print("\n===== HASIL CLUSTER =====")
print(df[['Income', 'MntWines', 'Cluster']].head())

# ============================================
# VISUALISASI 1 - BAR CHART
# Customer per Education
# ============================================

plt.figure(figsize=(8,5))

df['Education'].value_counts().plot(kind='bar')

plt.title("Jumlah Customer Berdasarkan Education")
plt.xlabel("Education")
plt.ylabel("Jumlah Customer")

plt.savefig("education_distribution.png")
plt.show()

# ============================================
# VISUALISASI 2 - HEATMAP CORRELATION
# ============================================

plt.figure(figsize=(10,6))

corr = df[['Income',
           'MntWines',
           'MntFruits',
           'MntMeatProducts',
           'NumWebPurchases']].corr()

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")
plt.show()

# ============================================
# VISUALISASI 3 - MODELING CLUSTER
# ============================================

plt.figure(figsize=(8,5))

plt.scatter(df['Income'],
            df['MntWines'],
            c=df['Cluster'])

plt.title("Customer Segmentation")
plt.xlabel("Income")
plt.ylabel("Wine Spending")

plt.savefig("customer_segmentation.png")
plt.show()