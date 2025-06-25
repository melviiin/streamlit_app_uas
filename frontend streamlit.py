#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests

st.set_page_config(page_title="Prediksi Obesitas", layout="centered")
st.title("Aplikasi Prediksi Tingkat Obesitas")

# Form input
with st.form("obesity_form"):
    Gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    Age = st.number_input("Umur (tahun)", min_value=1, max_value=120, value=25)
    Height = st.number_input("Tinggi (m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    Weight = st.number_input("Berat (kg)", min_value=20.0, max_value=300.0, value=70.0)
    family_history_with_overweight = st.selectbox("Riwayat Keluarga Obesitas", ["yes", "no"])
    FAVC = st.selectbox("Sering konsumsi makanan tinggi kalori?", ["yes", "no"])
    FCVC = st.slider("Frekuensi konsumsi sayur (1–3)", 1.0, 3.0, 2.0)
    NCP = st.slider("Jumlah makan utama per hari", 1.0, 4.0, 3.0)
    CAEC = st.selectbox("Camilan di antara waktu makan", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Merokok?", ["yes", "no"])
    CH2O = st.slider("Asupan air harian (1–3)", 1.0, 3.0, 2.0)
    SCC = st.selectbox("Pantau kalori yang dikonsumsi?", ["yes", "no"])
    FAF = st.slider("Frekuensi aktivitas fisik (0–3)", 0.0, 3.0, 1.0)
    TUE = st.slider("Waktu penggunaan teknologi (0–3)", 0.0, 3.0, 2.0)
    CALC = st.selectbox("Konsumsi alkohol", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Moda transportasi utama", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])
    
    submitted = st.form_submit_button("Prediksi")

if submitted:
    input_data = {
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)
        if response.status_code == 200:
            pred = response.json()["prediction"]
            st.success(f"Prediksi tingkat obesitas: Label ke-{pred}")
        else:
            st.error("Gagal mendapatkan prediksi dari backend API.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

