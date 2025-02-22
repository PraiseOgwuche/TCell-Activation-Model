# main.py - Integrates all modules and runs simulations

import numpy as np
from solver import solve_ode, run_agent_simulation
from visualization import (
    plot_ode_results, plot_agent_results, 
    plot_cytokine_heatmap, plot_tcell_sankey, 
    plot_overlay_response
)
from config import ODE_PARAMS, INITIAL_CONDITIONS, TIME_RANGE, AGENT_MODEL_PARAMS

# Prepare ODE parameters
params = [
    ODE_PARAMS["k1"], ODE_PARAMS["k2"], ODE_PARAMS["k3"], ODE_PARAMS["k4"],
    ODE_PARAMS["k5"], ODE_PARAMS["k6"], ODE_PARAMS["k7"], ODE_PARAMS["k8"],
    ODE_PARAMS["k9"], ODE_PARAMS["k10"], ODE_PARAMS["k11"], ODE_PARAMS["k12"],
    ODE_PARAMS["k13"], ODE_PARAMS["APC"]
]

initial_conditions = [
    INITIAL_CONDITIONS["T_cd4_0"], INITIAL_CONDITIONS["T_cd8_0"],
    INITIAL_CONDITIONS["IL2_0"], INITIAL_CONDITIONS["Treg_0"],
    INITIAL_CONDITIONS["IFNg_0"]  # Fix: Ensure IFN-γ is included
]

time_range = np.linspace(TIME_RANGE["start"], TIME_RANGE["end"], TIME_RANGE["num_points"])

# Run ODE model simulation
ode_solution = solve_ode(params, initial_conditions, time_range)
plot_ode_results(time_range, ode_solution)

# Generate heatmap for IFN-γ concentration over time
plot_cytokine_heatmap(time_range, ode_solution[:, 4])

# Run agent-based model simulation
active_cells, avg_cytokine = run_agent_simulation(
    n_agents=AGENT_MODEL_PARAMS["num_agents"],
    apc_signal=AGENT_MODEL_PARAMS["apc_signal"]
)
print(f"Active Cells: {active_cells}, Average Cytokine Level: {avg_cytokine}")

# Generate multiple runs of agent-based simulation
active_cells_list = []
cytokine_levels_list = []
for _ in range(10):
    active, cytokine = run_agent_simulation(
        n_agents=AGENT_MODEL_PARAMS["num_agents"],
        apc_signal=AGENT_MODEL_PARAMS["apc_signal"]
    )
    active_cells_list.append(active)
    cytokine_levels_list.append(cytokine)

# Plot agent-based model results
plot_agent_results(active_cells_list, cytokine_levels_list)

# Generate T cell differentiation Sankey diagram
plot_tcell_sankey()

# Generate Healthy vs. Dysregulated Immune Response Overlay
plot_overlay_response(time_range, ode_solution)

print("Simulation complete.")
