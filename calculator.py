import streamlit as st

# Judul aplikasi
st.title("🧮 Kalkulator Sederhana")

# Input angka
a = st.number_input("Masukkan angka pertama:", value=0.0)
b = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilihan operasi
operation = st.radio(
    "Pilih operasi:",
    ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"]
)

# Tombol hitung
if st.button("Hitung"):
    if operation == "Tambah (+)":
        hasil = a + b
    elif operation == "Kurang (-)":
        hasil = a - b
    elif operation == "Kali (×)":
        hasil = a * b
    elif operation == "Bagi (÷)":
        if b == 0:
            st.error("❌ Tidak bisa membagi dengan nol!")
            st.stop()
        hasil = a / b

    st.success(f"📌 **Hasil: {hasil}**")
    
