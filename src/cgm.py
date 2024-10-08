class CGM:
    """
    Classe représentant un capteur de glycémie en continu.
    Attributs :
        measurement_interval (int): Intervalle de mesure (minutes).
    """

    def __init__(self, measurement_interval):
        self.measurement_interval = measurement_interval

    def measure_glucose(self, patient):
        """
        Mesure la glycémie actuelle du patient.
        Args:
            patient (Patient): Instance de la classe Patient.
        Returns:
            float: Glycémie actuelle (mg/dL).
        """
        return patient.glucose_level
