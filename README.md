# PhishGuard AI: AI-Powered Phishing URL Detection
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/gudlamanideep912-dot/project1)

PhishGuard AI is a cybersecurity tool that leverages machine learning to detect phishing websites by analyzing their URLs. The system extracts a comprehensive set of lexical features from a URL and uses a pre-trained Random Forest model to classify it as either 'phishing' or 'legitimate'. It provides a clear prediction, a calculated risk score, and a risk level to help users assess the safety of a web link.

The entire data science workflow, including data cleaning, feature engineering, model training (Random Forest and a comparative ANN), and evaluation, is documented in the `notebooks` directory.

## Features
- **URL Feature Extraction:** Analyzes URLs to extract 25 distinct lexical features, including URL length, hostname entropy, and counts of special characters.
- **Machine Learning Model:** Utilizes a Random Forest classifier trained on a large dataset of phishing and legitimate URLs.
- **Risk Assessment:** Converts the model's prediction probability into an intuitive risk score (0-100) and a qualitative risk level (LOW, MEDIUM, HIGH).
- **Dual Interfaces:** Offers both a user-friendly Graphical User Interface (GUI) built with Tkinter and a Command-Line Interface (CLI) for flexible usage.
- **Input Validation:** Includes a security module to validate and sanitize URLs before analysis, ensuring robust and safe processing.

## How It Works
The application follows a simple yet effective pipeline for URL analysis:
1.  **Input:** A user provides a URL through the GUI or CLI.
2.  **Security Check:** The URL is validated to ensure it is well-formed (HTTP/HTTPS) and does not contain malicious patterns before processing.
3.  **Feature Extraction:** The system extracts 25 lexical features from the sanitized URL. These features are the same ones used to train the detection model.
4.  **Prediction:** The feature set is passed to the trained Random Forest model, which predicts the probability of the URL being a phishing attempt.
5.  **Risk Assessment:** The phishing probability is converted into a 0-100 risk score and categorized into LOW, MEDIUM, or HIGH risk levels.
6.  **Output:** The final prediction, risk score, and probabilities are presented to the user.

## Project Structure
```
.
├── app.py                      # Main application logic & CLI
├── gui.py                      # Tkinter GUI application
├── requirements.txt            # Project dependencies
├── models/
│   ├── random_forest_25_features.joblib # Trained Random Forest model
│   └── feature_columns.json    # List of feature names in the correct order
├── notebooks/                  # Jupyter notebooks for data analysis and modeling
│   ├── data_cleaning.ipynb
│   ├── feature_engineering.ipynb
│   ├── random_forest.ipynb
│   ├── ann_pytorch.ipynb
│   └── model_comparison.ipynb
└── src/
    ├── data/                   # Modules for data loading and cleaning
    │   ├── cleaner.py
    │   └── loader.py
    ├── features/               # Module for URL feature extraction
    │   └── url_features.py
    └── security/               # Module for URL validation and security checks
        └── security.py
```

## Installation
To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gudlamanideep912-dot/project1.git
    cd project1
    ```

2.  **Install dependencies:**
    It is recommended to create a virtual environment first.
    ```bash
    pip install -r requirements.txt
    ```

## Usage
You can run the application using either the Graphical User Interface or the Command-Line Interface.

### Graphical User Interface (GUI)
To launch the GUI, run the `gui.py` script:
```bash
python gui.py
```
Enter a URL into the input field and click **"Analyze URL"** to see the prediction and risk score.

### Command-Line Interface (CLI)
To use the CLI, run the `app.py` script:
```bash
python app.py
```
The application will prompt you to enter a URL, and the analysis results will be printed directly to the console.

## Model & Performance
The primary detection model is a Random Forest classifier, chosen for its high performance in identifying phishing URLs.

-   **Model:** Random Forest Classifier (`n_estimators=300`)
-   **Features:** 25 lexical URL-based features
-   **Performance Highlights:**
    -   **Accuracy:** 99.50%
    -   **Phishing Recall:** 99.15% (Correctly identifies 99.15% of all phishing URLs)
    -   **ROC-AUC:** 0.9968

*Metrics are based on the held-out test set, as detailed in the `model_comparison.ipynb` and `random_forest.ipynb` notebooks.*
## interface
<img width="870" height="676" alt="image" src="https://github.com/user-attachments/assets/908f10bf-35fb-40fc-b07c-ea654979bf0b" />
## if the url is safe
<img width="870" height="680" alt="image" src="https://github.com/user-attachments/assets/9f3c3a52-f07d-4d8e-860e-93e386d69d9e" />
## if the url is not safe
<img width="867" height="680" alt="Screenshot 2026-09-01 221950" src="https://github.com/user-attachments/assets/8f732d6f-a637-44b6-a9d0-81f897ab90cb" />
### error
<img width="867" height="683" alt="Screenshot 2026-09-01 221338" src="https://github.com/user-attachments/assets/f2e769e1-6e2b-4658-9e60-a6a5418cfbca" />




