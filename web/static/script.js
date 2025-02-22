document.getElementById("runSimulation").addEventListener("click", function() {
    let apcSignal = document.getElementById("apcStrength").value;
    let tregFactor = document.getElementById("tregFactor").value;
    let ifngamma = document.getElementById("ifngamma").value;

    // Update displayed values
    document.getElementById("apcValue").textContent = apcSignal;
    document.getElementById("tregValue").textContent = tregFactor;

    fetch(`/run_simulation?apc=${apcSignal}&treg=${tregFactor}&ifng=${ifngamma}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("activeCells").textContent = data.active_cells;
            document.getElementById("cytokineLevel").textContent = data.avg_il2.toFixed(4);

            // ✅ Check if images exist before updating
            if (data.ode_plot) {
                document.getElementById("odePlot").src = data.ode_plot;
            }
            if (data.agent_plot) {
                document.getElementById("agentPlot").src = data.agent_plot;
            }
            if (data.cytokine_heatmap) {
                document.getElementById("cytokineHeatmap").src = data.cytokine_heatmap;
            }
            if (data.sankey_plot) {
                document.getElementById("sankeyPlot").src = data.sankey_plot;
            }
        })
        .catch(error => console.error("Error fetching data:", error));
});
