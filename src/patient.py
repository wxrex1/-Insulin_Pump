from .pump_config import PumpConfig

class InsulinPump:
    """
    Classe représentant la pompe à insuline.
    Attributs :
        config (PumpConfig): Configuration de la pompe à insuline.
    """

    def __init__(self, config):
        self.config = config

    def deliver_basal(self, hour):
        return self.config.basal_rates[hour]

    def calculate_meal_bolus(self, carbs):
        return carbs / self.config.insulin_to_carb_ratio

    def calculate_correction_bolus(self, current_glucose, target_glucose):
        delta_glucose = current_glucose - target_glucose
        return delta_glucose / self.config.insulin_sensitivity_factor

    def apply_configuration(self, config):
        self.config = config
