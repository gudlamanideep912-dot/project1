# project1

# PhishGuard AI

## AI-Based Phishing URL Detection System

PhishGuard AI is a machine-learning-based cybersecurity project designed to analyze URLs and identify potentially malicious or phishing websites.

The system extracts URL-based features, uses a Random Forest classifier to predict whether a URL is phishing or legitimate, calculates a risk score, and presents the result through a graphical user interface.

---

## Features

- URL validation and security checks
- Automated URL feature extraction
- 25 URL-based features
- Random Forest machine-learning classifier
- 300 decision trees
- Phishing probability calculation
- Legitimate probability calculation
- Risk score from 0 to 100
- LOW, MEDIUM, and HIGH risk levels
- Graphical user interface
- Feature-engineering notebook
- Model evaluation
- Saved trained model

---

## Project Structure

```text
project1/
¦
+-- app.py
+-- gui.py
+-- README.md
¦
+-- data/
¦   +-- raw/
¦   +-- processed/
¦
+-- models/
¦   +-- random_forest.joblib
¦   +-- random_forest_25_features.joblib
¦   +-- feature_columns.json
¦
+-- notebooks/
¦   +-- feature_engineering.ipynb
¦   +-- final_phishguard.ipynb
¦   +-- risk_engine.ipynb
¦   +-- security_ipynb
¦
+-- src/
    +-- data/
    ¦   +-- loader.py
    ¦
    +-- features/
    ¦   +-- __init__.py
    ¦   +-- url_features.py
    ¦
    +-- security/
        +-- __init__.py
        +-- security.py
```
