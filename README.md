# T Cell Activation Computational Model

## Overview
This project models **T cell activation, cytokine feedback loops, and immune regulation** using:
- **Ordinary Differential Equations (ODEs)** to simulate **T cell activation dynamics**
- **Agent-Based Modeling (ABM)** to introduce **stochasticity in immune responses**
- **Data visualization** to analyze immune response variations and cytokine effects
- **Heatmaps and Sankey diagrams** to enhance interpretation of immune dynamics

The project is implemented in **Python** and is structured into multiple modules for clarity and modularity. A **FastAPI-based web interface** is also provided for interactive simulations.

---
## Installation & Requirements
### 1. Install Dependencies
Ensure you have Python installed (recommended: Python 3.8+). Install required libraries:
```bash
pip install numpy scipy matplotlib seaborn fastapi uvicorn
```

### 2. Clone the Repository
```bash
git clone <repository-url>
cd TCell-Activation-Model
```

### 3. Run the Web Application
To start the FastAPI-based interface:
```bash
uvicorn api:app --reload
```
Open `http://127.0.0.1:8000` in a browser to use the interactive UI.

---
## Project Structure
```
├── models.py        # Defines ODE and Agent-Based Models
├── solver.py        # Solves ODEs and runs agent-based simulations
├── visualization.py # Generates plots and analyzes results
├── config.py        # Stores model parameters and configurations
├── api.py           # FastAPI server to run simulations via a web UI
├── main.py          # Integrates all modules and runs the simulations
├── web/             # Web interface for the model
│   ├── static/      # CSS & JS for the UI
│   ├── templates/   # HTML files
├── README.md        # Project documentation
├── references.bib   # Bibliography of cited immunology sources
```

---
## Running the Simulation
### **1. Command-Line Execution**
Run the following command to execute the full simulation:
```bash
python main.py
```
This will:
1. **Solve the ODE model** and plot **T cell activation, IL-2, and IFN-γ dynamics**.
2. **Run the agent-based model** and display **active T cells & cytokine levels**.
3. **Generate heatmaps and Sankey diagrams** for cytokine interactions and T cell differentiation.

### **2. Running via Web UI**
1. Start the FastAPI server:
   ```bash
   uvicorn api:app --reload
   ```
2. Open `http://127.0.0.1:8000` in a web browser.
3. Adjust parameters and click **Run Simulation** to generate **real-time visualizations**.

---
## Model Descriptions
### **1. ODE Model (T Cell Activation & Cytokine Feedback)**
The ODE model governs **T cell proliferation**, **IL-2 production**, **IFN-γ regulation**, and **Treg suppression**.
#### **Differential Equations:**
```math
\frac{dT_{cd4}}{dt} = k_1 \cdot APC - k_2 \cdot Treg - k_3 \cdot T_{cd4}
```
```math
\frac{dT_{cd8}}{dt} = k_4 \cdot APC + k_5 \cdot IL_2 - k_6 \cdot Treg - k_7 \cdot T_{cd8}
```
```math
\frac{dIL_2}{dt} = k_8 \cdot T_{cd4} - k_9 \cdot IL_2
```
```math
\frac{dTreg}{dt} = k_{10} \cdot IL_2 - k_{11} \cdot Treg
```
```math
\frac{dIFN_γ}{dt} = k_{12} \cdot T_{cd8} - k_{13} \cdot IFN_γ
```

### **2. Agent-Based Model (ABM)**
Each agent represents a **T cell interacting with an APC signal**. Stochasticity is introduced using:
- **Random activation thresholds** for each T cell
- **Cytokine response variation per activation**

The model runs **multiple simulations** to assess **population-level immune responses**.

### **3. Visualizations & Analysis**
- **ODE Model Results**: Line plots showing changes in **CD4+, CD8+, IL-2, Tregs, and IFN-γ** over time.
- **Agent-Based Model Results**: Bar charts displaying **active T cells vs. cytokine levels** over multiple runs.
- **Cytokine Heatmap**: A **heatmap of IL-2 and IFN-γ concentrations** over time.
- **T Cell Differentiation Sankey Diagram**: A flow diagram showing **naïve-to-effector-memory transitions**.

---
## Results & Interpretation
### **1. ODE Results**
- Show how **T cell activation**, **IL-2 secretion**, and **IFN-γ regulation** change over time.
- Demonstrate **feedback mechanisms** between cytokines and Tregs.

### **2. Agent-Based Model Results**
- Illustrate **variation in immune responses** due to stochastic effects.
- Help compare **different antigen stimulation levels**.

### **3. Cytokine Heatmaps**
- Provide insight into the **spatiotemporal distribution of IL-2 and IFN-γ**.

### **4. T Cell Differentiation Sankey Diagram**
- Visualizes transitions between **naïve, effector, and memory T cells**.

---
## References
All immunological assumptions are backed by peer-reviewed sources. Citations are available in `references.bib`.

---
## Future Improvements
- Implement **multi-cytokine signaling networks** (e.g., IL-10, TNF-α).
- Introduce **cell differentiation stages** (e.g., effector vs. memory T cells).
- Explore **machine learning-based predictions** for immune responses.

---
## Contributors
- **Praise Ogwuche**
- [praiseogwuche@uni.minerva.edu]

For inquiries, feel free to reach out!

---
## License
This project is open-source under the **MIT License**.

