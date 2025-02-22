# config.py - Stores simulation parameters and settings

# ODE Model Parameters
ODE_PARAMS = {
    "k1": 0.2,  # Rate of activation by APCs
    "k2": 0.1,  # Suppression by Tregs
    "k3": 0.5,  # Decay rate of CD4+ T cells
    "k4": 0.3,  # Activation rate of CD8+ T cells by APCs
    "k5": 0.6,  # IL-2 induced CD8+ T cell proliferation
    "k6": 0.4,  # Suppression of CD8+ T cells by Tregs
    "k7": 0.3,  # Decay rate of CD8+ T cells
    "k8": 0.2,  # IL-2 production by CD4+ T cells
    "k9": 0.1,  # IL-2 degradation rate
    "k10": 0.15, # Treg activation by IL-2
    "k11": 0.25, # Treg decay rate
    "k12": 0.4,  # IFN-γ production rate
    "k13": 0.2,  # IFN-γ degradation rate
}

# Initial Conditions for ODE Model
INITIAL_CONDITIONS = {
    "T_cd4_0": 0.1,  # Initial CD4+ T cells
    "T_cd8_0": 0.1,  # Initial CD8+ T cells
    "IL2_0": 0.1,    # Initial IL-2 concentration
    "Treg_0": 0.05,  # Initial Regulatory T cells
    "IFNg_0": 0.05   # Initial IFN-γ concentration
}

# Time Range for ODE Simulation
TIME_RANGE = {
    "start": 0,
    "end": 100,
    "num_points": 1000,
}

# Agent-Based Model Parameters
AGENT_MODEL_PARAMS = {
    "num_agents": 100,  # Number of T cell agents
    "apc_signal_variability": 0.2,  # Standard deviation for APC signal strength
    "activation_threshold": 0.5,  # Threshold for activation
}

# Differentiation Parameters for Sankey Diagram
DIFFERENTIATION_PARAMS = {
    "naive_to_effector": 0.4,  # % of naïve cells becoming effector cells
    "naive_to_memory": 0.6,    # % of naïve cells becoming memory cells
    "effector_apoptosis": 0.4, # % of effector cells undergoing apoptosis
    "memory_survival": 0.6     # % of memory cells remaining over time
}

# Cytokine Heatmap Scaling
CYTOKINE_SCALING = {
    "ifng_scale": 1.5,  # Scaling factor for IFN-γ visualization
}

# Plotting Configuration
PLOTTING_CONFIG = {
    "style": "whitegrid",  # Seaborn style
    "figsize": (10, 5),
    "colors": {
        "cd4_t_cells": "blue",
        "cd8_t_cells": "orange",
        "il2": "red",
        "tregs": "green",
        "ifng": "purple",
        "active_cells": "purple",
        "cytokine_levels": "cyan",
    }
}
