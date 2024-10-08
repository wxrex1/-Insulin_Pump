class Patient:
    """
    Classe représentant un patient diabétique.
    Attributs :
        initial_glucose (float): Glycémie initiale (mg/dL).
        carb_sensitivity (float): Sensibilité aux glucides (mg/dL par g).
        insulin_sensitivity (float): Sensibilité à l'insuline (mg/dL par U).
    """

    def __init__(self, initial_glucose, carb_sensitivity, insulin_sensitivity):
        self.glucose_level = initial_glucose
        self.carb_sensitivity = carb_sensitivity  # Sensibilité aux glucides
        self.insulin_sensitivity = insulin_sensitivity  # Sensibilité à l'insuline

    def update_glucose_level(self, insulin, carbs):
        """
        Met à jour la glycémie en fonction de l'insuline administrée et des glucides consommés.
        Args:
            insulin (float): Quantité d'insuline administrée (U).
            carbs (float): Quantité de glucides consommés (g).
        """
        delta_glucose_carbs = carbs * self.carb_sensitivity
        delta_glucose_insulin = insulin * self.insulin_sensitivity
        self.glucose_level += delta_glucose_carbs - delta_glucose_insulin

    def add_carbs(self, carbs):
        """
        Ajoute des glucides consommés pour simuler un repas.
        Args:
            carbs (float): Quantité de glucides consommés (g).
        """
        self.update_glucose_level(0, carbs)
