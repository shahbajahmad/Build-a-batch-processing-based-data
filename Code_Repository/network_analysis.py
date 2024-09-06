# network_analysis.py
import random

class NetworkAnalysis:
    def __init__(self, devices, internet_speed):
        self.devices = devices
        self.internet_speed = internet_speed

    def simulate_performance(self):
        performance = {}
        for device in self.devices:
            load_handling = random.uniform(0.8, 1.2) * self.internet_speed
            performance[device.name] = load_handling
        return performance

    def analyze_performance(self, performance_data):
        analysis = "Network Performance Analysis:\n"
        analysis += "=" * 50 + "\n"
        for device, performance in performance_data.items():
            analysis += f"{device}: {performance:.2f} Mbps\n"
        return analysis
