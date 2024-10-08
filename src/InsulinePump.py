class InsulinPump:
    def __init__(self, config):
        self.config = config
        self.running = True  # Indicateur d'état de la pompe

    def stop(self):
        """Arrête la pompe."""
        self.running = False

    def is_running(self):
        """Vérifie si la pompe est en marche."""
        return self.running

    def check_glucose_and_stop(self, glucose_level):
        """Vérifie le niveau de glucose et arrête la pompe si nécessaire."""
        if glucose_level > 300:  # Seuil critique
            self.stop()

    
