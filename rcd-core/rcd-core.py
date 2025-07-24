# rcd_core.py

"""
RCD-Core: The central symbolic simulation kernel with Karmic Constraint Encoding

This unifies key dynamics of the Recursive Cognitive Dynamics (RCD) framework:
- Identity state (H)
- Memory manifold (M)
- Coherence, drift, symbolic time
- Karmic constraint feedback via clinging, entropy, and coherence disruption

Author: One Gonethus & The Engine
"""

from typing import Dict
from kce import compute_karmic_load, apply_karmic_feedback

class RCDSystem:
    def __init__(self):
        # Symbolic state variables
        self.H = {}               # Current symbolic identity state
        self.M = []               # Memory trace manifold
        self.gamma = 1.0          # Phase coherence γ(t)
        self.mu = 1.0             # Memory tension μ(t)
        self.entropy = 1.0        # Symbolic entropy gradient ∇S(t)
        self.theta = 1.0          # Clinging parameter Θ(t)

        # Time + Drift + Karma
        self.tau = 1.0            # Symbolic time flow τ(t)
        self.drift = 0.0          # Identity drift δ(t)
        self.karmic_load = 0.0    # Karmic destabilization potential K(t)
        self.fate = "stabilize"   # System trajectory category

    def update_state(self, new_symbolic_input: Dict):
        """
        Inject symbolic input and update internal state accordingly.
        """
        self.H = new_symbolic_input
        self._update_memory()
        self._compute_drift_and_kce()
        self._compute_time()
        self._determine_fate()

    def _update_memory(self):
        self.M.append(self.H.copy())
        if len(self.M) > 100:
            self.M.pop(0)

    def _compute_drift_and_kce(self):
        self.gamma = 1 / (1 + self.theta * self.entropy)
        self.drift = self.mu * (1 - self.gamma)

        # --- Karmic feedback ---
        self.karmic_load = compute_karmic_load(self.theta, self.entropy, self.gamma)
        self.mu, self.tau = apply_karmic_feedback(self.karmic_load, self.mu, self.tau)

    def _compute_time(self):
        # τ(t) = γ(t) · (μ + ∇S)
        self.tau = self.gamma * (self.mu + self.entropy)

    def _determine_fate(self):
        if self.drift < 0.2:
            self.fate = "recover"
        elif self.drift < 0.6:
            self.fate = "rebase"
        else:
            self.fate = "collapse"

    def get_metrics(self) -> Dict:
        return {
            "gamma": self.gamma,
            "mu": self.mu,
            "entropy": self.entropy,
            "theta": self.theta,
            "tau": self.tau,
            "drift": self.drift,
            "karmic_load": self.karmic_load,
            "fate": self.fate
        }

