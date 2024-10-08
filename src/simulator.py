from .pump_config import PumpConfig
from .patient import Patient
from .insulin_pump import InsulinPump
from .cgm import CGM
from .closed_loop_controller import ClosedLoopController

class Simulator:
    """
    Classe principale pour orchestrer la simulation.
    Attributs :
        patient (Patient): Instance de la classe Patient.
        pump (InsulinPump): Instance de la classe InsulinPump.
        cgm (CGM): Instance de la classe CGM.
        controller (ClosedLoopController): Instance de la classe ClosedLoopController.
        duration (int): Durée de la simulation (en heures).
    """

    def __init__(self, patient, pump, cgm, controller, duration):
        self.patient = patient
        self.pump = pump
        self.cgm = cgm
        self.controller = controller
        self.duration = duration

    def run_simulation(self):
        for hour in range(self.duration):
            # Administrer l'insuline basale
            basal_insulin = self.pump.deliver_basal(hour)
            self.patient.update_glucose_level(basal_insulin, 0)

            # Mesurer la glycémie
            glucose = self.cgm.measure_glucose(self.patient)
            print(f"Hour {hour}: Glucose level: {glucose:.2f} mg/dL")

            # Ajuster la délivrance basale en fonction de la boucle fermée
            correction_insulin = self.controller.adjust_basal_rate(glucose)
            self.patient.update_glucose_level(correction_insulin, 0)

        print("Simulation terminée")

if __name__ == "__main__":
    config = PumpConfig()
    
    # Initialisation du patient avec des valeurs spécifiques
    patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
    pump = InsulinPump(config)
    cgm = CGM(measurement_interval=5)
    controller = ClosedLoopController(target_glucose=100, pump=pump, cgm=cgm)

    simulator = Simulator(patient, pump, cgm, controller, duration=24)  # Simulation de 24 heures
    simulator.run_simulation()
