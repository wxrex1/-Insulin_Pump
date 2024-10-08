import unittest
from src.pump_config import PumpConfig
from src.insulin_pump import InsulinPump

class TestInsulinPump(unittest.TestCase):
    def test_meal_bolus(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        self.assertEqual(pump.calculate_meal_bolus(60), 6)  # 60g de glucides avec un ICR de 10 => 6U d'insuline

    def test_correction_bolus(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        self.assertEqual(pump.calculate_correction_bolus(180, 120), 2)  # Glycémie de 180, cible de 120, ISF de 30 => 2U d'insuline

if __name__ == '__main__':
    unittest.main()
