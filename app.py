import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="Drehgeschwindigkeit Visualisierung", layout="centered")

st.title("🌀 Drehgeschwindigkeit Visualisierung")

# Eingaben
durchmesser = st.number_input("Kreisdurchmesser (cm):", min_value=0.1, value=10.0, step=0.1)
u_min = st.number_input("Drehzahl (U/min):", min_value=0.0, value=60.0, step=1.0)

# Berechnungen
umfang = np.pi * durchmesser
u_sek = u_min / 60  # Umdrehungen pro Sekunde
winkelgeschwindigkeit = u_sek * 2 * np.pi  # rad/s

st.write(f"**Umfang:** {umfang:.2f} cm")
st.write(f"**Winkelgeschwindigkeit:** {winkelgeschwindigkeit:.2f} rad/s")

# Animation starten
start = st.button("▶️ Start Animation")

if start:
    fig, ax = plt.subplots()
    ax.set_xlim(-durchmesser, durchmesser)
    ax.set_ylim(-durchmesser, durchmesser)
    ax.set_aspect("equal")
    circle = plt.Circle((0, 0), durchmesser / 2, fill=False, color="blue", linewidth=2)
    point, = ax.plot([], [], "ro", markersize=10)
    ax.add_artist(circle)

    plot = st.pyplot(fig)
    t0 = time.time()

    while True:
        t = time.time() - t0
        theta = (winkelgeschwindigkeit * t) % (2 * np.pi)
        x = (durchmesser / 2) * np.cos(theta)
        y = (durchmesser / 2) * np.sin(theta)
        point.set_data([x], [y])
        plot.pyplot(fig)
        time.sleep(0.02)
