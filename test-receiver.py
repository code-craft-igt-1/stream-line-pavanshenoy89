import unittest
from receiver import Receiver


class ReceiverTest(unittest.TestCase):

    def setUp(self):
        self.metrics = Receiver()

    def test_initialization(self):
        self.assertEqual(len(self.metrics.temperatures), 0)
        self.assertEqual(len(self.metrics.pulse_rates), 0)
        self.assertEqual(len(self.metrics.spo2_levels), 0)
        self.assertEqual(self.metrics.max_temp, float('-inf'))
        self.assertEqual(self.metrics.min_temp, float('inf'))
        self.assertEqual(self.metrics.max_pulse, float('-inf'))
        self.assertEqual(self.metrics.min_pulse, float('inf'))
        self.assertEqual(self.metrics.max_spo2, float('-inf'))
        self.assertEqual(self.metrics.min_spo2, float('inf'))

    def test_update_metrics(self):
        self.metrics.update_metrics(85.0, 90.0, 95.0)
        self.assertEqual(self.metrics.max_temp, 85.0)
        self.assertEqual(self.metrics.min_temp, 85.0)
        self.assertEqual(self.metrics.max_pulse, 90.0)
        self.assertEqual(self.metrics.min_pulse, 90.0)
        self.assertEqual(self.metrics.max_spo2, 95.0)
        self.assertEqual(self.metrics.min_spo2, 95.0)

    def test_moving_average_not_calculated_before_five_entries(self):
        for i in range(4):
            self.metrics.update_metrics(80 + i, 70 + i, 60 + i)

    def test_moving_average_calculation_after_five_entries(self):
        for i in range(5):
            self.metrics.update_metrics(80 + i, 70 + i, 60 + i)

    def test_max_min_update_with_extreme_values(self):
        self.metrics.update_metrics(-1000.0, -1000.0, -1000.0)
        self.assertEqual(self.metrics.max_temp, -1000.0)
        self.assertEqual(self.metrics.min_temp, -1000.0)


if __name__ == '__main__':
    unittest.main()
