
# hawking_fusion.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from glossary import render_glossary
from hawking_engine import (
    compute_schwarzschild_radius,
    compute_hawking_temperature,
    compute_mass_decay,
    estimate_radiation_power
)

# ----------------------------
# Symbolic Functions
# ----------------------------

def compute_coherence(theta, entropy):
    return 1 / (1 + theta * entropy)

def compute_radiation(theta, entropy, gamma):
    return theta * entropy * (1 - gamma)

def compute_karmic_load(theta, entropy, gamma):
    return theta * entropy * (1 - gamma)

def simulate_symbolic_dynamics(theta, entropy, steps=20):
    times = np.arange(steps)
    gammas, rhos, karmic = [], [], []

    for t in times:
        entropy_t = entropy + 0.05 * t
        gamma = compute_coherence(theta, entropy_t)
        rho = compute_radiation(theta, entropy_t, gamma)
        k = compute_karmic_load(theta, entropy_t, gamma)

        gammas.append(gamma)
        rhos.append(rho)
        karmic.append(k)

    return times, gammas, rhos, karmic

# ----------------------------
# Streamlit UI
# ----------------------------

st.set_page_config(page_title="Hawking Fusion Simulator", layout="wide")
st.title("Hawking Radiation: Symbolic + Physical Fusion")
st.markdown("Model real and symbolic radiation from identity collapse or black hole evaporation.")

# Sidebar controls
with st.sidebar:
    st.header("Symbolic Parameters")
    theta = st.slider("Θ — Clinging", 0.0, 2.0, 1.0, 0.01)
    entropy = st.slider("∇S — Entropy Gradient", 0.1, 5.0, 1.0, 0.1)
    st.header("Physical Parameters")
    mass_kg = st.number_input("Black Hole Mass (kg)", value=1.98847e30, format="%.2e")
    time_elapsed = st.number_input("Time Elapsed (s)", value=1e12, format="%.2e")

    if st.checkbox("Show Glossary"):
        render_glossary()

# Run simulations
t, gammas, rhos, karmic = simulate_symbolic_dynamics(theta, entropy)
radius = compute_schwarzschild_radius(mass_kg)
temperature = compute_hawking_temperature(mass_kg)
power = estimate_radiation_power(mass_kg)
remaining_mass = compute_mass_decay(mass_kg, time_elapsed)

# Layout
st.subheader("Symbolic Identity Dynamics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Final Coherence γ", f"{gammas[-1]:.3f}")
    st.metric("Final Radiation ρ", f"{rhos[-1]:.3f}")
with col2:
    st.metric("Karmic Load K", f"{karmic[-1]:.3f}")
    if rhos[-1] > 2.5:
        st.error("Symbolic Attractor Collapsing")
    elif rhos[-1] > 1.0:
        st.warning("Symbolic Leakage Increasing")
    else:
        st.success("System Coherent")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, gammas, label="γ(t) — Coherence")
ax.plot(t, rhos, label="ρ(t) — Radiation", linestyle='--')
ax.plot(t, karmic, label="K(t) — Karmic Load", linestyle=':')
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Symbolic Collapse Over Time")
ax.legend()
st.pyplot(fig)

# Physical model
st.subheader("Physical Hawking Parameters")
col3, col4 = st.columns(2)
with col3:
    st.metric("Schwarzschild Radius", f"{radius:.2e} m")
    st.metric("Hawking Temperature", f"{temperature:.2e} K")
with col4:
    st.metric("Radiation Power", f"{power:.2e} W")
    st.metric("Remaining Mass", f"{remaining_mass:.2e} kg")

st.markdown("---")
st.caption("Fusion engine combining symbolic identity dynamics and Hawking radiation thermodynamics.")
