# backend/simulation.py

import simpy
import numpy as np
from .models import Case

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

def case_arrival(env, arrival_rate, agent_pool, sla_hours, results):
    case_id = 0

    while True:
        interarrival_time = np.random.exponential(1 / arrival_rate)
        yield env.timeout(interarrival_time)

        case = Case(case_id, env.now, sla_hours)
        env.process(handle_case(env, case, agent_pool, results))
        case_id += 1


def handle_case(env, case, agent_pool, results):
    with agent_pool.request() as request:
        yield request

        case.start_service_time = env.now

        service_time = np.random.exponential(1)  # avg 1 hour
        yield env.timeout(service_time)

        case.end_service_time = env.now
        results.append(case)


def run_simulation(
    arrival_rate=20,
    num_agents=5,
    sla_hours=4,
    simulation_hours=8
):
    env = simpy.Environment()
    agent_pool = simpy.Resource(env, capacity=num_agents)

    results = []

    env.process(
        case_arrival(env, arrival_rate, agent_pool, sla_hours, results)
    )

    env.run(until=simulation_hours)

    return results

if __name__ == "__main__":
    cases = run_simulation()

    total = len(cases)
    breached = sum(1 for c in cases if c.sla_breached())

    print(f"Total cases completed: {total}")
    print(f"SLA breaches: {breached}")
    print(f"Breach probability: {breached / total:.2f}")
