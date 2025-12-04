import streamlit as st import numpy as np import sympy as sp import
matplotlib.pyplot as plt

st.set_page_config( page_title=“Function & Derivative Plotter”,
layout=“wide”, page_icon=“📈”, )

st.markdown(““”
“““, unsafe_allow_html=True)

st.markdown(“

📈 Function & Derivative Visualizer

“, unsafe_allow_html=True) st.write(”Masukkan fungsi matematika, lalu
lihat grafik fungsi dan turunannya secara langsung!“)

with st.sidebar: st.header(“⚙ Pengaturan Input”) function_text =
st.text_input( “Masukkan fungsi f(x):”, value=“x2”, help=“Contoh:
sin(x), exp(x), x3 - 2*x” )

    range_min = st.number_input("Range Minimum (x)", value=-10)
    range_max = st.number_input("Range Maximum (x)", value=10)

    num_points = st.slider("Jumlah titik (resolusi)", 200, 2000, 500)

x = sp.symbols(“x”)

try: func = sp.sympify(function_text) derivative = sp.diff(func, x)

    st.markdown("### 🧮 Turunan Simbolik f'(x)")
    st.latex(sp.latex(derivative))

    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("📘 Grafik Fungsi f(x)")
        fig1, ax1 = plt.subplots()
        ax1.plot(x_vals, y_vals, label="f(x)")
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        st.pyplot(fig1)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("📕 Grafik Turunan f'(x)")
        fig2, ax2 = plt.subplots()
        ax2.plot(x_vals, dy_vals, label="f'(x)")
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        st.pyplot(fig2)
        st.markdown("</div>", unsafe_allow_html=True)

except Exception as e: st.error(“⚠ Terjadi kesalahan saat memproses
fungsi. Periksa kembali input Anda.”) st.error(str(e))
