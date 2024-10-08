import unittest
from src.pump_config import PumpConfig
from src.insulin_pump import InsulinPump
from src.patient import Patient
from src.cgm import CGM
from src.closed_loop_controller import ClosedLoopController
from src.simulator import Simulator

class TestInsulinPumpSimulator(unittest.TestCase):

    def test_basal_delivery(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        for hour in range(24):
            expected_basal = config.basal_rates[hour]
            actual_basal = pump.deliver_basal(hour)
            self.assertEqual(actual_basal, expected_basal, f"Hour {hour}: Expected basal delivery {expected_basal}, but got {actual_basal}.")

    def test_meal_bolus(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        carbs = 50  # Exemple de glucides
        expected_bolus = carbs / config.insulin_to_carb_ratio
        actual_bolus = pump.calculate_meal_bolus(carbs)
        self.assertEqual(actual_bolus, expected_bolus, f"For {carbs}g of carbs, expected bolus {expected_bolus}, but got {actual_bolus}.")

    def test_correction_bolus(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        current_glucose = 180  # Glycémie actuelle
        target_glucose = 120  # Glycémie cible
        expected_bolus = (current_glucose - target_glucose) / config.insulin_sensitivity_factor
        actual_bolus = pump.calculate_correction_bolus(current_glucose, target_glucose)
        self.assertEqual(actual_bolus, expected_bolus, f"Current glucose {current_glucose} with target {target_glucose}: expected correction bolus {expected_bolus}, but got {actual_bolus}.")

    def test_update_glucose_level(self):
        patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
        patient.update_glucose_level(insulin=2, carbs=60)  # Administration d'insuline et glucides
        expected_glucose = 120 + (60 * 5) - (2 * 2)  # Calcul de la glycémie attendue
        self.assertEqual(patient.glucose_level, expected_glucose, f"After insulin and carb intake, expected glucose level {expected_glucose}, but got {patient.glucose_level}.")

    def test_simulation(self):
        config = PumpConfig()
        patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
        pump = InsulinPump(config)
        cgm = CGM(measurement_interval=5)
        controller = ClosedLoopController(target_glucose=100, pump=pump, cgm=cgm)
        
        simulator = Simulator(patient, pump, cgm, controller, duration=24)
        simulator.run_simulation()

        self.assertLess(patient.glucose_level, 120, f"After 24 hours of simulation, expected glucose level to be less than 120, but got {patient.glucose_level}.")

    def test_meal_bolus_zero_carb(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        carbs = 0
        expected_bolus = 0  # 0g de glucides devrait donner 0U d'insuline
        actual_bolus = pump.calculate_meal_bolus(carbs)
        self.assertEqual(actual_bolus, expected_bolus, f"Expected bolus for 0g of carbs to be {expected_bolus}, but got {actual_bolus}.")

    def test_correction_bolus_at_target(self):
        config = PumpConfig()
        pump = InsulinPump(config)
        current_glucose = 100  # Glycémie à la cible
        target_glucose = 100   # Cible égale à la glycémie actuelle
        expected_bolus = 0  # Aucune insuline nécessaire
        actual_bolus = pump.calculate_correction_bolus(current_glucose, target_glucose)
        self.assertEqual(actual_bolus, expected_bolus, f"Expected correction bolus for target glucose to be {expected_bolus}, but got {actual_bolus}.")

if __name__ == '__main__':
    unittest.main()
