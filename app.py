import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.title("🌀 Drehgeschwindigkeit Visualisierung (flüssig)")

# Eingaben
durchmesser = st.number_input("Kreisdurchmesser (cm):", min_value=0.1, value=10.0, step=0.1)
u_min = st.number_input("Drehzahl (U/min):", min_value=0.0, value=60.0, step=1.0)

u_sek = u_min / 60
winkelgeschwindigkeit = u_sek * 2 * np.pi  # rad/s

st.write(f"**Winkelgeschwindigkeit:** {winkelgeschwindigkeit:.2f} rad/s")

# Kreis vorbereiten
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = (durchmesser / 2) * np.cos(theta)
y_circle = (durchmesser / 2) * np.sin(theta)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='blue')))

# roter Punkt für Rotation
point = go.Scatter(x=[durchmesser/2], y=[0], mode='markers', marker=dict(size=12, color='red'))
fig.add_trace(point)

fig.update_layout(width=400, height=400, xaxis=dict(scaleanchor="y", range=[-durchmesser, durchmesser]),
                  yaxis=dict(range=[-durchmesser, durchmesser]))

plot_area = st.empty()
start = st.button("▶️ Start Animation")

if start:
    t0 = time.time()
    while True:
        t = time.time() - t0
        x = (durchmesser / 2) * np.cos(winkelgeschwindigkeit * t)
        y = (durchmesser / 2) * np.sin(winkelgeschwindigkeit * t)
        fig.data[1].x = [x]
        fig.data[1].y = [y]
        plot_area.plotly_chart(fig, use_container_width=True)
        time.sleep(0.02)  # ~50 FPS

