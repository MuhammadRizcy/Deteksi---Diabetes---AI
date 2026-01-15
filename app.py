import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(
    page_title="Prediksi Diabetes AI",
    page_icon="🩺",
    layout="centered"
)

# LOAD MODEL 
model = joblib.load('model_deteksi_diabetes.pkl')


# judul
st.title("🩺 Deteksi Dini Diabetes")
st.caption("Model XGBoost dengan Recall Tinggi (Threshold 0.65)")
st.write("---")

# input data
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Jumlah Kehamilan (Pregnancies)', min_value=0, step=1)
    glucose = st.number_input('Glukosa (Glucose)', min_value=0, value=100)
    blood_pressure = st.number_input('Tekanan Darah (BloodPressure)', min_value=0, value=70)
    skin_thickness = st.number_input('Ketebalan Kulit (SkinThickness)', min_value=0, value=20)

with col2:
    insulin = st.number_input('Insulin', min_value=0, value=79)
    bmi = st.number_input('BMI', min_value=0.0, value=30.0)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, value=0.4)
    age = st.number_input('Umur (Age)', min_value=0, value=30)

# logic
if st.button('🔍 Cek Hasil Prediksi'):
    
    # A. Buat DataFrame Awal
    # Urutan kolom harus sama persis dengan data mentah (X) di notebook
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    # 1. Perkalian Fitur (Interaction)
    input_data['BMI_SKIN'] = input_data['BMI'] * input_data['SkinThickness']
    input_data['Glucose_insulin'] = input_data['Glucose'] * input_data['Insulin']
    input_data['Pregnancies_Age'] = input_data['Pregnancies'] * input_data['Age']
    
    # 2. Log Transformation (np.log1p)
    cols_to_log = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                   'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 
                   'BMI_SKIN', 'Glucose_insulin', 'Pregnancies_Age']
    
    for col in cols_to_log:
        input_data[col] = np.log1p(input_data[col])

    # C. PREDIKSI
    try:
        
        probs = model.predict_proba(input_data)[:, 1]
        probabilitas = probs[0]
        
        THRESHOLD = 0.65
        
        # Tampilkan Hasil
        st.write("---")
        st.subheader("Hasil Analisa AI:")
        
        st.write(f"**Skor Risiko:** {probabilitas:.2f}")
        st.progress(float(probabilitas))
        
        if probabilitas >= THRESHOLD:
            st.error(f"🔴 **TERINDIKASI DIABETES**")
            st.warning(f"Skor {probabilitas:.2f} melewati batas {THRESHOLD}. Disarankan cek lab.")
        else:
            st.success(f"🟢 **KEMUNGKINAN SEHAT**")
            st.info(f"Skor {probabilitas:.2f} masih di bawah batas {THRESHOLD}. Pertahankan!")
            
    except Exception as e:
        st.error(f"Terjadi error saat prediksi: {e}")
        st.write("Cek apakah urutan kolom Feature Engineering sudah sama dengan notebook.")


st.write("---")
st.caption("**Disclaimer:** Aplikasi ini adalah alat bantu prediksi berbasis AI (Artificial Intelligence) dan bukan pengganti diagnosis medis profesional. Jika hasil prediksi menunjukkan risiko tinggi, segera konsultasikan dengan dokter.")
