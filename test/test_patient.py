import unittest
from src.patient import Patient

class TestPatient(unittest.TestCase):
    def test_update_glucose_level(self):
        patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
        patient.update_glucose_level(insulin=2, carbs=60)  # 60g de glucides
        self.assertAlmostEqual(patient.glucose_level, 120 + 60 * 5 - 2 * 2)

if __name__ == '__main__':
    unittest.main()
