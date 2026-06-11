import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "dataset/college_student_placement_dataset.csv"
)

# ==========================================
# SHOW DATASET INFO
# ==========================================

print("\nColumns in Dataset:")

print(df.columns)

print("\nPlacement Values:")

print(df["Placement"].unique())

# ==========================================
# REMOVE MISSING VALUES
# ==========================================

df.dropna(inplace=True)

print("\nRemaining Rows:", len(df))

# ==========================================
# CONVERT CATEGORICAL VALUES
# ==========================================

df["Placement"] = df["Placement"].map({
    "Yes": 1,
    "No": 0
})

df["Internship_Experience"] = df[
    "Internship_Experience"
].map({
    "Yes": 1,
    "No": 0
})

df["Academic_Performance"] = df[
    "Academic_Performance"
].map({
    "Excellent": 4,
    "Good": 3,
    "Average": 2,
    "Poor": 1
})

# ==========================================
# SELECT FEATURES
# ==========================================

X = df[[
    "IQ",
    "CGPA",
    "Academic_Performance",
    "Internship_Experience",
    "Extra_Curricular_Score",
    "Communication_Skills",
    "Projects_Completed"
]]

# ==========================================
# TARGET
# ==========================================

y = df["Placement"]

# ==========================================
# SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# TRAIN MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================================
# TEST MODEL
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy, 2))

# ==========================================
# CREATE MODEL FOLDER
# ==========================================

os.makedirs("model", exist_ok=True)

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "model/placement_model.pkl"
)

print("\nModel Saved Successfully ✅")