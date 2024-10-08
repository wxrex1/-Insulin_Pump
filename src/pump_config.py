class PumpConfig:
    """
    Classe représentant la configuration de la pompe à insuline.
    Attributs :
        basal_rates (list[float]): Liste des taux basaux par heure (U/h).
        insulin_to_carb_ratio (float): Ratio insuline/glucides (ICR) (U/g).
        insulin_sensitivity_factor (float): Facteur de sensibilité à l'insuline (ISF) (mg/dL par U).
        max_bolus (float): Dose maximale autorisée pour les bolus (U).
    """

    def __init__(self, basal_rates, insulin_to_carb_ratio, insulin_sensitivity_factor, max_bolus):
        self.basal_rates = basal_rates
        self.insulin_to_carb_ratio = insulin_to_carb_ratio
        self.insulin_sensitivity_factor = insulin_sensitivity_factor
        self.max_bolus = max_bolus

    def validate(self):
        """
        Valide la configuration de la pompe pour s'assurer que les valeurs sont dans les plages acceptables.
        Returns:
            bool: True si la configuration est valide, False sinon.
        """
        return True