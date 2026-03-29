import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        with patch('weather_service.api_client.fetch_weather_data', return_value={"temp": 25, "condition": "sunny"}):
            result = weather_service.get_weather("London")
            self.assertEqual(result["temp"], 25)

    def test_get_weather_api_error(self):
        # Simulate API error by raising an exception
        with patch('weather_service.api_client.fetch_weather_data', side_effect=Exception("API Error")):
            with self.assertRaises(Exception) as context:
                weather_service.get_weather("London")
            self.assertIn("API Error", str(context.exception))

    def test_get_weather_timeout(self):
        # Simulate timeout by raising TimeoutError
        with patch('weather_service.api_client.fetch_weather_data', side_effect=TimeoutError("Timeout")):
            with self.assertRaises(TimeoutError) as context:
                weather_service.get_weather("London")
            self.assertIn("Timeout", str(context.exception))

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [
            {"day": "Monday", "temp": 25, "condition": "Sunny"},
            {"day": "Tuesday", "temp": 22, "condition": "Cloudy"},
        ]
        result = weather_service.get_forecast("London", days=2)
        # The function does not return, but we can check the mock was called
        mock_fetch.assert_called_once_with("London", 2)

    @patch("weather_service.api_client.get_current_hour")
    def test_get_current_time_mocked(self, mock_get_hour):
        # Test morning
        mock_get_hour.return_value = 8
        greeting = weather_service.get_greeting_based_on_time()
        self.assertEqual(greeting, "Good morning!")
        # Test afternoon
        mock_get_hour.return_value = 15
        greeting = weather_service.get_greeting_based_on_time()
        self.assertEqual(greeting, "Good afternoon!")
        # Test evening
        mock_get_hour.return_value = 22
        greeting = weather_service.get_greeting_based_on_time()
        self.assertEqual(greeting, "Good evening!")


if __name__ == "__main__":
    unittest.main()
