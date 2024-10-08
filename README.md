# Vérifier la version de Python
python --version

# Naviguer vers le dossier du projet
cd /c/Cours/tech/5eme\ Année/Insulin_Pump

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
source venv/Scripts/activate

# Installer les dépendances
pip install -r requirements.txt

# Exécuter le simulateur
python -m src.simulator

# Exécuter les tests
python -m unittest discover -v test

----------------------------------------------------------------------------

insulin_pump_simulator/
│
├── src/                                # Dossier contenant le code source
│   ├── __init__.py                     # Fichier d'initialisation du package
│   ├── patient.py                       # Classe Patient pour gérer les données du patient
│   ├── pump_config.py                  # Configuration de la pompe à insuline
│   ├── insulin_pump.py                 # Logique de la pompe à insuline
│   ├── cgm.py                           # Gestion du moniteur de glycémie continue (CGM)
│   ├── closed_loop_controller.py        # Contrôleur de boucle fermée
│   └── simulator.py                     # Simulateur de la pompe à insuline
│
├── tests/                               # Dossier contenant les tests unitaires
│   ├── __init__.py                     # Fichier d'initialisation du package de tests
│   ├── test_patient.py                  # Tests pour la classe Patient
│   ├── test_insulin_pump.py             # Tests pour la classe InsulinPump
│   ├── test_cgm.py                      # Tests pour la classe CGM
│   ├── test_closed_loop_controller.py    # Tests pour la classe ClosedLoopController
│   └── test_simulator.py                # Tests pour le simulateur
│
├── README.md                            # Documentation du projet
└── requirements.txt                     # Liste des dépendances requises
