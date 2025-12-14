import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import re

st.set_page_config(
    page_title="Function & Derivative Visualizer",
    layout="wide",
    page_icon="📈"
)

# =======================
# Language Selection
# =======================
language = st.sidebar.selectbox("Language / Bahasa", ["English", "Indonesia"])

# Translation dictionary
translations = {
    "English": {
        "settings": "Settings",
        "function_input": "Enter function f(x):",
        "range_min": "Range Minimum (x)",
        "range_max": "Range Maximum (x)",
        "num_points": "Number of points",
        "plot_mode": "Plot Mode:",
        "title": "📈 Function & Derivative Visualizer",
        "derivative_title": "### Step-by-step derivative f'(x)",
        "graph_fx": "Graph f(x)",
        "graph_dfx": "Graph f'(x)",
        "3d_title": "3D Interactive Curve f(x) & f'(x)",
        "error": "Error processing the function.",
        "optimization_title": "### Story-Based Optimization Solver",
        "optimization_desc": "Enter a story problem (e.g., 'Maximize the area of a rectangle with perimeter 20'). Supported: area, perimeter, volume, profit.",
        "solve_button": "Solve Optimization",
        "solution_title": "#### Solution",
        "critical_points": "Critical Points:",
        "optimal_value": "Optimal Value:",
        "visualization": "Visualization",
        "example": "Example: Maximize the area of a rectangle with perimeter P=20. (Use x for width, P for perimeter)",
        "sidebar_gif": "Cat GIF"
    },
    "Indonesia": {
        "settings": "Pengaturan",
        "function_input": "Masukkan fungsi f(x):",
        "range_min": "Rentang Minimum (x)",
        "range_max": "Rentang Maksimum (x)",
        "num_points": "Jumlah titik",
        "plot_mode": "Mode Plot:",
        "title": "📈 Visualizer Fungsi & Turunan",
        "derivative_title": "### Turunan langkah demi langkah f'(x)",
        "graph_fx": "Grafik f(x)",
        "graph_dfx": "Grafik f'(x)",
        "3d_title": "Kurva Interaktif 3D f(x) & f'(x)",
        "error": "Kesalahan memproses fungsi.",
        "optimization_title": "### Penyelesai Optimasi Berbasis Cerita",
        "optimization_desc": "Masukkan masalah cerita (contoh: 'Maksimalkan luas persegi panjang dengan keliling 20'). Didukung: luas, keliling, volume, keuntungan.",
        "solve_button": "Selesaikan Optimasi",
        "solution_title": "#### Solusi",
        "critical_points": "Titik Kritis:",
        "optimal_value": "Nilai Optimal:",
        "visualization": "Visualisasi",
        "example": "Contoh: Maksimalkan luas persegi panjang dengan keliling P=20. (Gunakan x untuk lebar, P untuk keliling)",
        "sidebar_gif": "GIF Kucing"
    }
}

t = translations[language]

# =======================
# Sidebar
# =======================
st.sidebar.header(t["settings"])
function_text = st.sidebar.text_input(t["function_input"], value="x**3 - 3*x")
range_min = st.sidebar.number_input(t["range_min"], value=-5)
range_max = st.sidebar.number_input(t["range_max"], value=5)
num_points = st.sidebar.slider(t["num_points"], 200, 2000, 500)
plot_mode = st.sidebar.radio(t["plot_mode"], ["2D", "3D"])

# GIF kucing di bawah sidebar
st.sidebar.markdown(
    f"""
    <div style="margin-top: 50px; text-align:center;">
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" 
        style="width:150px; border-radius:12px; box-shadow:0 0 12px rgba(255,255,255,0.6);" 
        alt="{t['sidebar_gif']}">
    </div>
    """, unsafe_allow_html=True
)

