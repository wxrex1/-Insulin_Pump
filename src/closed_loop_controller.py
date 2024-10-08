from .insulin_pump import InsulinPump
from .cgm import CGM

class ClosedLoopController:
    """
    Classe représentant un contrôleur en boucle fermée qui ajuste l'insuline en fonction des données du capteur de glycémie.
    Attributs :
        target_glucose (float): Glycémie cible (mg/dL).
        pump (InsulinPump): Instance de la classe InsulinPump.
        cgm (CGM): Instance de la classe CGM.
    """

    def __init__(self, target_glucose, pump, cgm):
        self.target_glucose = target_glucose
        self.pump = pump
        self.cgm = cgm

    def adjust_basal_rate(self, current_glucose):
        if current_glucose > self.target_glucose:
            return self.pump.calculate_correction_bolus(current_glucose, self.target_glucose)
        return 0
