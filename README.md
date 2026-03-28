# 🏥 MedTalk — Platform Konsultasi Online
**Tugas Project Mata Kuliah: Informatika Medis**

## 1. Pendahuluan
MedTalk adalah prototipe platform telemedicine berbasis **Python** yang dirancang untuk efisiensi administrasi di klinik kecil. Sistem ini memungkinkan pasien melakukan pendaftaran mandiri dan mendapatkan bantuan diagnosa awal secara digital.

## 2. Diagram Arsitektur Sistem 
Sistem ini menggunakan arsitektur **Modern Web App** berbasis Python:
* **User Interface:** Menggunakan framework **Streamlit** untuk tampilan dashboard yang responsif.
* **Logic Control:** Pemrosesan data pasien dan logika diagnosa menggunakan bahasa pemrograman **Python**.
* **Data Storage:** Penyimpanan data sementara (Session State) untuk manajemen antrean pasien dan dokter.

## 3. Komponen Utama Sistem 
1.  **Dashboard Manajemen Pasien:** Input data identitas dan alamat pasien secara digital.
2.  **Informasi Dokter:** Database jadwal dan spesialisasi dokter yang bertugas di klinik.
3.  **Sistem Pendukung Keputusan Klinis (SPKK):** Fitur analisis gejala otomatis untuk memberikan rekomendasi diagnosa dan obat awal bagi pasien.

## 4. Alur Kerja Aplikasi (Workflow)
1.  **Input:** Pasien memasukkan nama dan alamat pada menu "Data Pasien".
2.  **Proses:** Sistem menyimpan data dan memberikan konfirmasi keberhasilan.
3.  **Analisis:** Pada menu "Diagnosa", pasien memilih gejala (Gatal, Ruam, Demam, dsb).
4.  **Output:** Python memproses logika `if-else` untuk memunculkan diagnosa medis dan rekomendasi obat secara real-time.

## 5. Kreativitas & Teknologi 
Project ini menggunakan **Streamlit Cloud Ready** architecture, yang memungkinkan aplikasi dideploy menjadi link website aktif, memberikan kemudahan akses bagi pengguna tanpa perlu instalasi rumit.

**Disusun Oleh:**
* **Nama:** Ifa Uswatul Ummah
* **NIM:** 2417052801004
* **Program Studi:** Informatika Medis