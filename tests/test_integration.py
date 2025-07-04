import unittest
from backend import app, init_db
import sqlite3

class TestIntegration(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_full_flow(self):
        payload = {
            "cpf": "98765432100",
            "baseline_value": 130, "accelerations": 0.004, "fetal_movement": 0.1,
            "uterine_contractions": 0.1, "light_decelerations": 0.0, "severe_decelerations": 0.0,
            "prolongued_decelerations": 0.0, "abnormal_short_term_variability": 1,
            "mean_value_of_short_term_variability": 0.6, "percentage_of_time_with_abnormal_long_term_variability": 1,
            "mean_value_of_long_term_variability": 0.6, "histogram_width": 55, "histogram_min": 65,
            "histogram_max": 185, "histogram_number_of_peaks": 3, "histogram_number_of_zeroes": 1,
            "histogram_mode": 130, "histogram_mean": 130, "histogram_median": 130,
            "histogram_variance": 130, "histogram_tendency": 1
        }
        response = self.client.post('/registros', json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('fetalhealth', data)
        # Verifica se o registro foi salvo no banco
        conn = sqlite3.connect('registros.db')
        c = conn.cursor()
        c.execute('SELECT * FROM registros WHERE cpf=?', (payload['cpf'],))
        rows = c.fetchall()
        conn.close()
        self.assertTrue(len(rows) > 0)

    def test_multiple_registros(self):
        cpfs = ["11111111111", "22222222222", "33333333333"]
        for cpf in cpfs:
            payload = {
                "cpf": cpf,
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
        # Recupera todos
        response = self.client.get('/registros')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        cpfs_in_db = [str(row[1]) for row in data]
        for cpf in cpfs:
            self.assertIn(cpf, cpfs_in_db)

if __name__ == '__main__':
    unittest.main() 