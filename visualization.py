# visualization.py - Handles advanced plotting and data analysis
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.sankey import Sankey

# Function to plot ODE results with enhanced visualization
def plot_ode_results(time_range, solution):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    plt.plot(time_range, solution[:, 0], label='CD4+ T Cells', linewidth=2, color='blue')
    plt.plot(time_range, solution[:, 1], label='CD8+ T Cells', linewidth=2, linestyle='dashed', color='orange')
    plt.plot(time_range, solution[:, 2], label='IL-2 Concentration', linewidth=2, linestyle='dotted', color='red')
    plt.plot(time_range, solution[:, 3], label='Regulatory T Cells', linewidth=2, linestyle='dashdot', color='green')
    
    plt.xlabel("Time (hours)")
    plt.ylabel("Concentration (normalized)")
    plt.title("T Cell Activation Dynamics with IL-2 Feedback and Tregs")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot agent-based model results
def plot_agent_results(active_cells_list, cytokine_levels_list):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    plt.bar(range(len(active_cells_list)), active_cells_list, color='green', alpha=0.6, label='Active Cells')
    plt.plot(range(len(cytokine_levels_list)), cytokine_levels_list, color='purple', marker='o', linestyle='dashed', label='Cytokine Levels')
    
    plt.xlabel("Simulation Run")
    plt.ylabel("Cell Count / Cytokine Level")
    plt.title("Agent-Based Model: Active T Cells vs. Cytokine Levels")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot heatmap of IL-2 & IFN-γ levels over time
def plot_cytokine_heatmap(time_range, cytokine_data):
    plt.figure(figsize=(10, 6))
    sns.heatmap(np.array(cytokine_data).reshape(-1, len(time_range)), cmap="viridis", cbar=True)
    plt.xlabel("Time (hours)")
    plt.ylabel("Simulation Runs")
    plt.title("Heatmap of IL-2 & IFN-γ Levels Over Time")
    plt.show()

# Function to plot a Sankey diagram for T cell differentiation
def plot_tcell_sankey():
    Sankey(flows=[100, -40, -60, 40, 60], 
           labels=["Naïve T Cells", "Effector T Cells", "Memory T Cells", "Apoptosis", "Differentiation"],
           orientations=[0, 1, 1, -1, -1]).finish()
    plt.title("T Cell Differentiation Pathways")
    plt.show()

# Example Execution (if running standalone)
if __name__ == "__main__":
    time_range = np.linspace(0, 100, 1000)
    fake_solution = np.column_stack((np.sin(time_range / 10), np.cos(time_range / 10),
                                     np.sin(time_range / 20), np.cos(time_range / 20)))
    plot_ode_results(time_range, fake_solution)
    
    active_cells = np.random.randint(50, 100, 10)
    cytokine_levels = np.random.rand(10) * 10
    plot_agent_results(active_cells, cytokine_levels)
    
    # Generate synthetic data for the new visualizations
    cytokine_data = np.random.rand(10, len(time_range)) * 10
    plot_cytokine_heatmap(time_range, cytokine_data)
    
    plot_tcell_sankey()
