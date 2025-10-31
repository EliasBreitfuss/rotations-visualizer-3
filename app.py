import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.title("🌀 Drehgeschwindigkeit Visualisierung")

# Eingaben
durchmesser = st.number_input("Kreisdurchmesser (cm):", min_value=0.1, value=10.0, step=0.1)
u_min = st.number_input("Drehzahl (U/min):", min_value=0.0, value=60.0, step=1.0)

# Berechnungen
u_sek = u_min / 60  # Umdrehungen pro Sekunde
winkelgeschwindigkeit = u_sek * 2 * np.pi  # rad/s

st.write(f"**Winkelgeschwindigkeit:** {winkelgeschwindigkeit:.2f} rad/s")

# Platz für Animation
plot_area = st.empty()
start = st.button("▶️ Start Animation")

if start:
    t0 = time.time()
    for _ in range(200):  # Anzahl der Frames
        t = time.time() - t0
        theta = (winkelgeschwindigkeit * t) % (2 * np.pi)
        
        # Kreis zeichnen
        fig, ax = plt.subplots()
        ax.set_xlim(-durchmesser, durchmesser)
        ax.set_ylim(-durchmesser, durchmesser)
        ax.set_aspect("equal")
        
        circle = plt.Circle((0, 0), durchmesser / 2, fill=False, color="blue", linewidth=2)
        ax.add_artist(circle)
        
        # roter Punkt auf Kreis
        x = (durchmesser / 2) * np.cos(theta)
        y = (durchmesser / 2) * np.sin(theta)
        ax.plot(x, y, "ro", markersize=10)
        
        # Plot anzeigen
        plot_area.pyplot(fig)
        plt.close(fig)
        time.sleep(0.05)

