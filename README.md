insulin_pump_simulator/
│
├── src/
│   ├── __init__.py
│   ├── pump_config.py
│   ├── insulin_pump.py
│   ├── patient.py
│   ├── cgm.py
│   ├── closed_loop_controller.py
│   └── simulator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_insulin_pump.py
│   └── test_patient.py
│
├── README.md
└── requirements.txt


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
