# Exploratory Data Analysis (EDA) - Cleaned Titanic
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Screenshots folder automatically create karna
os.makedirs("screenshots", exist_ok=True)

# 2. Cleaned Dataset load kiya hai
df = pd.read_csv("cleaned_titanic.csv")

# ==========================
# Basic Information
# ==========================
print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
df.info()

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values Check ---")
print(df.isnull().sum()) 

# ==========================
# Filtering Columns for Plots
# ===========================
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
if 'PassengerId' in numeric_cols:
    numeric_cols = numeric_cols.drop('PassengerId')


# ==========================
# Categorical Analysis (Countplots)
# ==========================
print("\nGenerating Categorical Plots...")

# Overall Survival Count
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', palette='Set1')
plt.title('Overall Survival Count')
plt.savefig("screenshots/countplot_survived.png")
plt.close()

# Survival by Gender 
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', hue='Sex', palette='Set2')
plt.title('Survival by Gender')
plt.savefig("screenshots/countplot_survived_sex.png")
plt.close()

# Survival by Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', hue='Pclass', palette='Set3')
plt.title('Survival by Pclass')
plt.savefig("screenshots/countplot_survived_pclass.png")
plt.close()


# ==========================
# Histograms (Distribution of Data)
# ==========================
print("Generating Histograms...")
for col in numeric_cols:
    plt.figure(figsize=(10,6))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Histogram of {col}')
    plt.tight_layout()
    plt.savefig(f"screenshots/histogram_{col}.png")
    plt.close()


# ==========================
# Boxplots (Outliers Check)
# ==========================
print("Generating Boxplots...")
for col in numeric_cols:
    plt.figure(figsize=(10,6))
    sns.boxplot(x=df[col], color='skyblue')
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.savefig(f"screenshots/boxplot_{col}.png")
    plt.close()


# ==========================
# Correlation Heatmap
# ==========================
print("Generating Heatmap & Pairplot...")
plt.figure(figsize=(10,8))
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("screenshots/correlation_heatmap.png")
plt.close()


# ==========================
# Pairplot
# ============================
pairplot = sns.pairplot(df[numeric_cols])
pairplot.savefig("screenshots/pairplot.png")
plt.close()
print("\nEDA Completed Successfully!")
print("All graphs are saved inside the 'screenshots' folder.")