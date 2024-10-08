class PumpConfig:
    """
    Classe représentant la configuration de la pompe à insuline.
    Attributs :
        basal_rates (list[float]): Liste des taux basaux par heure (U/h).
        insulin_to_carb_ratio (float): Ratio insuline/glucides (ICR) (U/g).
        insulin_sensitivity_factor (float): Facteur de sensibilité à l'insuline (ISF) (mg/dL par U).
        max_bolus (float): Dose maximale autorisée pour les bolus (U).
    """

    def __init__(self, basal_rates=None, insulin_to_carb_ratio=10, insulin_sensitivity_factor=30, max_bolus=10):
        if basal_rates is None:
            basal_rates = [
                0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9,
                0.8, 0.7, 0.6, 0.6, 0.5, 0.4, 0.5,
                0.7, 0.8, 1.1, 1.0, 0.9, 0.8, 0.6,
                0.5, 0.4, 0.3
            ]
        self.basal_rates = basal_rates
        self.insulin_to_carb_ratio = insulin_to_carb_ratio
        self.insulin_sensitivity_factor = insulin_sensitivity_factor
        self.max_bolus = max_bolus
