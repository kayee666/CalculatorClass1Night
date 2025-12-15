import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set page config for theme
st.set_page_config(
    page_title="Calculus Explorer",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful calculus theme (updated colors and cat gifs)
st.markdown("""
<style>
    .main {background: #72c9e3 !important; color: white;}
    .sidebar .sidebar-content {background: #dea3ec !important; color: white;}
    .stButton>button {background: linear-gradient(45deg, #ff6b6b, #4ecdc4); color: white; border-radius: 10px; border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.2);}
    .stTextInput>div>div>input {border-radius: 10px; background: rgba(255,255,255,0.8); color: black;}
    .stSelectbox>div>div>select {border-radius: 10px; background: rgba(255,255,255,0.8); color: black;}
    h1, h2, h3 {color: #ffd700; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);}
    .card {background: rgba(255,255,255,0.9); padding: 20px; border-radius: 15px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); margin-bottom: 20px; backdrop-filter: blur(10px);}
    .gif-container {text-align: center; margin: 10px 0;}
    body {background: #72c9e3 !important;}
</style>
""", unsafe_allow_html=True)

# Language selection
lang = st.sidebar.selectbox("Language", ["English", "Indonesia"])

if lang == "English":
    texts = {
        "title": "🧮 Calculus Explorer",
        "subtitle": "Dive into the vibrant world of derivatives, integrals, and optimizations!",
        "function_input": "Enter a function of x (e.g., lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot 2D Function",
        "derivative_button": "Compute and Plot Derivative",
        "3d_button": "Plot 3D Surface (z = f(x,y))",
        "3d_input": "Enter a 3D function of x and y (e.g., lambda x, y: x**2 + y**2):",
        "opt_title": "Optimization Problems",
        "opt_select": "Select a problem:",
        "members_title": "Our Calculus Enthusiasts",
        "members": [
            {"name": "Alice Johnson", "image": "https://via.placeholder.com/100x100?text=Alice", "role": "Derivative Expert"},
            {"name": "Bob Smith", "image": "https://via.placeholder.com/100x100?text=Bob", "role": "Integral Guru"},
            {"name": "Charlie Brown", "image": "https://via.placeholder.com/100x100?text=Charlie", "role": "Optimization Wizard"},
            {"name": "Diana Prince", "image": "https://via.placeholder.com/100x100?text=Diana", "role": "3D Plot Specialist"}
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
        "title": "🧮 Penjelajah Kalkulus",
        "subtitle": "Jelajahi dunia turunan, integral, dan optimasi yang berwarna!",
        "function_input": "Masukkan fungsi dari x (contoh: lambda x: x**2 + 3*x + 1):",
        "plot_button": "Plot Fungsi 2D",
        "derivative_button": "Hitung dan Plot Turunan",
        "3d_button": "Plot Permukaan 3D (z = f(x,y))",
        "3d_input": "Masukkan fungsi 3D dari x dan y (contoh: lambda x, y: x**2 + y**2):",
        "opt_title": "Masalah Optimasi",
        "opt_select": "Pilih masalah:",
        "members_title": "Penggemar Kalkulus Kami",
        "members": [
            {"name": "Alice Johnson", "image": "https://via.placeholder.com/100x100?text=Alice", "role": "Ahli Turunan"},
            {"name": "Bob Smith", "image": "https://via.placeholder.com/100x100?text=Bob", "role": "Guru Integral"},
            {"name": "Charlie Brown", "image": "https://via.placeholder.com/100x100?text=Charlie", "role": "Penyihir Optimasi"},
            {"name": "Diana Prince", "image": "https://via.placeholder.com/100x100?text=Diana", "role": "Spesialis Plot 3D"}
        ],
        "problems": {
            "area": "Maksimalkan luas persegi panjang dengan keliling tetap.",
            "perimeter": "Minimalkan keliling untuk luas tetap.",
            "volume": "Maksimalkan volume kotak dengan luas permukaan tetap.",
            "profit": "Maksimalkan keuntungan untuk produk."
        }
    }

# Sidebar: Our Members section with calculus theme and cat gifs
with st.sidebar.expander(texts["members_title"] + " 🧠"):
    # Add a cat gif at the top
    st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="200" alt="Cute Cat Animation"></div>', unsafe_allow_html=True)
    st.markdown("---")
    for member in texts["members"]:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(member["image"], width=60, caption="📸")
        with col2:
            st.markdown(f"**{member['name']}**<br>*{member['role']}*", unsafe_allow_html=True)
        st.markdown("---")
    # Removed the bottom cat gif as requested

st.title(texts["title"])
st.markdown(f"*{texts['subtitle']}*")

# Function plotting section (2D)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("📈 2D Function Plotting")
func_str = st.text_input(texts["function_input"], "lambda x: x**2")

if st.button(texts["plot_button"]):
    try:
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, y_vals, color='#ffd700', linewidth=3)
        ax.fill_between(x_vals, y_vals, alpha=0.5, color='#ff6b6b')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel('f(x)', fontsize=12, color='white')
        ax.set_title('2D Plot of Function', fontsize=14, color='#ffd700')
        ax.grid(True, alpha=0.5, color='white')
        ax.set_facecolor('rgba(0,0,0,0.1)')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")
st.markdown('</div>', unsafe_allow_html=True)

# Derivative section (2D)
st.markdown('<div class="card">', unsafe_allow_html=True)
if st.button(texts["derivative_button"]):
    try:
        func = eval(func_str)
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        deriv_vals = np.gradient(y_vals, x_vals)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, deriv_vals, color='#4ecdc4', linewidth=3)
        ax.fill_between(x_vals, deriv_vals, alpha=0.5, color='#45b7d1')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel("f'(x)", fontsize=12, color='white')
        ax.set_title('2D Plot of Numerical Derivative', fontsize=14, color='#4ecdc4')
        ax.grid(True, alpha=0.5, color='white')
        ax.set_facecolor('rgba(0,0,0,0.1)')
        st.pyplot(fig)
        st.info("Note: This is a numerical approximation of the derivative using calculus principles.")
    except Exception as e:
        st.error(f"Error: {e}")
