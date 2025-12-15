import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Language selection
lang = st.sidebar.selectbox("Language", ["English", "Indonesia"])

if lang == "English":
    texts = {
        "title": "Math Application",
        "function_input": "Enter a function of x (e.g., lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot Function",
        "derivative_button": "Compute and Plot Derivative",
        "opt_title": "Optimization Problems",
        "opt_select": "Select a problem:",
        "members_title": "Our Members",
        "members": [
            {"name": "Alice Johnson", "image": "https://via.placeholder.com/100x100?text=Alice"},
            {"name": "Bob Smith", "image": "https://via.placeholder.com/100x100?text=Bob"},
            {"name": "Charlie Brown", "image": "https://via.placeholder.com/100x100?text=Charlie"},
            {"name": "Diana Prince", "image": "https://via.placeholder.com/100x100?text=Diana"}
        ],
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
        "function_input": "Masukkan fungsi dari x (contoh: lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot Fungsi",
        "derivative_button": "Hitung dan Plot Turunan",
        "opt_title": "Masalah Optimasi",
        "opt_select": "Pilih masalah:",
        "members_title": "Anggota Kami",
        "members": [
            {"name": "Alice Johnson", "image": "https://via.placeholder.com/100x100?text=Alice"},
            {"name": "Bob Smith", "image": "https://via.placeholder.com/100x100?text=Bob"},
            {"name": "Charlie Brown", "image": "https://via.placeholder.com/100x100?text=Charlie"},
            {"name": "Diana Prince", "image": "https://via.placeholder.com/100x100?text=Diana"}
        ],
        "problems": {
            "area": "Maksimalkan luas persegi panjang dengan keliling tetap.",
            "perimeter": "Minimalkan keliling untuk luas tetap.",
            "volume": "Maksimalkan volume kotak dengan luas permukaan tetap.",
            "profit": "Maksimalkan keuntungan untuk produk."
        }
    }

# Sidebar: Our Members section
with st.sidebar.expander(texts["members_title"]):
    for member in texts["members"]:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(member["image"], width=50)
        with col2:
            st.write(f"**{member['name']}**")
            st.write("---")  # Separator for visual appeal

st.title(texts["title"])

# Function plotting section
st.header("Function Plotting")
func_str = st.text_input(texts["function_input"], "lambda x: x**2")

if st.button(texts["plot_button"]):
    try:
        # Safely evaluate the lambda function
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Plot of Function')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")

# Derivative section (numerical)
if st.button(texts["derivative_button"]):
    try:
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        # Numerical derivative using central difference
        h = 1e-5
        deriv_vals = np.gradient(y_vals, x_vals)
        fig, ax = plt.subplots()
        ax.plot(x_vals, deriv_vals)
        ax.set_xlabel('x')
        ax.set_ylabel("f'(x)")
        ax.set_title('Plot of Numerical Derivative')
        st.pyplot(fig)
        st.write("Note: This is a numerical approximation of the derivative.")
    except Exception as e:
        st.error(f"Error: {e}")

# Optimization section (unchanged)
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
