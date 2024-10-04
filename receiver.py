import sys
from collections import deque


class Receiver:
    def __init__(self):
        self.temperatures = deque(maxlen=5)
        self.pulse_rates = deque(maxlen=5)
        self.spo2_levels = deque(maxlen=5)
        self.max_temp = float('-inf')
        self.min_temp = float('inf')
        self.max_pulse = float('-inf')
        self.min_pulse = float('inf')
        self.max_spo2 = float('-inf')
        self.min_spo2 = float('inf')

    def update_metrics(self, temperature, pulse_rate, spo2):
        self.max_temp = max(self.max_temp, temperature)
        self.min_temp = min(self.min_temp, temperature)
        self.max_pulse = max(self.max_pulse, pulse_rate)
        self.min_pulse = min(self.min_pulse, pulse_rate)
        self.max_spo2 = max(self.max_spo2, spo2)
        self.min_spo2 = min(self.min_spo2, spo2)

        self.temperatures.append(temperature)
        self.pulse_rates.append(pulse_rate)
        self.spo2_levels.append(spo2)

        print(f"Max Temperature: {self.max_temp}, Min Temperature: {self.min_temp}")
        print(f"Max Pulse Rate: {self.max_pulse}, Min Pulse Rate: {self.min_pulse}")
        print(f"Max SPO2: {self.max_spo2}, Min SPO2: {self.min_spo2}")

    def moving_average(self):
        if len(self.temperatures) == 5:
            avg_temp = sum(self.temperatures) / 5
            avg_pulse = sum(self.pulse_rates) / 5
            avg_spo2 = sum(self.spo2_levels) / 5
            print(f"Moving Average Temperature: {avg_temp:.4f}, "
                  f"Moving Average Pulse Rate: {avg_pulse:.4f}, "
                  f"Moving Average SPO2: {avg_spo2:.4f}")


if __name__ == '__main__':
    metrics = Receiver()
    for line in sys.stdin:
        parts = line.strip().split(', ')

        temp_str, pulse_str, spo2_str = parts[0], parts[1], parts[2]

        temperature = float(temp_str.split('= ')[1])
        pulse_rate = float(pulse_str.split('= ')[1])
        spo2 = float(spo2_str.split('= ')[1])

        metrics.update_metrics(temperature, pulse_rate, spo2)
        metrics.moving_average()
