# Machine Learning Projekt

Dieses Repository enthält ein Machine Learning Projekt, das mit Python und TensorFlow entwickelt wurde.

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Installer)

### Setup

1. Repository klonen:
   ```bash
   git clone https://github.com/YunusEA12/ML2.git
   cd ML2
   ```

2. Virtuelle Umgebung erstellen und aktivieren:

   **Windows:**
   ```bash
   python -m venv ml_env2
   ml_env2\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv ml_env2
   source ml_env2/bin/activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. Jupyter Kernel einrichten:
   ```bash
   python -m ipykernel install --user --name ml_env2 --display-name "Python (ml_env2)"
   ```

## Verwendung

1. Jupyter Notebook starten:
   ```bash
   jupyter notebook
   ```

2. Im Notebook den Kernel "Python (ml_env2)" auswählen

## Projektstruktur

## Models
1. Model 1: Basic MLPClassifier
2. Model 2: Optimized MLPClassifier
3. Model 3: Keras Implementation
4. Model 4: LeNet5 CNN

## Hardware Requirements
- Works on ARM64 architecture
- CPU only (no GPU required)