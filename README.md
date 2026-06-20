# Proyek Akhir: HR Employee Attrition Analysis - Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih menghadapi kesulitan dalam mengelola karyawan. Hal ini berimbas pada tingginya *attrition rate* (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga mencapai lebih dari 10%. 

Tingginya tingkat pergantian karyawan (attrition) ini dapat menimbulkan biaya operasional yang besar untuk rekrutmen dan pelatihan karyawan baru, hilangnya pengetahuan institusional, serta mengganggu produktivitas tim.

### Permasalahan Bisnis

1. **Mengidentifikasi Faktor Penyebab Attrition**: Mengetahui faktor-faktor utama (seperti lembur, gaji, tingkat kepuasan, status pernikahan, dll.) yang mendorong karyawan untuk keluar dari Jaya Jaya Maju.
2. **Prediksi Risiko Attrition Karyawan**: Membangun model prediktif machine learning untuk mengidentifikasi karyawan yang memiliki risiko tinggi untuk keluar dari perusahaan, sehingga tim HR dapat melakukan intervensi preventif.
3. **Memonitor Metrik Karyawan**: Membuat business dashboard interaktif untuk memantau metrik-metrik HR secara berkala.

### Cakupan Proyek

1. **Eksplorasi Data (EDA)**: Menganalisis korelasi dan visualisasi hubungan antara berbagai fitur dengan status attrition.
2. **Preprocessing Data**: Membersihkan data, menangani missing values, encoding variabel kategorikal, scaling fitur numerik, dan mengatasi class imbalance dengan teknik SMOTE.
3. **Pembuatan Model Machine Learning**: Melatih model klasifikasi menggunakan algoritma *Gradient Boosting Classifier* dan mengoptimalkannya dengan penyesuaian threshold keputusan.
4. **Evaluasi Model**: Menganalisis performa model menggunakan *classification report*, *confusion matrix*, dan kurva *ROC-AUC*.
5. **Penyusunan Solusi Bisnis & Dashboard**: Menyediakan panduan wireframe, kueri SQL, dan langkah-langkah pembuatan dashboard analitik menggunakan Metabase.
6. **Deployment Lokal**: Menyediakan script klasifikasi interaktif (`prediction.py`) untuk menguji data karyawan baru.

### Persiapan

