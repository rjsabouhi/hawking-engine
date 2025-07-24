# glossary.py

import streamlit as st

def render_glossary():
    st.markdown("## Symbolic Glossary")
    st.markdown("---")

    glossary = {
        "γ(t) — Coherence": "How in-sync current identity is with memory. High = stable, low = fragmented.",
        "μ(t) — Memory Tension": "How strongly symbolic patterns are reinforced over time. High = heavy reinforcement (can be stabilizing or obsessive).",
        "∇S(t) — Entropy Gradient": "Symbolic disorder. Represents internal tension, contradiction, or unresolved structure.",
        "Θ(t) — Clinging": "Resistance to symbolic change. High Θ means identity is gripping the past or present too tightly.",
        "τ(t) — Symbolic Time Drift": "The subjective rate of internal time. High = time feels fast; low = time slows or collapses.",
        "δ(t) — Drift": "Deviation from symbolic baseline. High drift = loss of coherent identity.",
        "K(t) — Karmic Load": "Stabilization pressure. Emerges from too much clinging, entropy, and low coherence. System will slow itself down to rebalance.",
        "ψ — System Fate": "Trajectory of the system: recover, rebase (new attractor), or collapse from symbolic overload."
    }

    for label, explanation in glossary.items():
        st.markdown(f"**{label}**  \n{explanation}")