st.markdown('</div>', unsafe_allow_html=True)

# 3D Plotting section (using matplotlib)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🌐 3D Surface Plotting")
func_3d_str = st.text_input(texts["3d_input"], "lambda x, y: x**2 + y**2")

if st.button(texts["3d_button"]):
    try:
        func_3d = eval(func_3d_str)
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        Z = func_3d(X, Y)
        
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8, edgecolor='none')
        ax.set_xlabel('x', fontsize=12, color='white')
        ax.set_ylabel('y', fontsize=12, color='white')
        ax.set_zlabel('z', fontsize=12, color='white')
        ax.set_title('3D Surface Plot', fontsize=14, color='#ffd700')
        ax.set_facecolor('rgba(0,0,0,0.1)')
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        st.pyplot(fig)
        st.info("Explore partial derivatives and integrals in 3D space!")
        # Add a cat gif below the plot
        st.markdown('<div class="gif-container"><img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="300" alt="Cute Cat Animation"></div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")
st.markdown('</div>', unsafe_allow_html=True)

# Optimization section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("⚖️ " + texts["opt_title"])
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
    st.success(f"Optimal x: {x_opt}, y: {y_opt}, Max Area: {A_max}")

elif problem == "perimeter":
    if lang == "English":
        st.write("Minimize perimeter P = 2x + 2y, subject to area x*y = A. Enter A:")
    else:
        st.write("Minimalkan keliling P = 2x + 2y, dengan luas x*y = A. Masukkan A:")
    A = st.number_input("A", value=100.0)
    x_opt = np.sqrt(A)
    y_opt = A / x_opt
    P_min = 2 * x_opt + 2 * y_opt
    st.success(f"Optimal x: {x_opt}, y: {y_opt}, Min Perimeter: {P_min}")

elif problem == "volume":
    if lang == "English":
        st.write("Maximize volume V = x*y*z, subject to surface area 2xy + 2xz + 2yz = S. Enter S:")
    else:
        st.write("Maksimalkan volume V = x*y*z, dengan luas permukaan 2xy + 2xz + 2yz = S. Masukkan S:")
    S = st.number_input("S", value=24.0)
    x_opt = np.sqrt(S / 6)
    V_max = x_opt ** 3
    st.success(f"Optimal x=y=z: {x_opt}, Max Volume: {V_max}")

elif problem == "profit":
    if lang == "English":
        st.write("Maximize profit P = 100x - 0.1x^2 - 50, where x is quantity.")
    else:
        st.write("Maksimalkan keuntungan P = 100x - 0.1x^2 - 50, di mana x adalah jumlah.")
    x_opt = 500
    P_max = 100 * 500 - 0.1 * 500 ** 2 - 50
    st.success(f"Optimal x: {x_opt}, Max Profit: {P_max}")
