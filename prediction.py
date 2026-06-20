"""
Prediction Script - Employee Attrition Prediction
Jaya Jaya Maju - HR Department

Script ini digunakan untuk memprediksi apakah seorang karyawan
akan mengalami attrition (keluar dari perusahaan) atau tidak.

Penggunaan:
    python prediction.py

Pastikan model sudah dilatih dan tersimpan di folder model/
"""

import joblib
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


def load_model():
    """Load model dan preprocessor yang sudah dilatih."""
    model = joblib.load('model/model.joblib')
    preprocessor = joblib.load('model/preprocessor.joblib')
    return model, preprocessor


def preprocess_input(data_dict, preprocessor):
    """Preprocess input data menggunakan preprocessor yang tersimpan."""
    df = pd.DataFrame([data_dict])

    # Drop kolom yang tidak relevan
    drop_cols = preprocessor['drop_cols']
    existing_drop = [c for c in drop_cols if c in df.columns]
    if existing_drop:
        df = df.drop(columns=existing_drop)

    # Label encoding untuk binary columns
    binary_cols = preprocessor['binary_cols']
    label_encoders = preprocessor['label_encoders']
    for col in binary_cols:
        if col in df.columns:
            le = label_encoders[col]
            df[col] = le.transform(df[col])

    # One-Hot Encoding
    ohe_cols = preprocessor['ohe_cols']
    existing_ohe = [c for c in ohe_cols if c in df.columns]
    df = pd.get_dummies(df, columns=existing_ohe, drop_first=True)

    # Pastikan semua kolom yang dibutuhkan ada
    feature_columns = preprocessor['feature_columns']
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_columns]

    # Scaling
    scaler = preprocessor['scaler']
    num_cols = preprocessor['num_cols_to_scale']
    existing_num = [c for c in num_cols if c in df.columns]
    df[existing_num] = scaler.transform(df[existing_num])

    return df


def predict(model, preprocessor, data_dict):
    """Lakukan prediksi attrition."""
    X = preprocess_input(data_dict, preprocessor)
    probability = model.predict_proba(X)[0]
    
    # Gunakan threshold optimal dari preprocessor jika ada, default 0.5
    threshold = preprocessor.get('threshold', 0.5)
    prediction = 1 if probability[1] >= threshold else 0

    return prediction, probability


def get_sample_data():
    """Contoh data karyawan untuk testing."""
    return {
        'Age': 35,
        'BusinessTravel': 'Travel_Frequently',
        'DailyRate': 800,
        'Department': 'Sales',
        'DistanceFromHome': 15,
        'Education': 3,
        'EducationField': 'Marketing',
        'EnvironmentSatisfaction': 2,
        'Gender': 'Male',
        'HourlyRate': 60,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobRole': 'Sales Executive',
        'JobSatisfaction': 2,
        'MaritalStatus': 'Single',
        'MonthlyIncome': 4500,
        'MonthlyRate': 15000,
        'NumCompaniesWorked': 5,
        'OverTime': 'Yes',
        'PercentSalaryHike': 12,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 2,
        'StockOptionLevel': 0,
        'TotalWorkingYears': 10,
        'TrainingTimesLastYear': 2,
        'WorkLifeBalance': 2,
        'YearsAtCompany': 3,
        'YearsInCurrentRole': 2,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 2
    }


