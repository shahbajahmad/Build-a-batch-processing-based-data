# security_evaluation.py
class SecurityEvaluation:
    def __init__(self, devices):
        self.devices = devices

    def evaluate_security(self):
        security_scores = {}
        for device in self.devices:
            score = self._calculate_security_score(device)
            security_scores[device.name] = score
        return security_scores

    def _calculate_security_score(self, device):
        base_score = 80
        if 'Firewall' in device.device_type:
            base_score += 15
        if 'Advanced Malware Protection' in device.specifications:
            base_score += 10
        return base_score

    def security_report(self, security_scores):
        report = "Network Security Evaluation:\n"
        report += "=" * 50 + "\n"
        for device, score in security_scores.items():
            report += f"{device}: Security Score = {score}/100\n"
        return report
