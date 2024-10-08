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
        self.carb_sensitivity = carb_sensitivity
        self.insulin_sensitivity = insulin_sensitivity

    def update_glucose_level(self, insulin, carbs):
        delta_glucose_carbs = carbs * self.carb_sensitivity
        delta_glucose_insulin = insulin * self.insulin_sensitivity
        self.glucose_level += delta_glucose_carbs - delta_glucose_insulin

    def add_carbs(self, carbs):
        self.update_glucose_level(0, carbs)
