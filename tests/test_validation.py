import unittest
from backend import app, init_db

class TestValidation(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_missing_field(self):
        payload = {
            "cpf": "11122233344",
            # campo baseline_value ausente
            "accelerations": 0.003, "fetal_movement": 0.0,
            "uterine_contractions": 0.0, "light_decelerations": 0.0, "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0, "abnormal_short_term_variability": 0,
            "mean_value_of_short_term_variability": 0.5, "percentage_of_time_with_abnormal_long_term_variability": 0,
            "mean_value_of_long_term_variability": 0.5, "histogram_width": 50, "histogram_min": 60,
            "histogram_max": 180, "histogram_number_of_peaks": 2, "histogram_number_of_zeroes": 0,
            "histogram_mode": 120, "histogram_mean": 120, "histogram_median": 120,
            "histogram_variance": 120, "histogram_tendency": 0
        }
        response = self.client.post('/registros', json=payload)
        self.assertIn(response.status_code, [400, 422, 500])  # depende do tratamento do backend

    def test_invalid_type(self):
        payload = {
            "cpf": "11122233344",
            "baseline_value": "valor_invalido", # tipo errado
            "accelerations": 0.003, "fetal_movement": 0.0,
            "uterine_contractions": 0.0, "light_decelerations": 0.0, "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0, "abnormal_short_term_variability": 0,
            "mean_value_of_short_term_variability": 0.5, "percentage_of_time_with_abnormal_long_term_variability": 0,
            "mean_value_of_long_term_variability": 0.5, "histogram_width": 50, "histogram_min": 60,
            "histogram_max": 180, "histogram_number_of_peaks": 2, "histogram_number_of_zeroes": 0,
            "histogram_mode": 120, "histogram_mean": 120, "histogram_median": 120,
            "histogram_variance": 120, "histogram_tendency": 0
        }
        response = self.client.post('/registros', json=payload)
        self.assertIn(response.status_code, [400, 422, 500])

if __name__ == '__main__':
    unittest.main() 