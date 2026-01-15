# 🩺 Deteksi Dini Diabetes Berbasis AI (XGBoost)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-prediction-rz.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)

Aplikasi berbasis web sederhana untuk memprediksi kemungkinan diabetes secara dini menggunakan Machine Learning (**XGBoost Classifier**).

🔗 **Coba Aplikasi Langsung:** [Klik di sini untuk membuka Web App](https://diabetes-prediction-rz.streamlit.app/)

---

## 📖 Tentang Proyek Ini
Diabetes adalah penyakit kronis yang seringkali terlambat dideteksi. Aplikasi ini dibuat sebagai alat **skrining awal (screening tool)** untuk membantu pengguna mengetahui tingkat risiko mereka berdasarkan parameter kesehatan dasar.

**PENTING:** Aplikasi ini ibarat "Thermometer". Ia memberi peringatan awal, namun **bukan pengganti diagnosis dokter**.

### 🧠 Logika & Model
Model ini dilatih menggunakan dataset **Pima Indians Diabetes Database**.
* **Algoritma:** XGBoost Classifier.
* **Fokus Metrik:** Recall (Sensitivitas). Kami mengutamakan kemampuan model untuk mendeteksi pasien positif (meminimalkan *False Negative*).
* **Threshold:** `0.65` (Model dikonfigurasi agar lebih ketat/waspada dalam memberikan vonis "Sehat").

---

## 📂 Struktur File
* `app.py`: Kode utama aplikasi web (menggunakan framework Streamlit).
* `model_deteksi_diabetes.pkl`: Model Machine Learning yang sudah dilatih dan disimpan.
* `Diabetes.ipynb`: Notebook eksperimen (Data Cleaning, EDA, Preprocessing, Feature Engineering, Training, Evaluasi Model).
* `diabetes.csv`: Dataset yang digunakan untuk melatih model.
* `requirements.txt`: Daftar library Python yang dibutuhkan.

---

## 🛠️ Cara Menjalankan di Komputer Sendiri (Localhost)

Jika Anda ingin menjalankan atau memodifikasi kode ini di laptop Anda:

1.  **Clone Repository ini:**
    ```bash
    git clone [https://github.com/MuhammadRizcy/Deteksi---Diabetes---AI.git](https://github.com/MuhammadRizcy/Deteksi---Diabetes---AI.git)
    ```
2.  **Masuk ke folder:**
    ```bash
    cd Deteksi---Diabetes---AI
    ```
3.  **Install Library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Jalankan Aplikasi:**
    ```bash
    streamlit run app.py
    ```

---

## 📊 Parameter Input
Aplikasi ini membutuhkan input pengguna berupa:
1.  **Pregnancies:** Jumlah kehamilan.
2.  **Glucose:** Tingkat glukosa dalam darah (mg/dL).
3.  **BloodPressure:** Tekanan darah (mm Hg).
4.  **SkinThickness:** Ketebalan lipatan kulit triceps (mm).
5.  **Insulin:** Kadar insulin serum (mu U/ml).
6.  **BMI:** Indeks Massa Tubuh (Berat / Tinggi²).
7.  **DiabetesPedigreeFunction:** Skor riwayat diabetes dalam keluarga (0.0 - 2.5).
8.  **Age:** Umur (tahun).

---

## ⚠️ Disclaimer Medis
Aplikasi ini dikembangkan untuk tujuan **edukasi dan portofolio Data Science**. 
* Hasil prediksi tidak boleh dianggap sebagai saran medis mutlak.
* Model memiliki **keterbatasan akurasi**. Jika hasil prediksi menunjukkan **Positif/Risiko Tinggi**, segera konsultasikan dengan dokter atau lakukan tes laboratorium resmi.

---

Made with ❤️ by **Muhammad Rizcy**
