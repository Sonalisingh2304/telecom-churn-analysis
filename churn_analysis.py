import pandas as pd

# load dataset
df = pd.read_csv("telco_Churn_7k.csv")

# first look
print(df.head())

print("\nShape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nInfo:")
print(df.info())

# check missing values
missing_values = df.isnull().sum()
print("\nMissing Values per Column:\n", missing_values)

# 4. Check data types of each column
print("\nData Types of Columns:\n")
print(df.dtypes)

# Churn distribution
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True) * 100)

# churn count
churn_counts = df['Churn'].value_counts()
print("\nChurn Counts:\n", churn_counts)

# churn percentage
churn_percent = df['Churn'].value_counts(normalize=True) * 100
print("\nChurn Percentage:\n", churn_percent)

# Churn vs Gender
print("\nChurn vs Gender:\n")
print(pd.crosstab(df['gender'], df['Churn'], normalize='index') * 100)

# Churn vs Partner
print("\nChurn vs Partner:\n")
print(pd.crosstab(df['Partner'], df['Churn'], normalize='index') * 100)

# Churn vs Senior Citizen
print("\nChurn vs Senior Citizen:\n")
print(pd.crosstab(df['SeniorCitizen'], df['Churn'], normalize='index') * 100)

# Churn vs Dependents
print("\nChurn vs Dependents:\n")
print(pd.crosstab(df['Dependents'], df['Churn'], normalize='index') * 100)

# churn by contract type
churn_by_contract = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
print("\nChurn by Contract (%):\n", churn_by_contract)

# Churn vs Tenure 
print("\nChurn vs Tenure Summary:\n")
print(df.groupby('Churn')['tenure'].describe())

# Churn vs Phone Service
print("\nChurn vs Phone Service:\n")
print(pd.crosstab(df['PhoneService'], df['Churn'], normalize='index') * 100)

# Churn vs Internet Service
print("\nChurn vs Internet Service:\n")
print(pd.crosstab(df['InternetService'], df['Churn'], normalize='index') * 100)

# Churn vs Online Security
print("\nChurn vs Online Security:\n")
print(pd.crosstab(df['OnlineSecurity'], df['Churn'], normalize='index') * 100)

# Churn vs Online Backup
print("\nChurn vs Online Backup:\n")
print(pd.crosstab(df['OnlineBackup'], df['Churn'], normalize='index') * 100)

# Churn vs Device Protection
print("\nChurn vs Device Protection:\n")
print(pd.crosstab(df['DeviceProtection'], df['Churn'], normalize='index') * 100)

# Churn vs Tech Support
print("\nChurn vs Tech Support:\n")
print(pd.crosstab(df['TechSupport'], df['Churn'], normalize='index') * 100)

# Churn vs Streaming TV
print("\nChurn vs Streaming TV:\n")
print(pd.crosstab(df['StreamingTV'], df['Churn'], normalize='index') * 100)

# Churn vs Streaming Movies
print("\nChurn vs Streaming Movies:\n")
print(pd.crosstab(df['StreamingMovies'], df['Churn'], normalize='index') * 100)

# Churn vs Paperless Billing
print("\nChurn vs Paperless Billing:\n")
print(pd.crosstab(df['PaperlessBilling'], df['Churn'], normalize='index') * 100)

# Churn vs Payment Method
print("\nChurn vs Payment Method:\n")
print(pd.crosstab(df['PaymentMethod'], df['Churn'], normalize='index') * 100)

# save summary
churn_by_contract.to_csv("churn_by_contract.csv")