def interactive_input():
    """Input data karyawan secara interaktif melalui terminal."""
    print("\n" + "=" * 60)
    print("INPUT DATA KARYAWAN BARU")
    print("=" * 60)

    data = {}

    data['Age'] = int(input("Age (usia, misal: 35): "))
    data['BusinessTravel'] = input("BusinessTravel (Non-Travel / Travel_Rarely / Travel_Frequently): ")
    data['DailyRate'] = int(input("DailyRate (misal: 800): "))
    data['Department'] = input("Department (Human Resources / Research & Development / Sales): ")
    data['DistanceFromHome'] = int(input("DistanceFromHome (km, misal: 15): "))
    data['Education'] = int(input("Education (1-Below College, 2-College, 3-Bachelor, 4-Master, 5-Doctor): "))
    data['EducationField'] = input("EducationField (Life Sciences / Medical / Marketing / Technical Degree / Other / Human Resources): ")
    data['EnvironmentSatisfaction'] = int(input("EnvironmentSatisfaction (1-Low, 2-Medium, 3-High, 4-Very High): "))
    data['Gender'] = input("Gender (Male / Female): ")
    data['HourlyRate'] = int(input("HourlyRate (misal: 60): "))
    data['JobInvolvement'] = int(input("JobInvolvement (1-Low, 2-Medium, 3-High, 4-Very High): "))
    data['JobLevel'] = int(input("JobLevel (1-5): "))
    data['JobRole'] = input("JobRole (Sales Executive / Research Scientist / Laboratory Technician / Manufacturing Director / Healthcare Representative / Manager / Sales Representative / Research Director / Human Resources): ")
    data['JobSatisfaction'] = int(input("JobSatisfaction (1-Low, 2-Medium, 3-High, 4-Very High): "))
    data['MaritalStatus'] = input("MaritalStatus (Single / Married / Divorced): ")
    data['MonthlyIncome'] = int(input("MonthlyIncome (misal: 4500): "))
    data['MonthlyRate'] = int(input("MonthlyRate (misal: 15000): "))
    data['NumCompaniesWorked'] = int(input("NumCompaniesWorked (misal: 3): "))
    data['OverTime'] = input("OverTime (Yes / No): ")
    data['PercentSalaryHike'] = int(input("PercentSalaryHike (misal: 15): "))
    data['PerformanceRating'] = int(input("PerformanceRating (1-4): "))
    data['RelationshipSatisfaction'] = int(input("RelationshipSatisfaction (1-Low, 2-Medium, 3-High, 4-Very High): "))
    data['StockOptionLevel'] = int(input("StockOptionLevel (0-3): "))
    data['TotalWorkingYears'] = int(input("TotalWorkingYears (misal: 10): "))
    data['TrainingTimesLastYear'] = int(input("TrainingTimesLastYear (misal: 3): "))
    data['WorkLifeBalance'] = int(input("WorkLifeBalance (1-Low, 2-Good, 3-Excellent, 4-Outstanding): "))
    data['YearsAtCompany'] = int(input("YearsAtCompany (misal: 5): "))
    data['YearsInCurrentRole'] = int(input("YearsInCurrentRole (misal: 3): "))
    data['YearsSinceLastPromotion'] = int(input("YearsSinceLastPromotion (misal: 1): "))
    data['YearsWithCurrManager'] = int(input("YearsWithCurrManager (misal: 3): "))

    return data


def main():
    print("=" * 60)
    print("  EMPLOYEE ATTRITION PREDICTION SYSTEM")
    print("  Jaya Jaya Maju - HR Department")
    print("=" * 60)

    # Load model
    try:
        model, preprocessor = load_model()
        print("\n[OK] Model dan preprocessor berhasil dimuat!")
    except FileNotFoundError:
        print("\n[ERROR] Model belum dilatih!")
        print("    Jalankan notebook terlebih dahulu untuk melatih model.")
        return

    # Pilih mode input
    print("\nPilih mode input:")
    print("1. Gunakan data sampel (demo)")
    print("2. Input data manual")

    choice = input("\nPilihan (1/2): ").strip()

    if choice == '2':
        data = interactive_input()
    else:
        data = get_sample_data()
        print("\n--- Menggunakan Data Sampel ---")

    # Prediksi
    prediction, probability = predict(model, preprocessor, data)

    # Tampilkan hasil
    print("\n" + "=" * 60)
    print("  HASIL PREDIKSI")
    print("=" * 60)

    print(f"\n  Data Karyawan:")
    for key, value in data.items():
        print(f"    {key}: {value}")

    print(f"\n  {'-' * 40}")
    if prediction == 1:
        print(f"  [WARNING] PREDIKSI: KARYAWAN BERPOTENSI ATTRITION (KELUAR)")
    else:
        print(f"  [OK] PREDIKSI: KARYAWAN KEMUNGKINAN BERTAHAN")

    print(f"\n  Probabilitas:")
    print(f"    - Bertahan (No Attrition) : {probability[0]*100:.2f}%")
    print(f"    - Keluar   (Attrition)    : {probability[1]*100:.2f}%")
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
