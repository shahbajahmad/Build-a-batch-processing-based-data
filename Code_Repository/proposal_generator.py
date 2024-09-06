# proposal_generator.py
class ProposalGenerator:
    def __init__(self, company_name, devices, performance_data, security_scores):
        self.company_name = company_name
        self.devices = devices
        self.performance_data = performance_data
        self.security_scores = security_scores

    def generate_proposal(self):
        proposal = f"Network Architecture Proposal for {self.company_name}\n"
        proposal += "=" * 80 + "\n"
        proposal += "Device Information:\n"
        for device in self.devices:
            proposal += device.device_info() + "\n"
        proposal += "\nNetwork Performance Analysis:\n"
        for device, performance in self.performance_data.items():
            proposal += f"{device}: {performance:.2f} Mbps\n"
        proposal += "\nNetwork Security Evaluation:\n"
        for device, score in self.security_scores.items():
            proposal += f"{device}: Security Score = {score}/100\n"
        proposal += "\nTotal Estimated Cost: ${}\n".format(self.calculate_total_cost())
        return proposal

    def calculate_total_cost(self):
        return sum(device.cost for device in self.devices)
