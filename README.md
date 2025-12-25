Predictive Process Simulation for SLA Risk Forecasting

This project demonstrates a predictive, simulation-based approach to estimate Service Level Agreement (SLA) breach risk in operational workflows before violations occur. Many organizations such as insurance companies, banks, customer support centers, and government departments process a large number of cases every day under strict SLA constraints. Traditional monitoring systems are reactive in nature and usually identify SLA breaches only after they have already happened. This project focuses on moving from reactive monitoring to proactive decision-making.

The core idea of the project is that SLA violations are primarily caused by variability in arrivals, service times, and resource availability rather than simple averages. Instead of relying on historical reports, the system simulates how work may flow in the near future under current conditions. Discrete Event Simulation is used to model cases, queues, and agents realistically, while Monte Carlo simulation is applied to run multiple future scenarios in order to quantify uncertainty and risk.

The system takes basic operational parameters such as case arrival rate, number of agents, SLA duration, and simulation window as inputs. Based on these inputs, it estimates the probability of SLA breaches, classifies the risk level, and shows how changes in staffing impact the overall risk. An interactive Streamlit dashboard allows users to adjust parameters and immediately see the effect on SLA risk, making the system suitable for demonstration and decision support.

The project is implemented using Python with SimPy for discrete event simulation, NumPy for numerical computation, and Streamlit for the user interface. The backend logic is modular and separated from the UI, following clean software engineering practices. The solution is intended as a prototype to demonstrate predictive process simulation rather than a full production deployment.

To run the project locally, install the required dependencies using the provided requirements file and start the Streamlit application from the project root. Once running, the dashboard can be accessed in a web browser where users can experiment with different operational scenarios and observe how SLA risk changes.

This project highlights how simulation can be used as a powerful decision-support tool for operations management by providing early warnings, reducing firefighting, and enabling proactive planning. The approach is applicable across multiple industries wherever time-bound processes and SLAs are critical.

Developed by Bhuvana, B.Tech CSE (Artificial Intelligence and Machine Learning).
GitHub repository: https://github.com/Bhuvana-ai-ml/predictive-process-simulation