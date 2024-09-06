# network_device.py
class NetworkDevice:
    def __init__(self, name, device_type, cost, specifications):
        self.name = name
        self.device_type = device_type
        self.cost = cost
        self.specifications = specifications

    def device_info(self):
        info = f"Device: {self.name}\nType: {self.device_type}\nCost: ${self.cost}\n"
        info += "Specifications:\n"
        for key, value in self.specifications.items():
            info += f"  {key}: {value}\n"
        return info
