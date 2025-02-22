# models.py - Defines the T Cell Activation & Differentiation Models

import numpy as np
from scipy.integrate import odeint
import random
from config import DIFFERENTIATION_PARAMS

# Updated ODE-based T cell activation model with CD4+, CD8+, Tregs, and IFN-γ
def tcell_ode(y, t, params):
    """
    Defines the ODE system for T Cell Activation.

    y[0] = CD4+ Helper T Cells (T_cd4)
    y[1] = CD8+ Cytotoxic T Cells (T_cd8)
    y[2] = IL-2 Cytokine Concentration
    y[3] = Regulatory T Cells (Treg)
    y[4] = IFN-γ Cytokine Concentration

    params = [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, APC]
    """
    T_cd4, T_cd8, IL2, Treg, IFNg = y
    k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, APC = params

    # CD4+ T Cell Activation (regulated by APC and suppressed by Treg)
    dT_cd4_dt = k1 * APC - k2 * Treg - k3 * T_cd4

    # CD8+ T Cell Activation (depends on APC, IL-2, and suppression by Treg)
    dT_cd8_dt = k4 * APC + k5 * IL2 - k6 * Treg - k7 * T_cd8

    # IL-2 Production (Produced by CD4+ T cells)
    dIL2_dt = k8 * T_cd4 - k9 * IL2

    # Regulatory T Cell Activation (Increases with IL-2)
    dTreg_dt = k10 * IL2 - k11 * Treg

    # IFN-γ Production (Produced by activated CD8+ T cells)
    dIFNg_dt = k12 * T_cd8 - k13 * IFNg

    return [dT_cd4_dt, dT_cd8_dt, dIL2_dt, dTreg_dt, dIFNg_dt]

# 🔀 T Cell Differentiation Model for Sankey Diagram
def tcell_differentiation():
    """
    Simulates differentiation from naïve T cells to Effector or Memory T cells.
    Used for Sankey diagram visualization.
    """
    naive_cells = 100  # Starting naïve T cell count

    # Differentiation rates from config
    effector_count = int(naive_cells * DIFFERENTIATION_PARAMS["naive_to_effector"])
    memory_count = int(naive_cells * DIFFERENTIATION_PARAMS["naive_to_memory"])
    
    # Effector apoptosis & memory survival
    surviving_effector = int(effector_count * (1 - DIFFERENTIATION_PARAMS["effector_apoptosis"]))
    surviving_memory = int(memory_count * DIFFERENTIATION_PARAMS["memory_survival"])

    return {
        "Naïve T Cells": naive_cells,
        "Effector T Cells": effector_count,
        "Memory T Cells": memory_count,
        "Surviving Effector Cells": surviving_effector,
        "Surviving Memory Cells": surviving_memory,
    }

# 🦠 Agent-based T Cell Model with Cytokine Response
class TCellAgent:
    def __init__(self, activation_threshold=0.5):
        self.active = False
        self.activation_threshold = activation_threshold
        self.cytokine_response = 0
        self.il2_response = 0
        self.ifng_response = 0

    def interact_with_apc(self, apc_signal):
        """Simulates interaction with APC and possible activation."""
        if apc_signal > self.activation_threshold:
            self.active = True
            self.cytokine_response = random.uniform(0.1, 1.0)
            self.il2_response = random.uniform(0.05, 0.5)  # Some IL-2 production
            self.ifng_response = random.uniform(0.02, 0.4)  # Some IFN-γ production
        else:
            self.active = False
            self.cytokine_response = 0
            self.il2_response = 0
            self.ifng_response = 0

# Agent-based model simulation
def agent_based_model(n_agents=100, apc_signal=0.7):
    agents = [TCellAgent() for _ in range(n_agents)]
    active_cells = 0
    il2_levels = []
    ifng_levels = []

    for agent in agents:
        agent.interact_with_apc(apc_signal)
        if agent.active:
            active_cells += 1
            il2_levels.append(agent.il2_response)
            ifng_levels.append(agent.ifng_response)

    avg_il2 = sum(il2_levels) / len(il2_levels) if il2_levels else 0
    avg_ifng = sum(ifng_levels) / len(ifng_levels) if ifng_levels else 0

    return active_cells, avg_il2, avg_ifng  # 🟢 Now tracks IL-2 & IFN-γ
