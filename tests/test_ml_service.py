import unittest
from ml_service import ModelPredictor

class TestModelPredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = ModelPredictor()

    def test_inference(self):
        sample = [120, 0.003, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.5, 0, 0.5, 50, 60, 180, 2, 0, 120, 120, 120, 0]
        result = self.predictor.inference(sample)
        self.assertIn(result, [1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            self.predictor.inference([None]*20)

if __name__ == '__main__':
    unittest.main() 