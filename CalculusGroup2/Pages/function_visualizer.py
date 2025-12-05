import streamlit as st
from pythreejs import *
import numpy as np
import time

st.set_page_config(page_title="3D Calculus Symbols", layout="centered")

st.title("🔮 3D Calculus Symbols (Animated pythreejs version)")

# Membuat simbol kalkulus
symbols = ["∫", "∂", "π", "∞", "Σ", "√"]
meshes = []

for i, s in enumerate(symbols):
    text_geom = TextGeometry(
        text=s,
        size=2,
        height=0.4,
        curveSegments=12,
        font="helvetiker",
        bevelEnabled=False
    )
    material = MeshPhongMaterial(color="#9370db", shininess=120, specular="#ffffff")
    mesh = Mesh(geometry=text_geom, material=material)
    mesh.position = [np.sin(i) * 5, np.cos(i) * 3, i - 3]
    meshes.append(mesh)

# Scene dan pencahayaan
scene = Scene(children=[
    *meshes,
    AmbientLight(intensity=0.6),
    PointLight(position=[10, 10, 10], intensity=1.2)
])

# Kamera dan kontrol
camera = PerspectiveCamera(position=[0, 0, 15], fov=60)
controller = OrbitControls(controlling=camera)

renderer = Renderer(
    camera=camera,
    scene=scene,
    controls=[controller],
    width=800,
    height=500,
    background="#e0ffff"
)

# Tampilkan renderer di Streamlit
st.write(renderer)

# Animasi rotasi otomatis
st.write("⏳ Animasi rotasi otomatis aktif...")
for _ in range(200):  # durasi animasi
    for mesh in meshes:
        mesh.rotation = [
            mesh.rotation[0] + 0.02,
            mesh.rotation[1] + 0.04,
            mesh.rotation[2]
        ]
    time.sleep(0.05)
    renderer.render(scene, camera)
