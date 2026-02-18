import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

print("🚀 Script Started Successfully!\n")

# ----------------------------
# 1. LOAD DATA
# ----------------------------

df = pd.read_csv("../data/student_sleep.csv")

print("First 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())


# ----------------------------
# 2. BASIC STATISTICS
# ----------------------------

print("\n----- BASIC STATISTICS -----")

print("Average Sleep Hours:", round(df["Sleep Hours"].mean(), 2))
print("Average GPA:", round(df["GPA"].mean(), 2))
print("Minimum Sleep:", df["Sleep Hours"].min())
print("Maximum Sleep:", df["Sleep Hours"].max())


# ----------------------------
# 3. CREATE SLEEP CATEGORIES
# ----------------------------

def categorize_sleep(hours):
    if hours < 6:
        return "Sleep Deprived (<6 hrs)"
    elif 6 <= hours < 8:
        return "Adequate Sleep (6–8 hrs)"
    else:
        return "Oversleeping (8+ hrs)"

df["Sleep Category"] = df["Sleep Hours"].apply(categorize_sleep)


# ----------------------------
# 4. GPA BY SLEEP CATEGORY
# ----------------------------

gpa_by_sleep = df.groupby("Sleep Category")["GPA"].mean()

print("\n----- GPA BY SLEEP CATEGORY -----")
print(gpa_by_sleep)


# ----------------------------
# 5. CORRELATION ANALYSIS
# ----------------------------

correlation = df["Sleep Hours"].corr(df["GPA"])

print("\nCorrelation between Sleep Hours and GPA:",
      round(correlation, 3))

if correlation > 0:
    print("📈 Positive relationship between sleep and academic performance.")
elif correlation < 0:
    print("📉 Negative relationship between sleep and academic performance.")
else:
    print("⚖ No significant relationship found.")


# ----------------------------
# 6. PERCENTAGE OF SLEEP-DEPRIVED STUDENTS
# ----------------------------

total_students = len(df)
sleep_deprived = len(df[df["Sleep Hours"] < 6])

percentage = (sleep_deprived / total_students) * 100

print("\nPercentage of Students Sleeping <6 Hours:",
      round(percentage, 2), "%")


# ----------------------------
# 7. VISUALIZATIONS
# ----------------------------

# 🔹 Sleep vs GPA Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="Sleep Hours", y="GPA", data=df)
plt.title("Sleep Hours vs GPA")
plt.show()


# 🔹 Sleep vs Stress Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="Sleep Hours", y="Stress Level", data=df)
plt.title("Sleep Hours vs Stress Level")
plt.show()


# 🔹 Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# ----------------------------
# 8. FINAL SUMMARY
# ----------------------------

print("\n===== FINAL INSIGHTS =====")
print(f"Average Sleep Duration: {round(df['Sleep Hours'].mean(),2)} hours")
print(f"Average GPA: {round(df['GPA'].mean(),2)}")
print(f"{round(percentage,2)}% of students are sleep deprived.")

if correlation > 0.3:
    print("Strong positive relationship between sleep and performance.")
elif correlation > 0:
    print("Mild positive relationship between sleep and performance.")
else:
    print("Sleep does not strongly predict academic performance in this dataset.")

print("\n✅ Analysis Completed Successfully!")
