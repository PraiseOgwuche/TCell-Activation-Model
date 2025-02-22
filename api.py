import io
import base64
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from solver import solve_ode, run_agent_simulation
from visualization import plot_ode_results, plot_agent_results, plot_cytokine_heatmap, plot_tcell_sankey
from config import ODE_PARAMS, INITIAL_CONDITIONS, TIME_RANGE, AGENT_MODEL_PARAMS

app = FastAPI()

# Serve static files (CSS & JS)
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# Serve frontend HTML file
@app.get("/")
def serve_frontend():
    return FileResponse("web/templates/index.html")

@app.get("/run_simulation")
def run_simulation(request: Request):
    # Get parameters from frontend
    apc_signal = float(request.query_params.get("apc", 1.0))
    treg_factor = float(request.query_params.get("treg", 0.5))
    ifngamma = request.query_params.get("ifng", "no")

    # Dynamically update APC availability
    params = [
        ODE_PARAMS["k1"], ODE_PARAMS["k2"], ODE_PARAMS["k3"],
        ODE_PARAMS["k4"], ODE_PARAMS["k5"], ODE_PARAMS["k6"],
        ODE_PARAMS["k7"], ODE_PARAMS["k8"], ODE_PARAMS["k9"],
        ODE_PARAMS["k10"], ODE_PARAMS["k11"], 
        ODE_PARAMS["k12"], ODE_PARAMS["k13"], 
        apc_signal  # ✅ Fix: Use dynamic APC signal
    ]

    initial_conditions = [
        INITIAL_CONDITIONS["T_cd4_0"], INITIAL_CONDITIONS["T_cd8_0"],
        INITIAL_CONDITIONS["IL2_0"], INITIAL_CONDITIONS["Treg_0"],
        INITIAL_CONDITIONS["IFNg_0"]
    ]

    # Solve ODE model
    time_range = np.linspace(TIME_RANGE["start"], TIME_RANGE["end"], TIME_RANGE["num_points"])
    ode_solution = solve_ode(params, initial_conditions, time_range)

    # ✅ Generate ODE plot
    plt.clf()
    buf = io.BytesIO()
    plt.figure()
    plot_ode_results(time_range, ode_solution)
    plt.savefig(buf, format="png", bbox_inches='tight')
    plt.close()
    ode_plot = base64.b64encode(buf.getvalue()).decode("utf-8")

    # ✅ Generate Cytokine Heatmap for IFN-γ
    plt.clf()
    buf = io.BytesIO()
    plt.figure()
    plot_cytokine_heatmap(time_range, ode_solution[:, 4])
    plt.savefig(buf, format="png", bbox_inches='tight')
    plt.close()
    cytokine_heatmap = base64.b64encode(buf.getvalue()).decode("utf-8")

    # ✅ Now correctly handles three return values from run_agent_simulation()
    active_cells, avg_il2, avg_ifng = run_agent_simulation(
        n_agents=AGENT_MODEL_PARAMS["num_agents"],
        apc_signal=apc_signal
    )

    # ✅ Generate Agent-Based Model plot
    plt.clf()
    buf = io.BytesIO()
    plt.figure()
    active_cells_list = []
    cytokine_levels_list = []
    ifng_levels_list = []  # ✅ Add IFN-γ tracking
    for _ in range(10):
        active, il2, ifng = run_agent_simulation(
            n_agents=AGENT_MODEL_PARAMS["num_agents"],
            apc_signal=apc_signal
        )
        active_cells_list.append(active)
        cytokine_levels_list.append(il2)
        ifng_levels_list.append(ifng)

    plot_agent_results(active_cells_list, cytokine_levels_list)
    plt.savefig(buf, format="png", bbox_inches='tight')
    plt.close()
    agent_plot = base64.b64encode(buf.getvalue()).decode("utf-8")

    # ✅ Generate Sankey Diagram for T Cell Differentiation
    plt.clf()
    buf = io.BytesIO()
    plt.figure()
    plot_tcell_sankey()
    plt.savefig(buf, format="png", bbox_inches='tight')
    plt.close()
    sankey_plot = base64.b64encode(buf.getvalue()).decode("utf-8")

    return JSONResponse(content={
        "active_cells": active_cells,  # ✅ FIXED: Using single-run results
        "avg_il2": avg_il2,
        "avg_ifng": avg_ifng,
        "ode_plot": f"data:image/png;base64,{ode_plot}",
        "cytokine_heatmap": f"data:image/png;base64,{cytokine_heatmap}",
        "agent_plot": f"data:image/png;base64,{agent_plot}",
        "sankey_plot": f"data:image/png;base64,{sankey_plot}"
    })
