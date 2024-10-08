class CGM:
    """
    Classe représentant un capteur de glycémie en continu.
    Attributs :
        measurement_interval (int): Intervalle de mesure (minutes).
    """

    def __init__(self, measurement_interval):
        self.measurement_interval = measurement_interval

    def measure_glucose(self, patient):
        return patient.glucose_level
