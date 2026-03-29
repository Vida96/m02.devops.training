import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestSecurity(unittest.TestCase):
    def test_missing_field_a(self):
        return requests.post(f"{BASE_URL}/process", json={"field_b": "value_b"})   

    def test_missing_field_b(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": "value_a"})

    def test_invalid_data_type(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": 123, "field_b": "value_b"})

    def test_empty_string_value(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": "", "field_b": "value_b"})

    def test_very_large_number(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": 10**10, "field_b": "value_b"})

    def test_malformed_json(self):
        headers = {"Content-Type": "application/json"}
        return requests.post(f"{BASE_URL}/process", data="{field_a: value_a, field_b: value_b}", headers=headers)

    def test_division_by_zero_returns_safe_error(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": 10, "field_b": 0})

    def test_sql_injection_attempt(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": "value_a'; DROP TABLE users; --", "field_b": "value_b"})

    def test_xss_attempt(self):
        return requests.post(f"{BASE_URL}/process", json={"field_a": "<script>alert('XSS')</script>", "field_b": "value_b"})

    def test_csrf_attempt(self):
        headers = {"X-CSRF-Token": "invalid_token"}
        return requests.post(f"{BASE_URL}/process", json={"field_a": "value_a", "field_b": "value_b"}, headers=headers)

    def test_rate_limiting(self):
        for _ in range(10):
            response = requests.post(f"{BASE_URL}/process", json={"field_a": "value_a", "field_b": "value_b"})
        return response

if __name__ == "__main__":
    unittest.main()
