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
            basal_insulin = self.pump.deliver_basal(hour)
            self.patient.update_glucose_level(basal_insulin, 0)

            glucose = self.cgm.measure_glucose(self.patient)
            print(f"Hour {hour}: Glucose level: {glucose} mg/dL")

            correction_insulin = self.controller.adjust_basal_rate(glucose)
            self.patient.update_glucose_level(correction_insulin, 0)

        print("Simulation terminée")

if __name__ == "__main__":
    from pump_config import PumpConfig
    config = PumpConfig(
        basal_rates=[0.8]*24,
        insulin_to_carb_ratio=10,
        insulin_sensitivity_factor=30,
        max_bolus=10
    )

    patient = Patient(initial_glucose=120, carb_sensitivity=5, insulin_sensitivity=2)
    pump = InsulinPump(config)
    cgm = CGM(measurement_interval=5)
    controller = ClosedLoopController(target_glucose=100, pump=pump, cgm=cgm)

    simulator = Simulator(patient, pump, cgm, controller, duration=24)
    simulator.run_simulation()
