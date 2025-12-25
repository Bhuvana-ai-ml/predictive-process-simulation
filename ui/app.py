# ui/app.py

import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
from backend.monte_carlo import monte_carlo_simulation

st.set_page_config(page_title="SLA Risk Predictor", layout="centered")

st.title("🔮 Predictive SLA Risk Simulator")

arrival_rate = st.slider("Arrival Rate (cases/hour)", 5, 30, 20)
num_agents = st.slider("Number of Agents", 2, 10, 5)
sla_hours = st.slider("SLA Duration (hours)", 1, 8, 4)

if st.button("Run Simulation"):
    with st.spinner("Simulating future scenarios..."):
        result = monte_carlo_simulation(
            runs=200,
            arrival_rate=arrival_rate,
            num_agents=num_agents,
            sla_hours=sla_hours,
            simulation_hours=8
        )

    risk = result["average_risk"]
    #st.subheader("📊 SLA Risk Forecast")
    st.metric("Average SLA Breach Risk", f"{risk:.2%}")
    st.markdown("### 📊 SLA Risk Forecast (Next 8 Hours)")
    st.caption("Based on Monte Carlo simulation of operational variability")

    st.divider()

    if risk > 0.30:
        st.error(f"🔴 HIGH RISK — {risk:.2%}")
    elif risk > 0.15:
        st.warning(f"🟠 MEDIUM RISK — {risk:.2%}")
    else:
        st.success(f"🟢 LOW RISK — {risk:.2%}")
    st.subheader("🔁 What-If Staffing Analysis")

    agent_range = [num_agents - 1, num_agents, num_agents + 1]
    agent_range = [a for a in agent_range if a > 0]

    from backend.monte_carlo import what_if_analysis
    what_if = what_if_analysis(agent_range)

    st.bar_chart(what_if)
    st.caption("Comparison of average SLA breach risk under different staffing levels")
