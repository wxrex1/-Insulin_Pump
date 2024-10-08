import unittest
from src.pump_config import PumpConfig
from src.insulin_pump import InsulinPump
from src.patient import Patient
from src.cgm import CGM
from src.closed_loop_controller import ClosedLoopController
from src.simulator import Simulator

class TestInsulinPumpSimulator(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        self.config = PumpConfig()
        self.pump = InsulinPump(self.config)  # Passer config à InsulinPump
        self.patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
        self.cgm = CGM(measurement_interval=5)
        self.controller = ClosedLoopController(target_glucose=100, pump=self.pump, cgm=self.cgm)

    def test_basal_delivery(self):
        """Test de l'administration basale d'insuline pour chaque heure."""
        for hour in range(24):
            expected_basal = self.config.basal_rates[hour]
            actual_basal = self.pump.deliver_basal(hour)
            self.assertEqual(actual_basal, expected_basal,
                             f"Hour {hour}: Expected basal delivery {expected_basal}, but got {actual_basal}.")

    def test_meal_bolus(self):
        """Test du calcul du bolus alimentaire pour 50g de glucides."""
        carbs = 50
        expected_bolus = carbs / self.config.insulin_to_carb_ratio
        actual_bolus = self.pump.calculate_meal_bolus(carbs)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"For {carbs}g of carbs, expected bolus {expected_bolus}, but got {actual_bolus}.")

    def test_correction_bolus(self):
        """Test du calcul du bolus de correction pour une glycémie actuelle de 180."""
        current_glucose = 180
        target_glucose = 120
        expected_bolus = (current_glucose - target_glucose) / self.config.insulin_sensitivity_factor
        actual_bolus = self.pump.calculate_correction_bolus(current_glucose, target_glucose)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"Current glucose {current_glucose} with target {target_glucose}: expected correction bolus {expected_bolus}, but got {actual_bolus}.")

    def test_update_glucose_level(self):
        """Test de la mise à jour de la glycémie après administration d'insuline et consommation de glucides."""
        self.patient.update_glucose_level(insulin=2, carbs=60)
        expected_glucose = 120 + (60 * 5) - (2 * 2)
        self.assertEqual(self.patient.glucose_level, expected_glucose,
                         f"After insulin and carb intake, expected glucose level {expected_glucose}, but got {self.patient.glucose_level}.")

    def test_simulation(self):
        """Test de la simulation sur 24 heures pour vérifier la diminution de la glycémie."""
        simulator = Simulator(self.patient, self.pump, self.cgm, self.controller, duration=24)
        simulator.run_simulation()
        self.assertLess(self.patient.glucose_level, 120,
                        f"After 24 hours of simulation, expected glucose level to be less than 120, but got {self.patient.glucose_level}.")

    def test_meal_bolus_zero_carb(self):
        """Test pour vérifier que le bolus pour 0g de glucides est 0."""
        carbs = 0
        expected_bolus = 0
        actual_bolus = self.pump.calculate_meal_bolus(carbs)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"Expected bolus for 0g of carbs to be {expected_bolus}, but got {actual_bolus}.")

    def test_correction_bolus_at_target(self):
        """Test pour vérifier que le bolus de correction est 0 lorsque la glycémie est à la cible."""
        current_glucose = 100
        target_glucose = 100
        expected_bolus = 0
        actual_bolus = self.pump.calculate_correction_bolus(current_glucose, target_glucose)
        self.assertEqual(actual_bolus, expected_bolus,
                         f"Expected correction bolus for target glucose to be {expected_bolus}, but got {actual_bolus}.")

    def test_stop_pump_on_high_glucose(self):
        """Test pour vérifier que la pompe s'arrête si la glycémie dépasse un seuil critique."""
        high_glucose_level = 350  # Glycémie critique
        self.pump.check_glucose_and_stop(high_glucose_level)  # Appel de la méthode pour vérifier la glycémie
        self.assertFalse(self.pump.is_running(),
                         f"Expected pump to be stopped due to high glucose level {high_glucose_level}, but it is still running.")

if __name__ == '__main__':
    unittest.main()
