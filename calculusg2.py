import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Language selection
lang = st.sidebar.selectbox("Language", ["English", "Indonesia"])

if lang == "English":
    texts = {
        "title": "Math Application",
        "function_input": "Enter a function of x (e.g., x**2 + 3*x + 1):",
        "plot_button": "Plot Function",
        "derivative_button": "Compute and Plot Derivative",
        "opt_title": "Optimization Problems",
        "opt_select": "Select a problem:",
        "problems": {
            "area": "Maximize area of a rectangle with fixed perimeter.",
            "perimeter": "Minimize perimeter for fixed area.",
            "volume": "Maximize volume of a box with fixed surface area.",
            "profit": "Maximize profit for a product."
        }
    }
else:
    texts = {
        "title": "Aplikasi Matematika",
        "function_input": "Masukkan fungsi dari x (contoh: x**2 + 3*x + 1):",
        "plot_button": "Plot Fungsi",
        "derivative_button": "Hitung dan Plot Turunan",
        "opt_title": "Masalah Optimasi",
        "opt_select": "Pilih masalah:",
        "problems": {
            "area": "Maksimalkan luas persegi panjang dengan keliling tetap.",
            "perimeter": "Minimalkan keliling untuk luas tetap.",
            "volume": "Maksimalkan volume kotak dengan luas permukaan tetap.",
            "profit": "Maksimalkan keuntungan untuk produk."
        }
    }

st.title(texts["title"])

# Function plotting section
st.header("Function Plotting")
func_str = st.text_input(texts["function_input"], "x**2")

if st.button(texts["plot_button"]):
    try:
        x = sp.symbols('x')
        func = sp.sympify(func_str)
        f = sp.lambdify(x, func, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Plot of Function')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")

# Derivative section
if st.button(texts["derivative_button"]):
    try:
        x = sp.symbols('x')
        func = sp.sympify(func_str)
        deriv = sp.diff(func, x)
        st.write(f"Derivative: {deriv}")
        d = sp.lambdify(x, deriv, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = d(x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel('x')
        ax.set_ylabel("f'(x)")
        ax.set_title('Plot of Derivative')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")

# Optimization section
st.header(texts["opt_title"])
problem = st.selectbox(texts["opt_select"], list(texts["problems"].keys()), format_func=lambda x: texts["problems"][x])

if problem == "area":
    if lang == "English":
        st.write("Maximize area A = x*y, subject to perimeter 2x + 2y = P. Enter P:")
    else:
        st.write("Maksimalkan luas A = x*y, dengan keliling 2x + 2y = P. Masukkan P:")
    P = st.number_input("P", value=20.0)
    x_opt = P / 4
    y_opt = P / 4
    A_max = x_opt * y_opt
    st.write(f"Optimal x: {x_opt}, y: {y_opt}, Max Area: {A_max}")

elif problem == "perimeter":
    if lang == "English":
        st.write("Minimize perimeter P = 2x + 2y, subject to area x*y = A. Enter A:")
    else:
        st.write("Minimalkan keliling P = 2x + 2y, dengan luas x*y = A. Masukkan A:")
    A = st.number_input("A", value=100.0)
    x_opt = np.sqrt(A)
    y_opt = A / x_opt
    P_min = 2 * x_opt + 2 * y_opt
    st.write(f"Optimal x: {x_opt}, y: {y_opt}, Min Perimeter: {P_min}")

elif problem == "volume":
    if lang == "English":
        st.write("Maximize volume V = x*y*z, subject to surface area 2xy + 2xz + 2yz = S. Enter S:")
    else:
        st.write("Maksimalkan volume V = x*y*z, dengan luas permukaan 2xy + 2xz + 2yz = S. Masukkan S:")
    S = st.number_input("S", value=24.0)
    x_opt = np.sqrt(S / 6)
    V_max = x_opt ** 3
    st.write(f"Optimal x=y=z: {x_opt}, Max Volume: {V_max}")

elif problem == "profit":
    if lang == "English":
        st.write("Maximize profit P = 100x - 0.1x^2 - 50, where x is quantity.")
    else:
        st.write("Maksimalkan keuntungan P = 100x - 0.1x^2 - 50, di mana x adalah jumlah.")
    x_opt = 500
    P_max = 100 * 500 - 0.1 * 500 ** 2 - 50
    st.write(f"Optimal x: {x_opt}, Max Profit: {P_max}")
