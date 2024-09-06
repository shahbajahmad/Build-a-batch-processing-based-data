# main.py
from network_device import NetworkDevice
from network_analysis import NetworkAnalysis
from security_evaluation import SecurityEvaluation
from data_handler import DataHandler
from proposal_generator import ProposalGenerator

def main():
    # Load device data
    device_data = DataHandler.load_device_data('devices.json')

    # Initialize devices
    devices = []
    for data in device_data:
        device = NetworkDevice(data['name'], data['type'], data['cost'], data['specifications'])
        devices.append(device)

    # Perform network analysis
    internet_speed = 1000  # Assume 1000 Mbps
    analysis = NetworkAnalysis(devices, internet_speed)
    performance_data = analysis.simulate_performance()

    # Evaluate network security
    security = SecurityEvaluation(devices)
    security_scores = security.evaluate_security()

    # Generate proposal
    proposal = ProposalGenerator("UniversityNet", devices, performance_data, security_scores)
    proposal_text = proposal.generate_proposal()

    # Save proposal to file
    DataHandler.save_report(proposal_text, 'UniversityNet_Network_Proposal.txt')

    # Log the action
    DataHandler.append_to_log('project_log.txt', "Network proposal generated and saved.")

if __name__ == "__main__":
    main()
