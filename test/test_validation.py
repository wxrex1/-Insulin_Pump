import unittest
from src.pump_config import PumpConfig
from src.insulin_pump import InsulinPump

class TestInsulinPumpValidation(unittest.TestCase):

    def test_invalid_carb_input(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        with self.assertRaises(TypeError):
            pump.calculate_meal_bolus("invalid")  # Entrée invalide

if __name__ == '__main__':
    unittest.main()
