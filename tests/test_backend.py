import unittest
from backend import app, init_db

class TestBackend(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_post_registros(self):
        payload = {
            "cpf": "12345678900",
            "baseline_value": 120, "accelerations": 0.003, "fetal_movement": 0.0,
            "uterine_contractions": 0.0, "light_decelerations": 0.0, "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0, "abnormal_short_term_variability": 0,
            "mean_value_of_short_term_variability": 0.5, "percentage_of_time_with_abnormal_long_term_variability": 0,
            "mean_value_of_long_term_variability": 0.5, "histogram_width": 50, "histogram_min": 60,
            "histogram_max": 180, "histogram_number_of_peaks": 2, "histogram_number_of_zeroes": 0,
            "histogram_mode": 120, "histogram_mean": 120, "histogram_median": 120,
            "histogram_variance": 120, "histogram_tendency": 0
        }
        response = self.client.post('/registros', json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn('fetalhealth', response.get_json())

    def test_get_registros(self):
        response = self.client.get('/registros')
        self.assertEqual(response.status_code, 200)

    def test_empty_payload(self):
        response = self.client.post('/registros', json={})
        self.assertIn(response.status_code, [400, 422, 500])

    def test_ml_service_unavailable(self):
        import backend
        original_post = backend.requests.post
        def mock_post(*args, **kwargs):
            raise Exception("ML service unavailable")
        backend.requests.post = mock_post
        payload = {
            "cpf": "12345678900",
            "baseline_value": 120, "accelerations": 0.003, "fetal_movement": 0.0,
            "uterine_contractions": 0.0, "light_decelerations": 0.0, "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0, "abnormal_short_term_variability": 0,
            "mean_value_of_short_term_variability": 0.5, "percentage_of_time_with_abnormal_long_term_variability": 0,
            "mean_value_of_long_term_variability": 0.5, "histogram_width": 50, "histogram_min": 60,
            "histogram_max": 180, "histogram_number_of_peaks": 2, "histogram_number_of_zeroes": 0,
            "histogram_mode": 120, "histogram_mean": 120, "histogram_median": 120,
            "histogram_variance": 120, "histogram_tendency": 0
        }
        response = self.client.post('/registros', json=payload)
        self.assertIn(response.status_code, [500, 502, 503])
        backend.requests.post = original_post

if __name__ == '__main__':
    unittest.main() 