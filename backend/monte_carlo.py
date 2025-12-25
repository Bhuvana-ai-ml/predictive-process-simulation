# backend/monte_carlo.py

#from backend.simulation import run_simulation
from .simulation import run_simulation


def monte_carlo_simulation(
    runs=200,
    arrival_rate=20,
    num_agents=5,
    sla_hours=4,
    simulation_hours=8
):
    breach_rates = []

    for _ in range(runs):
        cases = run_simulation(
            arrival_rate,
            num_agents,
            sla_hours,
            simulation_hours
        )

        if not cases:
            continue

        breached = sum(1 for c in cases if c.sla_breached())
        breach_rate = breached / len(cases)
        breach_rates.append(breach_rate)

    return {
        "average_risk": sum(breach_rates) / len(breach_rates),
        "min_risk": min(breach_rates),
        "max_risk": max(breach_rates),
    }


def what_if_analysis(
    agent_counts,
    runs=200,
    arrival_rate=20,
    sla_hours=4,
    simulation_hours=8
):
    results = {}

    for agents in agent_counts:
        result = monte_carlo_simulation(
            runs=runs,
            arrival_rate=arrival_rate,
            num_agents=agents,
            sla_hours=sla_hours,
            simulation_hours=simulation_hours
        )
        results[agents] = result["average_risk"]

    return results


if __name__ == "__main__":
    agents_test = [4, 5, 6, 7]
    risks = what_if_analysis(agents_test)

    for agents, risk in risks.items():
        print(f"Agents: {agents} → SLA Risk: {risk:.2%}")
