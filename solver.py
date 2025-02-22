# solver.py - Solves the ODE and Agent-Based Model with Advanced Visualizations

import numpy as np
from scipy.integrate import odeint
from models import tcell_ode, agent_based_model
import matplotlib.pyplot as plt
from visualization import plot_ode_results, plot_agent_results, plot_cytokine_heatmap, plot_tcell_sankey

# Solve ODE Model with Updated Variables
def solve_ode(params, initial_conditions, time_range):
    """
    Solves the ODE system for T Cell Activation, now including IFN-γ.
    """
    solution = odeint(tcell_ode, initial_conditions, time_range, args=(params,))
    return solution

# Run Agent-Based Model Simulation
def run_agent_simulation(n_agents=100, apc_signal=0.7):
    """
    Simulates an agent-based model of T cell activation.
    """
    active_cells, avg_il2, avg_ifng = agent_based_model(n_agents, apc_signal)
    return active_cells, avg_il2, avg_ifng  # ✅ Now correctly returns IFN-γ

# Example Execution (Standalone Run)
if __name__ == "__main__":
    params = [0.2, 0.1, 0.5, 0.3, 0.6, 0.4, 0.3, 0.2, 0.1, 0.15, 0.25, 0.4, 0.2, 1.0]  # Sample parameters with IFN-γ
    initial_conditions = [0.1, 0.1, 0.1, 0.05, 0.05]  # Initial values for CD4, CD8, IL-2, Tregs, IFN-γ
    time_range = np.linspace(0, 100, 1000)

    # 🔵 Solve ODE Model
    ode_solution = solve_ode(params, initial_conditions, time_range)
    plot_ode_results(time_range, ode_solution)  # 📈 Line Plot

    # 🔥 Generate Cytokine Heatmap (IL-2 & IFN-γ over time)
    plot_cytokine_heatmap(time_range, ode_solution[:, 2], ode_solution[:, 4])

    # 🟢 Run Agent-Based Model Simulation
    active_cells, avg_cytokine = run_agent_simulation()
    print(f"Active Cells: {active_cells}, Average Cytokine Level: {avg_cytokine}")

    # 🔄 Generate Multiple Runs for Variability Analysis
    active_cells_list = []
    cytokine_levels_list = []
    for _ in range(10):
        active, cytokine = run_agent_simulation()
        active_cells_list.append(active)
        cytokine_levels_list.append(cytokine)

    # 📊 Plot Agent-Based Model Simulation
    plot_agent_results(active_cells_list, cytokine_levels_list)

    # 🔀 Generate T Cell Differentiation Sankey Diagram
    plot_tcell_sankey()

    print("✅ Simulation complete with full visualizations.")
