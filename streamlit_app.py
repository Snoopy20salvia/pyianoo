import streamlit as st

st.title("via in pixels 🦦")
st.write("just a small space to share some thoughts and ideas."
)
st.image("51682c20b649d9604f842cf837b88926.jpg", width=200)
st.write("\n")
st.write("a cute little puppy")
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
