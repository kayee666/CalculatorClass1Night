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
        "sidebar_gif": "Cat GIF",
        "unsupported": "Unsupported problem type. Supported: area/perimeter, volume/surface, profit.",
        "team_title": "### Meet Our Team",
        "team_desc": "The amazing team behind this app!",
        "member1_name": "Alice Johnson",
        "member1_desc": "Math Enthusiast & Developer",
        "member2_name": "Bob Smith",
        "member2_desc": "Data Scientist",
        "member3_name": "Charlie Brown",
        "member3_desc": "UI/UX Designer",
        "member4_name": "Diana Prince",
        "member4_desc": "Project Manager",
        "calculus_group": "Calculus Group 2"
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
        "sidebar_gif": "GIF Kucing",
        "unsupported": "Tipe masalah tidak didukung. Didukung: luas/keliling, volume/permukaan, keuntungan.",
        "team_title": "### Temui Tim Kami",
        "team_desc": "Tim hebat di balik aplikasi ini!",
        "member1_name": "Alice Johnson",
        "member1_desc": "Penggemar Matematika & Pengembang",
        "member2_name": "Bob Smith",
        "member2_desc": "Ilmuwan Data",
        "member3_name": "Charlie Brown",
        "member3_desc": "Desainer UI/UX",
        "member4_name": "Diana Prince",
        "member4_desc": "Manajer Proyek",
        "calculus_group": "Kelompok Kalkulus 2"
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
# Calculus Group 2 Section in Sidebar
# =======================
st.sidebar.markdown("---")  # Separator
st.sidebar.subheader(t["calculus_group"])

# Placeholder photos for members
member_photos = [
    "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=100&h=100&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop&crop=face"
]

for i in range(4):
    st.sidebar.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="{member_photos[i]}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 2px solid #FFD580;" alt="Member {i+1}">
        <p style="margin: 5px 0; font-size: 14px; font-weight: bold;">{t[f'member{i+1}_name']}</p>
        <p style="margin: 0; font-size: 12px; color: #666;">{t[f'member{i+1}_desc']}</p>
    </div>
    """, unsafe_allow_html=True)

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
.team-card {
    background: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    transition: transform 0.3s ease;
    margin-bottom: 20px;
}
.team-card:hover {
    transform: scale(1.05);
}
.team-img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='big-title'>{t['title']}</div>", unsafe_allow_html=True)

# =======================
# Tabs for Function Visualizer, Optimization, and Team
# =======================
tab1, tab2, tab3 = st.tabs(["Function Visualizer", "Optimization Solver", "Team Members"])

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
            # Improved parsing for supported cases (English and Indonesian)
            problem_lower = problem_text.lower()
            x = sp.symbols('x')
            
            # Keywords for area
            area_keywords = ["area", "luas"]
            rectangle_keywords = ["rectangle", "persegi panjang"]
            perimeter_keywords = ["perimeter", "keliling"]
            
            # Keywords for volume
            volume_keywords = ["volume", "volume"]
            box_keywords = ["box", "kotak"]
            surface_keywords = ["surface", "permukaan"]
            
            # Keywords for profit
            profit_keywords = ["profit", "keuntungan"]
            
            # Check for area/perimeter
            if any(k in problem_lower for k in area_keywords) and any(k in problem_lower for k in rectangle_keywords) and any(k in problem_lower for k in perimeter_keywords):
                # Extract P (perimeter) from text (e.g., "keliling 20", "perimeter 20")
                match = re.search(r'(?:keliling|perimeter)\s+(\d+)', problem_lower)
                if match:
                    P = int(match.group(1))
                    func = x * (P/2 - x)  # Area = x * (P/2 - x)
                    goal = "maximize"
                else:
                    st.error("Could not extract perimeter value. Use format like 'keliling 20' or 'perimeter 20'.")
                    func = None
            
            # Check for volume/surface
            elif any(k in problem_lower for k in volume_keywords) and any(k in problem_lower for k in box_keywords) and any(k in problem_lower for k in surface_keywords):
                # Extract S (surface area)
                match = re.search(r'(?:permukaan|surface)\s+area\s+(\d+)', problem_lower)
                if match:
                    S = int(match.group(1))
                    # Volume V = x^2 * h, with 2x^2 + 4x h = S -> h = (S - 2x^2)/(4x)
                    func = x**2 * (S - 2*x**2)/(4*x)
                    goal = "maximize"
                else:
                    st.error("Could not extract surface area value. Use format like 'permukaan area 20' or 'surface area 20'.")
                    func = None
            
            # Check for profit
            elif any(k in problem_lower for k in profit_keywords):
                # Extract P (price) and C (cost) if possible
                match_p = re.search(r'(?:price|harga)\s+(\d+)', problem_lower)
                match_c = re.search(r'(?:cost|biaya)\s+(\d+)', problem_lower)
                P = int(match_p.group(1)) if match_p else 10
                C = int(match_c.group(1)) if match_c else 1
                func = P*x - C*x**2
                goal = "maximize"
            
            else:
                st.error(t["unsupported"])
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

with tab3:
    # =======================
    # Team Members Display
    # =======================
    st.markdown(t["team_title"])
    st.markdown(t["team_desc"])
    
    # Placeholder photos (using Unsplash for random avatars)
    member_photos = [
        "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face"
    ]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="team-card">
            <img src="{member_photos[0]}" class="team-img" alt="Member 1">
            <h4>{t['member1_name']}</h4>
            <p>{t['member1_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="team-card">
            <img src="{member_photos[1]}" class="team-img" alt="Member 2">
            <h4>{t['member2_name']}</h4>
            <p>{t['member2_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f
        <div class="team-card">

