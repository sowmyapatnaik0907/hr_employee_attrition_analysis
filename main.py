
# ==========================================
# HR EMPLOYEE ATTRITION ANALYSIS
# Step 2: Load Dataset
# ==========================================

import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("hr_attrition_cleaned.csv")

# Display project heading
print("=" * 50)
print("HR EMPLOYEE ATTRITION ANALYSIS")
print("=" * 50)

# Display first 5 records
print("\nFIRST 5 EMPLOYEE RECORDS")
print(df.head())

# Display total rows and columns
print("\nDATASET INFORMATION")
print("Total Employees:", df.shape[0])
print("Total Columns:", df.shape[1])

# Display all column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Display data types
print("\nDATA TYPES")
print(df.dtypes)

# Calculate attrition statistics
total_employees = len(df)

employees_left = len(df[df["Attrition"] == "Yes"])

active_employees = len(df[df["Attrition"] == "No"])

attrition_rate = (employees_left / total_employees) * 100

retention_rate = (active_employees / total_employees) * 100

# Display key metrics
print("\nEMPLOYEE ATTRITION SUMMARY")
print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Active Employees:", active_employees)

print("Attrition Rate:", round(attrition_rate, 2), "%")
print("Retention Rate:", round(retention_rate, 2), "%")

print("\nDATASET LOADED SUCCESSFULLY")

print("=" * 60)
print("HR EMPLOYEE ATTRITION - FACTOR ANALYSIS")
print("=" * 60)


# 1. OVERTIME ANALYSIS
print("\n1. OVERTIME VS ATTRITION")

overtime_analysis = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print(overtime_analysis.round(2))


# 2. JOB SATISFACTION ANALYSIS
print("\n2. JOB SATISFACTION VS ATTRITION")

satisfaction_analysis = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100

print(satisfaction_analysis.round(2))


# 3. DEPARTMENT ANALYSIS
print("\n3. DEPARTMENT-WISE ATTRITION")

department_analysis = df.groupby("Department").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Employees_Left"] /
    department_analysis["Total_Employees"] * 100
)

print(department_analysis.round(2))


# 4. JOB ROLE ANALYSIS
print("\n4. JOB ROLE-WISE ATTRITION")

jobrole_analysis = df.groupby("JobRole").agg(
    Total_Employees=("EmployeeNumber", "count"),
    Employees_Left=("Attrition", lambda x: (x == "Yes").sum())
)

jobrole_analysis["Attrition_Rate"] = (
    jobrole_analysis["Employees_Left"] /
    jobrole_analysis["Total_Employees"] * 100
)

print(jobrole_analysis.sort_values(
    by="Attrition_Rate",
    ascending=False
).round(2))


# 5. MONTHLY INCOME ANALYSIS
print("\n5. MONTHLY INCOME VS ATTRITION")

income_analysis = df.groupby("Attrition")["MonthlyIncome"].mean()

print(income_analysis.round(2))


# 6. AGE GROUP ANALYSIS
print("\n6. AGE GROUP VS ATTRITION")

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 100],
    labels=["18-25", "26-35", "36-45", "46-55", "55+"]
)

age_analysis = pd.crosstab(
    df["AgeGroup"],
    df["Attrition"],
    normalize="index"
) * 100

print(age_analysis.round(2))


# 7. EXPERIENCE ANALYSIS
print("\n7. YEARS AT COMPANY VS ATTRITION")

df["ExperienceGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, 50],
    labels=["0-2 Years", "3-5 Years", "6-10 Years",
            "11-20 Years", "20+ Years"]
)

experience_analysis = pd.crosstab(
    df["ExperienceGroup"],
    df["Attrition"],
    normalize="index"
) * 100

print(experience_analysis.round(2))


# 8. BUSINESS TRAVEL ANALYSIS
print("\n8. BUSINESS TRAVEL VS ATTRITION")

travel_analysis = pd.crosstab(
    df["BusinessTravel"],
    df["Attrition"],
    normalize="index"
) * 100

print(travel_analysis.round(2))


print("\nFACTOR ANALYSIS COMPLETED!")
