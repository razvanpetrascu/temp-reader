import unittest
from unittest.mock import patch
from cpu_monitor.core import get_cpu_temperature_reading

class TestCpuTemperatureReading(unittest.TestCase):
    @patch('cpu_monitor.core.get_cpu_temperature')
    def test_get_cpu_temperature_reading(self, mock_get_cpu_temperature):
        # Arrange: Mock the CPU temperature value
        mock_get_cpu_temperature.return_value = 55.0
        
        # Act: Call the function
        result = get_cpu_temperature_reading()
        
        # Assert: Check if the output is formatted correctly
        self.assertEqual(result, "CPU Temperature: 55.0°C")

if __name__ == '__main__':
    unittest.main()
