import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go

st.set_page_config(
    page_title="Function & Derivative Visualizer",
    layout="wide",
    page_icon="📈"
)

# =======================
# Sidebar
# =======================
st.sidebar.header("Settings")
function_text = st.sidebar.text_input("Enter function f(x):", value="x**3 - 3*x")
range_min = st.sidebar.number_input("Range Minimum (x)", value=-5)
range_max = st.sidebar.number_input("Range Maximum (x)", value=5)
num_points = st.sidebar.slider("Number of points", 200, 2000, 500)
plot_mode = st.sidebar.radio("Plot Mode:", ["2D", "3D"])

# GIF kucing di sidebar
st.sidebar.markdown(
    """
    <div style="margin-top: 50px; text-align:center;">
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" 
        style="width:150px; border-radius:12px; box-shadow:0 0 12px rgba(255,255,255,0.6);" 
        alt="Cat GIF">
    </div>
    """, unsafe_allow_html=True
)

# =======================
# Background + Title
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

# ================
# 3D Background Animasi Calculus Symbols (floating)
# ================
st.markdown("""
<canvas id="calcCanvas"></canvas>
<style>
#calcCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
    filter: blur(1px) brightness(1.12);
}
</style>
<script>
const canvas = document.getElementById('calcCanvas');
const ctx = canvas.getContext('2d');
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.onresize = resizeCanvas;
const symbols = ["∫", "∂", "∇", "Σ", "∞", "√", "π", "dx", "dy", "lim", "f’", "∂x", "∂y"];
let particles = [];
for (let i = 0; i < 40; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        z: Math.random() * 3 + 0.5,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
        symbol: symbols[Math.floor(Math.random() * symbols.length)],
        size: Math.random() * 25 + 18
    });
}
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        ctx.font = (p.size * p.z) + "px serif";
        ctx.fillStyle = "rgba(255,255,255,0.35)";
        ctx.fillText(p.symbol, p.x, p.y);
        p.x += p.vx * p.z;
        p.y += p.vy * p.z;
        if (p.x < -50) p.x = canvas.width + 50;
        if (p.y < -50) p.y = canvas.height + 50;
        if (p.x > canvas.width + 50) p.x = -50;
        if (p.y > canvas.height + 50) p.y = -50;
    });
    requestAnimationFrame(animate);
}
animate();
</script>
""", unsafe_allow_html=True)

# =======================
# Title
# =======================
st.markdown("<div class='big-title'>📈 Function & Derivative Visualizer</div>", unsafe_allow_html=True)

# =======================
# Animasi 3D Kalkulus di Main Display (warna latar #e0ffff)
# =======================
st.markdown("""
<div id="calc3d"></div>

<style>
#calc3d {
    width: 100%;
    height: 400px;
    margin: 0 auto 40px auto;
    border-radius: 12px;
    background: #e0ffff; /* Warna latar diganti */
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
}
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const container = document.getElementById('calc3d');
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 400, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({antialias: true, alpha: true});
renderer.setSize(container.clientWidth, 400);
container.appendChild(renderer.domElement);

// Cahaya
const light = new THREE.PointLight(0xffffff, 1);
light.position.set(10, 10, 10);
scene.add(light);

// Objek simbol kalkulus 3D
const loader = new THREE.FontLoader();
loader.load('https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function(font) {
    const symbols = ["∫", "∂", "π", "∞", "Σ", "√"];
    const group = new THREE.Group();
    symbols.forEach((s, i) => {
        const geometry = new THREE.TextGeometry(s, {
            font: font,
            size: 2,
            height: 0.3,
            curveSegments: 12,
        });
        const material = new THREE.MeshPhongMaterial({color: 0x4682b4, shininess: 100});
        const mesh = new THREE.Mesh(geometry, material);
        mesh.position.set(Math.sin(i)*5, Math.cos(i)*3, i-3);
        group.add(mesh);
    });
    scene.add(group);
    camera.position.z = 12;
    function animate() {
        requestAnimationFrame(animate);
        group.rotation.x += 0.005;
        group.rotation.y += 0.01;
        renderer.render(scene, camera);
    }
    animate();
});
</script>
""", unsafe_allow_html=True)

# =======================
# Symbolic Math
# =======================
x = sp.symbols("x")
try:
    func = sp.sympify(function_text)
    derivative = sp.diff(func, x)
    second_derivative = sp.diff(derivative, x)

    st.markdown("### Step-by-step derivative f'(x)")
    st.latex(sp.latex(derivative))

    f_num = sp.lambdify(x, func, "numpy")
    df_num = sp.lambdify(x, derivative, "numpy")

    x_vals = np.linspace(range_min, range_max, num_points)
    y_vals = f_num(x_vals)
    dy_vals = df_num(x_vals)

    if plot_mode == "2D":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f(x)")
            fig1, ax1 = plt.subplots()
            ax1.plot(x_vals, y_vals, color="#FFD580", linewidth=3, alpha=0.8)
            ax1.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig1)
            st.markdown("</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
            st.subheader("Graph f'(x)")
            fig2, ax2 = plt.subplots()
            ax2.plot(x_vals, dy_vals, color="#FF9AA2", linewidth=3, alpha=0.8)
            ax2.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='sub-box'>", unsafe_allow_html=True)
        st.subheader("3D Interactive Curve f(x) & f'(x)")
        z_vals = np.zeros_like(x_vals)
        z_vals2 = np.ones_like(x_vals)
        fig3d = go.Figure()
        fig3d.add_trace(go.Scatter3d(x=x_vals, y=y_vals, z=z_vals, mode='lines',
                                     line=dict(color='lightblue', width=5), name='f(x)'))
        fig3d.add_trace(go.Scatter3d(x=x_vals, y=dy_vals, z=z_vals2, mode='lines',
                                     line=dict(color='pink', width=5), name="f'(x)"))
        fig3d.update_layout(
            scene=dict(
                xaxis_title='x',
                yaxis_title='y',
                zaxis_title='Curve ID',
                bgcolor='rgba(0,0,0,0)'
            ),
            margin=dict(l=0, r=0, b=0, t=0), height=600
        )
        st.plotly_chart(fig3d, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
except Exception as e:
    st.error("Error processing the function.")
    st.error(str(e))
