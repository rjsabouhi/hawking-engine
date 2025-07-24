# hawking_simulator.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from glossary import render_glossary

# ----------------------------
# Core Symbolic Radiation Logic
# ----------------------------

def compute_coherence(theta, entropy):
    return 1 / (1 + theta * entropy)

def compute_radiation(theta, entropy, gamma):
    return theta * entropy * (1 - gamma)

def compute_karmic_load(theta, entropy, gamma):
    return theta * entropy * (1 - gamma)

def simulate_radiation(theta, entropy, steps=20):
    times = np.arange(steps)
    gammas = []
    rhos = []
    karmic = []

    for t in times:
        # Simulate entropy increase over time
        entropy_t = entropy + 0.05 * t
        gamma = compute_coherence(theta, entropy_t)
        rho = compute_radiation(theta, entropy_t, gamma)
        k = compute_karmic_load(theta, entropy_t, gamma)

        gammas.append(gamma)
        rhos.append(rho)
        karmic.append(k)

    return times, gammas, rhos, karmic

# ----------------------------
# Streamlit App Interface
# ----------------------------

st.set_page_config(page_title="Symbolic Hawking Radiation Simulator", layout="wide")
st.title("Symbolic Hawking Radiation Simulator")
st.markdown("Simulate symbolic radiation and attractor collapse using clinging (Θ), entropy gradient (∇S), and coherence.")

# Sidebar sliders
with st.sidebar:
    theta = st.slider("Θ — Clinging", 0.0, 2.0, 1.0, 0.01)
    entropy = st.slider("∇S — Entropy Gradient", 0.1, 5.0, 1.0, 0.1)
    show_glossary = st.checkbox("Show Glossary")

    if show_glossary:
        render_glossary()

# Run simulation
t, gammas, rhos, karmic = simulate_radiation(theta, entropy)
final_rho = rhos[-1]
final_k = karmic[-1]

# Results panel
col1, col2 = st.columns(2)
with col1:
    st.metric("Final Coherence γ", f"{gammas[-1]:.3f}")
    st.metric("Final Radiation ρ", f"{final_rho:.3f}")
with col2:
    st.metric("Karmic Load K", f"{final_k:.3f}")
    if final_rho > 2.5:
        st.error("⚠️ Symbolic Attractor Collapsing")
    elif final_rho > 1.0:
        st.warning("⚠️ Symbolic Leakage Increasing")
    else:
        st.success("System Coherent")

# Plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, gammas, label="γ(t) — Coherence")
ax.plot(t, rhos, label="ρ(t) — Radiation", linestyle='--')
ax.plot(t, karmic, label="K(t) — Karmic Load", linestyle=':')
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Symbolic Radiation & Collapse Over Time")
ax.legend()
st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("This simulation models symbolic Hawking radiation: information loss driven by identity instability in high-entropy, low-coherence symbolic fields.")
