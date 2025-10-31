import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🌀 Drehgeschwindigkeit Visualisierung (flüssig)")

# Eingaben
durchmesser = st.number_input("Kreisdurchmesser (cm):", min_value=0.1, value=10.0, step=0.1)
u_min = st.number_input("Drehzahl (U/min):", min_value=0.0, value=60.0, step=1.0)

u_sek = u_min / 60
winkelgeschwindigkeit = u_sek * 2 * np.pi  # rad/s

st.write(f"**Winkelgeschwindigkeit:** {winkelgeschwindigkeit:.2f} rad/s")

# Kreis vorbereiten
theta_circle = np.linspace(0, 2*np.pi, 100)
x_circle = (durchmesser/2) * np.cos(theta_circle)
y_circle = (durchmesser/2) * np.sin(theta_circle)

# Frames vorbereiten
frames = []
num_frames = 100
t_values = np.linspace(0, 2*np.pi/winkelgeschwindigkeit, num_frames)

for t in t_values:
    x_point = (durchmesser/2) * np.cos(winkelgeschwindigkeit * t)
    y_point = (durchmesser/2) * np.sin(winkelgeschwindigkeit * t)
    frames.append(go.Frame(data=[go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='blue')),
                                go.Scatter(x=[x_point], y=[y_point], mode='markers', marker=dict(size=12, color='red'))]))

fig = go.Figure(
    data=[go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='blue')),
          go.Scatter(x=[durchmesser/2], y=[0], mode='markers', marker=dict(size=12, color='red'))],
    frames=frames
)

fig.update_layout(
    width=400, height=400,
    xaxis=dict(scaleanchor="y", range=[-durchmesser, durchmesser]),
    yaxis=dict(range=[-durchmesser, durchmesser]),
    updatemenus=[dict(type="buttons",
                      buttons=[dict(label="Play",
                                    method="animate",
                                    args=[None, {"frame": {"duration": 50, "redraw": True},
                                                 "fromcurrent": True, "transition": {"duration": 0}}])])]
)

st.plotly_chart(fig, use_container_width=True)

