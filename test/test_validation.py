import unittest
from src.pump_config import PumpConfig
from src.insulin_pump import InsulinPump

class TestInsulinPumpValidation(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        self.config = PumpConfig()
        self.pump = InsulinPump(self.config)  # Passer config à InsulinPump

    def test_invalid_carb_input(self):
        """Test d'entrée invalide pour le calcul du bolus alimentaire."""
        with self.assertRaises(TypeError):
            self.pump.calculate_meal_bolus("invalid")  # Entrée invalide

    def test_high_carb_intake(self):
        """Test pour vérifier la réponse du système à une quantité élevée de glucides."""
        carbs = 300  # Quantité de glucides élevée
        expected_bolus = carbs / self.config.insulin_to_carb_ratio
        actual_bolus = self.pump.calculate_meal_bolus(carbs)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"For {carbs}g of carbs, expected bolus {expected_bolus}, but got {actual_bolus}.")

    def test_extreme_glucose_level(self):
        """Test pour vérifier le comportement avec une glycémie très élevée."""
        current_glucose = 400  # Glycémie très élevée
        target_glucose = 100
        expected_bolus = (current_glucose - target_glucose) / self.config.insulin_sensitivity_factor
        actual_bolus = self.pump.calculate_correction_bolus(current_glucose, target_glucose)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"With high glucose {current_glucose}, expected correction bolus {expected_bolus}, but got {actual_bolus}.")

if __name__ == '__main__':
    unittest.main()
