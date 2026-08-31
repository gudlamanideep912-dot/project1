# ============================================================
# PHISHGUARD AI - MAIN APPLICATION
# ============================================================

from pathlib import Path
import sys
import json
import joblib
import pandas as pd

# ------------------------------------------------------------
# Project setup
# ------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ------------------------------------------------------------
# Import project modules
# ------------------------------------------------------------

from src.features.url_features import extract_url_features
from src.security.security import security_check


# ------------------------------------------------------------
# Paths
# ------------------------------------------------------------

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "random_forest_25_features.joblib"
)

FEATURE_COLUMNS_PATH = (
    PROJECT_ROOT
    / "models"
    / "feature_columns.json"
)


# ------------------------------------------------------------
# Load model
# ------------------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found:\n{MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)


# ------------------------------------------------------------
# Load feature columns
# ------------------------------------------------------------

if not FEATURE_COLUMNS_PATH.exists():
    raise FileNotFoundError(
        f"Feature column file not found:\n"
        f"{FEATURE_COLUMNS_PATH}"
    )

with open(
    FEATURE_COLUMNS_PATH,
    "r",
    encoding="utf-8"
) as file:

    FEATURE_COLUMNS = json.load(file)


# ------------------------------------------------------------
# Verify model compatibility
# ------------------------------------------------------------

if model.n_features_in_ != len(FEATURE_COLUMNS):
    raise RuntimeError(
        "Model and feature-column count do not match.\n"
        f"Model expects: {model.n_features_in_}\n"
        f"Features available: {len(FEATURE_COLUMNS)}"
    )


# ------------------------------------------------------------
# Prediction function
# ------------------------------------------------------------

def predict_url(url):

    # Security check
    security_result = security_check(url)

    if not security_result["safe_to_analyze"]:

        return {
            "success": False,
            "url": url,
            "message": security_result["message"]
        }

    # Extract features
    features = extract_url_features(url)

    feature_df = pd.DataFrame(
        [features]
    )

    # Check missing features
    missing_features = [
        feature
        for feature in FEATURE_COLUMNS
        if feature not in feature_df.columns
    ]

    if missing_features:

        return {
            "success": False,
            "url": url,
            "message": (
                "Missing features: "
                + ", ".join(missing_features)
            )
        }

    # Keep exact training order
    feature_df = feature_df[
        FEATURE_COLUMNS
    ]

    # Prediction
    prediction = model.predict(
        feature_df
    )[0]

    probabilities = model.predict_proba(
        feature_df
    )[0]

    classes = list(model.classes_)

    phishing_probability = 0.0
    legitimate_probability = 0.0

    for class_value, probability in zip(
        classes,
        probabilities
    ):

        if int(class_value) == 1:
            phishing_probability = float(
                probability
            )
        else:
            legitimate_probability = float(
                probability
            )

    # Result
    if int(prediction) == 1:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    # Risk score
    risk_score = round(
        phishing_probability * 100,
        2
    )

    if risk_score >= 75:
        risk_level = "HIGH"

    elif risk_score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "success": True,
        "url": url,
        "result": result,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "phishing_probability":
            phishing_probability,
        "legitimate_probability":
            legitimate_probability,
        "features": features
    }


# ------------------------------------------------------------
# Command-line application
# ------------------------------------------------------------

def main():

    print("=" * 70)
    print("PHISHGUARD AI")
    print("AI-Based Phishing URL Detection")
    print("=" * 70)

    url = input(
        "\nEnter a URL to analyze: "
    ).strip()

    if not url:

        print(
            "\nError: URL cannot be empty."
        )

        return

    result = predict_url(url)

    print("\n" + "=" * 70)
    print("ANALYSIS RESULT")
    print("=" * 70)

    if not result["success"]:

        print("\nStatus: FAILED")
        print(
            "\nReason:",
            result["message"]
        )

        return

    print("\nURL:")
    print(result["url"])

    print("\nPrediction:")
    print(result["result"])

    print("\nRisk Score:")
    print(
        f"{result['risk_score']}/100"
    )

    print("\nRisk Level:")
    print(result["risk_level"])

    print("\nPhishing Probability:")
    print(
        f"{result['phishing_probability'] * 100:.2f}%"
    )

    print("\nLegitimate Probability:")
    print(
        f"{result['legitimate_probability'] * 100:.2f}%"
    )

    print("\n" + "=" * 70)
    print("Analysis completed successfully. ✅")
    print("=" * 70)


# ------------------------------------------------------------
# Run application
# ------------------------------------------------------------

if __name__ == "__main__":
    main()