* **Sumber data**: Dataset disediakan di folder `data/employee_data.csv` (terdiri atas 1470 data karyawan dan 35 kolom/fitur). Penjelasan setiap kolom dapat dibaca pada [README.md data](file:///c:/Users/User/Documents/TUGAS%20TI/PORTFOLIO/Projects/JayaMaju/data/README.md).
* **Setup environment**:
  Pastikan Anda telah memasang seluruh pustaka (dependencies) yang dibutuhkan dengan menjalankan perintah berikut:
  ```bash
  pip install -r requirements.txt
  ```

---

## Business Dashboard

Dashboard analitik dibuat menggunakan **Metabase** untuk membantu departemen HR memonitor faktor-faktor yang mempengaruhi *attrition rate*.

### Kredensial Akses Metabase
* **Email / Username**: `root@mail.com`
* **Password**: `root123`

### Struktur Layout Dashboard (Wireframe)
```
┌──────────────────────────────────────────────────────────────────┐
│           JAYA JAYA MAJU - HR ATTRITION DASHBOARD               │
│                                                                  │
├─────────────┬─────────────┬──────────────┬──────────────────────┤
│   CARD 1    │   CARD 2    │   CARD 3     │      CARD 4          │
│ Total Emp.  │ Attrition   │ Attrition    │  Avg Monthly         │
│   1058      │  Count: 179 │  Rate: 16.9% │  Income: $6,503      │
│  (Number)   │  (Number)   │  (Number)    │  (Number)            │
├─────────────┴─────────────┴──────────────┴──────────────────────┤
│                                                                  │
│  ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│  │       CARD 5              │ │         CARD 6               │ │
│  │  Attrition Rate by        │ │  Attrition Rate by           │ │
│  │  Department                │ │  Job Role                    │ │
│  │  (Bar Chart - Grouped)    │ │  (Horizontal Bar Chart)      │ │
│  │                           │ │                              │ │
│  └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                  │
│  ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│  │       CARD 7              │ │         CARD 8               │ │
│  │  Attrition by OverTime    │ │  Attrition by Business       │ │
│  │  (Pie Chart)              │ │  Travel (Bar Chart)          │ │
│  │                           │ │                              │ │
│  └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                  │
│  ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│  │       CARD 9              │ │         CARD 10              │ │
│  │  Attrition by Age Group   │ │  Attrition by Marital        │ │
│  │  (Bar Chart)              │ │  Status (Bar Chart)          │ │
│  │                           │ │                              │ │
│  └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                  │
│  ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│  │       CARD 11             │ │         CARD 12              │ │
│  │  Avg Income: Attrition    │ │  Attrition by Environment    │ │
│  │  vs Retained (Bar)        │ │  Satisfaction (Bar Chart)    │ │
│  │                           │ │                              │ │
│  └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────────┐│
│  │                    CARD 13                                   ││
│  │  Attrition Count by Years at Company (Line Chart)            ││
│  │                                                              ││
│  └──────────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────┘
```

Panduan lengkap mengenai pembuatan kueri SQL, konfigurasi setiap visualisasi card, serta langkah ekspor database kontainer Metabase telah didokumentasikan di berkas: **[DASHBOARD_GUIDE.md](file:///c:/Users/User/Documents/TUGAS%20TI/PORTFOLIO/Projects/JayaMaju/DASHBOARD_GUIDE.md)**.

---

## Machine Learning Model

Proyek ini melatih model klasifikasi untuk memprediksi apakah seorang karyawan berpotensi melakukan *attrition* (keluar).

* **Model Terbaik**: `Gradient Boosting Classifier`
* **Metrik Evaluasi (Data Test)**:
  * **Akurasi**: 81.00%
  * **ROC-AUC**: 0.8045
  * **Attrition Recall**: 42.00% (Dioptimalkan menggunakan threshold kustom `0.30` agar dapat menangkap lebih banyak karyawan yang berisiko keluar).
* **Lokasi Berkas Model**:
  * Model Utama: `model/model.joblib`
  * Preprocessor Pipeline: `model/preprocessor.joblib`

### Penggunaan Script Prediksi (`prediction.py`)

Anda dapat menjalankan sistem prediksi attrition di terminal secara interaktif menggunakan data sampel ataupun input data manual:

```bash
python prediction.py
```

* **Menu Interaktif**:
  1. **Pilih 1**: Menggunakan data sampel karyawan (untuk keperluan demonstrasi).
  2. **Pilih 2**: Memasukkan data karyawan baru secara manual untuk diprediksi langsung oleh model.

---

## Conclusion

Berdasarkan hasil analisis data eksploratif (EDA) dan tingkat kepentingan fitur (*Feature Importance*) dari model Gradient Boosting, berikut beberapa kesimpulan utama mengenai penyebab attrition di Jaya Jaya Maju:

1. **Kompensasi dan Gaji Bulanan (*Monthly Income*)**: Karyawan yang keluar memiliki rata-rata gaji bulanan yang jauh lebih rendah (~$4,787) dibandingkan dengan karyawan yang memilih untuk bertahan (~$6,832). Ini mengindikasikan ketidakpuasan finansial sebagai salah satu faktor pendorong terbesar.
2. **Beban Kerja Lembur (*OverTime*)**: Karyawan yang bekerja lembur (*OverTime = Yes*) memiliki *attrition rate* yang sangat tinggi (sekitar 30%), berbanding terbalik dengan mereka yang tidak lembur (sekitar 10%). Beban kerja yang berlebihan berdampak signifikan pada retensi.
3. **Tingkat Opsi Saham (*Stock Option Level*) & Level Jabatan (*Job Level*)**: Karyawan dengan `StockOptionLevel` dan `JobLevel` yang rendah memiliki tingkat kerentanan attrition tertinggi. Ketiadaan kepemilikan aset perusahaan memperkecil rasa loyalitas.
4. **Masa Kerja Awal (*Years At Company*)**: Attrition paling tinggi terjadi pada rentang **0 hingga 2 tahun pertama** masa kerja. Setelah melewati tahun ke-3, retensi karyawan cenderung lebih stabil.
5. **Kepuasan Lingkungan Kerja (*Environment & Job Satisfaction*)**: Karyawan yang menilai kepuasan lingkungan dan kepuasan kerjanya di angka **1 (Low)** memiliki attrition rate di atas 25%.
6. **Frekuensi Perjalanan Bisnis (*Business Travel*)**: Karyawan yang ditugaskan untuk bepergian dinas secara sering (`Travel_Frequently`) menunjukkan tingkat attrition yang lebih tinggi dibandingkan dengan mereka yang jarang atau tidak bepergian.
7. **Status Pernikahan (*Marital Status*)**: Karyawan berstatus **Single** memiliki tingkat pergantian yang jauh lebih tinggi daripada karyawan yang sudah Married atau Divorced.

---

## Rekomendasi Action Items

Berdasarkan temuan konklusi di atas, berikut adalah 6 rekomendasi strategis konkret bagi manajemen Jaya Jaya Maju untuk menekan *attrition rate* di bawah 10%:

1. **Review Skema Lembur & Kesehatan Karyawan (Pencegahan Burnout)**
   * *Aksi*: Lakukan audit beban kerja dan kurangi lembur yang tidak perlu. Terapkan batas maksimum jam lembur mingguan dan sediakan kompensasi lembur yang lebih adekuat atau opsi insentif libur pengganti (*comp-off*).
2. **Salary Benchmarking & Penyelarasan Gaji Bulanan**
   * *Aksi*: HR harus meninjau ulang struktur gaji, terutama untuk level staf bawah (Job Level 1 & 2). Selaraskan gaji dengan standar pasar (benchmarking eksternal) untuk memastikan karyawan dibayar dengan adil.
3. **Penyempurnaan Struktur Karir & Pembagian Opsi Saham**
   * *Aksi*: Berikan rencana transisi karir yang transparan bagi karyawan baru sejak tahun pertama. Distribusikan program kepemilikan saham (*Stock Option*) dengan skema pencapaian target kerja tertentu untuk retensi jangka panjang.
4. **Penguatan Program Mentoring & Onboarding pada 1 Tahun Pertama**
   * *Aksi*: Sediakan sistem *Buddy* (rekan mentor) bagi karyawan baru di 6 bulan pertama. Lakukan wawancara evaluasi berkala di bulan ke-1, ke-3, dan ke-6 untuk mendeteksi dini masalah adaptasi.
5. **Perbaikan Fasilitas & Budaya Lingkungan Kerja**
   * *Aksi*: Buat survei kepuasan internal secara anonim per triwulan dan tindak lanjuti tim yang memiliki skor kepuasan rendah. Sediakan program fleksibilitas kerja seperti *hybrid working* atau jam kerja fleksibel untuk meningkatkan Work-Life Balance.
6. **Manajemen Penugasan Dinas (*Business Travel Rotation*)**
   * *Aksi*: Sediakan skema rotasi penugasan perjalanan dinas di divisi Sales dan R&D agar beban perjalanan dinas tidak menumpuk pada orang yang sama. Berikan tunjangan dinas luar kota yang menarik sebagai apresiasi.
