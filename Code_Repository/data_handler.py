# data_handler.py
import json

class DataHandler:
    @staticmethod
    def load_device_data(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_report(report, filename):
        with open(filename, 'w') as file:
            file.write(report)

    @staticmethod
    def append_to_log(log_filename, message):
        with open(log_filename, 'a') as log_file:
            log_file.write(message + "\n")
