# backend/models.py

class Case:
    def __init__(self, case_id, arrival_time, sla_hours):
        self.case_id = case_id
        self.arrival_time = arrival_time
        self.sla_hours = sla_hours
        self.start_service_time = None
        self.end_service_time = None

    def sla_breached(self):
        if self.end_service_time is None:
            return False
        return (self.end_service_time - self.arrival_time) > self.sla_hours
