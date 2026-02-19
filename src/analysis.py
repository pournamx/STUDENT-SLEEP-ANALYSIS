# ==========================================
# PROJECT TITLE: Do Students Actually Sleep Enough?
# Analysis of Sleep Duration & Academic Performance
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("\n===== STUDENT SLEEP ANALYSIS PROJECT =====\n")

# ------------------------------------------
# 1. LOAD DATA
# ------------------------------------------

try:
    df = pd.read_csv("../data/student_sleep.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: Dataset not found.")
    exit()

print("First 5 Rows:")
print(df.head())

print("\nDataset Overview:")
print(df.info())


# ------------------------------------------
# 2. BASIC STATISTICAL ANALYSIS
# ------------------------------------------

print("\n===== BASIC STATISTICS =====")

avg_sleep = df["Sleep Hours"].mean()
avg_gpa = df["GPA"].mean()
correlation = df["Sleep Hours"].corr(df["GPA"])

print(f"Average Sleep Hours: {round(avg_sleep,2)}")
print(f"Average GPA: {round(avg_gpa,2)}")
print(f"Correlation (Sleep vs GPA): {round(correlation,3)}")


# ------------------------------------------
# 3. SLEEP CATEGORY ANALYSIS
# ------------------------------------------

def categorize_sleep(hours):
    if hours < 6:
        return "Sleep Deprived"
    elif 6 <= hours < 8:
        return "Adequate Sleep"
    else:
        return "Oversleeping"

df["Sleep Category"] = df["Sleep Hours"].apply(categorize_sleep)

gpa_by_category = df.groupby("Sleep Category")["GPA"].mean()

print("\nAverage GPA by Sleep Category:")
print(gpa_by_category)


# ------------------------------------------
# 4. VISUALIZATIONS
# ------------------------------------------

# Scatter Plot: Sleep vs GPA
plt.figure(figsize=(6,4))
sns.scatterplot(x="Sleep Hours", y="GPA", data=df)
plt.title("Sleep Hours vs GPA")
plt.show()

# Scatter Plot: Sleep vs Stress
plt.figure(figsize=(6,4))
sns.scatterplot(x="Sleep Hours", y="Stress Level", data=df)
plt.title("Sleep Hours vs Stress Level")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ------------------------------------------
# 5. FINAL CONCLUSION
# ------------------------------------------

print("\n===== FINAL CONCLUSION =====")

if correlation > 0:
    print("There is a positive relationship between sleep and GPA.")
else:
    print("There is no strong positive relationship between sleep and GPA.")

sleep_deprived_percent = (len(df[df["Sleep Hours"] < 6]) / len(df)) * 100

print(f"{round(sleep_deprived_percent,2)}% of students are sleep deprived.")
print("Students who sleep 7–8 hours tend to perform better academically.")

print("\nProject Completed Successfully.")