# =======================
# Main background + title
# =======================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #5F9EA0;
    color: #FFFFFF;
}
.sub-box {
    background: rgba(219,112,147,0.8);
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(219,112,147,0.9);
}
.big-title {
    font-size: 36px !important;
    font-weight: 700;
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='big-title'>{t['title']}</div>", unsafe_allow_html=True)

# =======================
# Tabs for Function Visualizer and Optimization
# =======================
tab1, tab2 = st.tabs(["Function Visualizer", "Optimization Solver"])

with tab1:
    # =======================
    # Symbolic Math
    # =======================
    x = sp.symbols("x")
    try:
        func = sp.sympify(function_text)
        derivative = sp.diff(func, x)
        second_derivative = sp.diff(derivative, x)

        st.markdown(t["derivative_title"])
        st.latex(sp.latex(derivative))

        f_num = sp.lambdify(x, func, "numpy")
        df_num = sp.lambdify(x, derivative, "numpy")

        x_vals = np.linspace(range_min, range_max, num_points)
        y_vals = f_num(x_vals)
        dy_vals = df_num(x_vals)

        # --------------------------
        # 2D plotting
        # --------------------------
        if plot_mode == "2D":
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
                st.subheader(t["graph_fx"])
                fig1, ax1 = plt.subplots()
                ax1.plot(x_vals, y_vals, color="#FFD580", linewidth=3, alpha=0.8)
                ax1.grid(True, linestyle="--", alpha=0.5)
                st.pyplot(fig1)
                st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
                st.subheader(t["graph_dfx"])
                fig2, ax2 = plt.subplots()
                ax2.plot(x_vals, dy_vals, color="#FF9AA2", linewidth=3, alpha=0.8)
                ax2.grid(True, linestyle="--", alpha=0.5)
                st.pyplot(fig2)
                st.markdown("</div>", unsafe_allow_html=True)

        # --------------------------
        # 3D plotting
        # --------------------------
        else:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader(t["3d_title"])
            z_vals = np.zeros_like(x_vals)
            z_vals2 = np.ones_like(x_vals)

            fig3d = go.Figure()
            fig3d.add_trace(go.Scatter3d(x=x_vals, y=y_vals, z=z_vals, mode='lines',
                                         line=dict(color='lightblue', width=5), name='f(x)'))
            fig3d.add_trace(go.Scatter3d(x=x_vals, y=dy_vals, z=z_vals2, mode='lines',
                                         line=dict(color='pink', width=5), name="f'(x)"))
            fig3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='Curve ID',
                                           bgcolor='rgba(0,0,0,0)'),
                                margin=dict(l=0, r=0, b=0, t=0), height=600)
            st.plotly_chart(fig3d, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(t["error"])
        st.error(str(e))

with tab2:
    # =======================
    # Optimization Solver
    # =======================
    st.markdown(t["optimization_title"])
    st.markdown(t["optimization_desc"])
    st.markdown(f"*{t['example']}*")
    
    problem_text = st.text_area("Problem Input", value="", height=100)
    
    if st.button(t["solve_button"]):
        try:
            # Simple parsing for supported cases
            # Supported patterns:
            # - Maximize area of rectangle with perimeter P
            # - Maximize volume of box with surface area S
            # - Maximize profit with cost C and price P (linear)
            
            problem_lower = problem_text.lower()
            x = sp.symbols('x')
            
            if "area" in problem_lower and "rectangle" in problem_lower and "perimeter" in problem_lower:
                # Extract P from text (assume format like "perimeter 20")
                match = re.search(r'perimeter\s+(\d+)', problem_lower)
                if match:
                    P = int(match.group(1))
                    func = x * (P/2 - x)  # Area = x * (P/2 - x)
                    goal = "maximize"
                else:
                    st.error("Could not extract perimeter value.")
                    func = None
            
            elif "volume" in problem_lower and "box" in problem_lower and "surface" in problem_lower:
                # Extract S from text
                match = re.search(r'surface\s+area\s+(\d+)', problem_lower)
                if match:
                    S = int(match.group(1))
                    # Volume V = x*y*z, with 2(xy + xz + yz) = S
                    # Assume square base for simplicity: V = x^2 * h, 2x^2 + 4x h = S -> h = (S - 2x^2)/(4x)
                    func = x**2 * (S - 2*x**2)/(4*x)
                    goal = "maximize"
                else:
                    st.error("Could not extract surface area value.")
                    func = None
            
            elif "profit" in problem_lower:
                # Assume linear profit: Profit = P*x - C*x^2 (simplified)
                # Extract P and C if possible, else default
                match_p = re.search(r'price\s+(\d+)', problem_lower)
                match_c = re.search(r'cost\s+(\d+)', problem_lower)
                P = int(match_p.group(1)) if match_p else 10
                C = int(match_c.group(1)) if match_c else 1
                func = P*x - C*x**2
                goal = "maximize"
            
            else:
                st.error("Unsupported problem type. Supported: area/perimeter, volume/surface, profit.")
                func = None
            
            if func:
                derivative = sp.diff(func, x)
                critical_points = sp.solve(derivative, x)
                critical_points = [cp for cp in critical_points if cp.is_real and cp > 0]  # Filter positive real
                
                st.markdown(t["solution_title"])
                st.write(f"Objective Function: {func}")
                st.write(f"Derivative: {derivative}")
                st.write(f"{t['critical_points']} {critical_points}")
                
                if critical_points:
                    optimal_x = critical_points[0]  # Assume first for simplicity
                    optimal_value = func.subs(x, optimal_x)
                    st.write(f"{t['optimal_value']} {optimal_value} at x = {optimal_x}")
                    
                    # Visualization
                    st.markdown(f"### {t['visualization']}")
                    x_vals_opt = np.linspace(0.1, float(optimal_x)*2, 100)
                    y_vals_opt = [float(func.subs(x, val)) for val in x_vals_opt]
                    
                    fig_opt, ax_opt = plt.subplots()
                    ax_opt.plot(x_vals_opt, y_vals_opt, color="#FFD580", linewidth=3)
                    ax_opt.scatter([float(optimal_x)], [float(optimal_value)], color='red', s=100, label='Optimal')
                    ax_opt.grid(True, linestyle="--", alpha=0.5)
                    ax_opt.legend()
                    st.pyplot(fig_opt)
                else:
                    st.write("No valid critical points found.")
        
        except Exception as e:
            st.error("Error solving the problem.")
            st.error(str(e))
