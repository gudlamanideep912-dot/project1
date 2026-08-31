from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "PhiUSIIL_Phishing_URL_Dataset.csv"
)


def load_raw_dataset():

    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{RAW_DATA_PATH}"
        )

    dataframe = pd.read_csv(
        RAW_DATA_PATH,
        low_memory=False
    )

    if dataframe.empty:
        raise ValueError(
            "Dataset is empty."
        )

    return dataframe


def dataset_info(dataframe):

    print("=" * 70)
    print("PHISHGUARD AI - DATASET INFORMATION")
    print("=" * 70)

    print("\nDataset shape:")
    print(dataframe.shape)

    print("\nColumn names:")

    for column in dataframe.columns:
        print(column)

    print("\nMissing values:")

    print(dataframe.isnull().sum())

    print("\nDuplicate rows:")

    print(dataframe.duplicated().sum())

    print("\nFirst 5 rows:")

    print(dataframe.head())