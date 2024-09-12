import unittest
from unittest.mock import patch, MagicMock
from cpu_monitor.platform_utils import get_cpu_temperature, get_windows_temp, get_linux_temp, get_macos_temp

class TestPlatformUtils(unittest.TestCase):

    @patch('cpu_monitor.platform_utils.platform.system')
    def test_get_cpu_temperature_windows(self, mock_platform_system):
        # Mock platform system to return 'Windows'
        mock_platform_system.return_value = 'Windows'
        
        # Mock the get_windows_temp to return a value
        with patch('cpu_monitor.platform_utils.get_windows_temp', return_value=45.0):
            result = get_cpu_temperature()
            self.assertEqual(result, 45.0)

    @patch('cpu_monitor.platform_utils.platform.system')
    def test_get_cpu_temperature_macos(self, mock_platform_system):
        # Mock platform system to return 'Darwin' (macOS)
        mock_platform_system.return_value = 'Darwin'
        
        # Mock the get_macos_temp to return a value
        with patch('cpu_monitor.platform_utils.get_macos_temp', return_value=60.0):
            result = get_cpu_temperature()
            self.assertEqual(result, 60.0)

    @patch('cpu_monitor.platform_utils.platform.system')
    def test_get_cpu_temperature_unsupported_os(self, mock_platform_system):
        # Mock platform system to return an unsupported OS
        mock_platform_system.return_value = 'UnsupportedOS'
        with self.assertRaises(OSError) as context:
            get_cpu_temperature()
        
        self.assertEqual(str(context.exception), "Unsupported operating system")

    @patch('cpu_monitor.platform_utils.wmi.WMI')
    def test_get_windows_temp(self, mock_wmi):
        # Mock WMI to return a mocked temperature object
        mock_instance = MagicMock()
        mock_instance.MSAcpi_ThermalZoneTemperature.return_value = [MagicMock(CurrentTemperature=2992)]
        mock_wmi.return_value = mock_instance

        result = get_windows_temp()

        # 2992 / 10 - 273.15 = 26.05
        self.assertAlmostEqual(result, 26.05, places=2)

    @patch('os.popen')
    def test_get_macos_temp(self, mock_popen):
        mock_popen.return_value.read.return_value = "75.0°C"

        result = get_macos_temp()

        self.assertEqual(result, 75.0)

if __name__ == '__main__':
    unittest.main()
