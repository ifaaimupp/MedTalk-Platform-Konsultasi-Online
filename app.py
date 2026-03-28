import streamlit as st

# Konfigurasi Halaman Browser
st.set_page_config(page_title="MedTalk — Platform Konsultasi Online", layout="centered")

# JUDUL UTAMA (Sudah Diubah)
st.title("🏥 MedTalk — Platform Konsultasi Online")
st.markdown("---")

# Sidebar untuk Menu
st.sidebar.header("Menu Utama")
menu = st.sidebar.selectbox("Pilih Layanan:", ["Data Pasien", "Data Dokter", "Diagnosa & Obat"])

# Identitas Mahasiswa di Sidebar
st.sidebar.markdown("---")
st.sidebar.write("**Disusun Oleh:**")
st.sidebar.text("Nama: Ifa Uswatul Ummah")
st.sidebar.text("NIM: 2417052801004")

if menu == "Data Pasien":
    st.header("📋 Manajemen Pasien")
    nama = st.text_input("Nama Lengkap Pasien")
    alamat = st.text_area("Alamat")
    if st.button("Simpan Data"):
        if nama:
            st.success(f"Data pasien {nama} berhasil masuk ke sistem MedTalk!")
        else:
            st.warning("Mohon isi nama pasien terlebih dahulu.")

elif menu == "Data Dokter":
    st.header("👨‍⚕️ Informasi Dokter")
    st.info("*dr. Andi S.* - Spesialis Penyakit Dalam (Ruang 101)")
    st.info("*dr. Siska M.* - Dokter Umum (Ruang 105)")
    st.info("*dr. Budi H.* - Spesialis Anak (Ruang 103)")

elif menu == "Diagnosa & Obat":
    st.header("🔍 Cek Diagnosa & Obat")
    st.write("Sistem Pendukung Keputusan Klinis Sederhana")
    gejala = st.multiselect("Pilih gejala yang dirasakan:", ["Gatal", "Ruam", "Demam", "Pusing"])
    
    if st.button("Analisis"):
        if "Gatal" in gejala and "Ruam" in gejala:
            st.error("Diagnosa: Alergi Kulit")
            st.success("Rekomendasi Obat: Salep Cetirizine")
        elif "Demam" in gejala:
            st.warning("Diagnosa: Indikasi Flu/Infeksi")
            st.success("Rekomendasi Obat: Paracetamol")
        elif not gejala:
            st.write("Silakan pilih gejala lebih dulu.")
        else:
            st.info("Gejala perlu pemeriksaan lebih lanjut oleh dokter.")