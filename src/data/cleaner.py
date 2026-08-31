# ============================================================
# PHISHGUARD AI - DATA CLEANER
# ============================================================

import pandas as pd


def clean_dataset(dataframe):
    """
    Clean the PhiUSIIL phishing URL dataset.

    Operations:
    1. Copy the original DataFrame
    2. Remove completely empty rows
    3. Remove duplicate rows
    4. Remove rows with missing URL
    5. Remove rows with missing label
    6. Normalize URL values
    7. Normalize labels
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(
            "Input must be a pandas DataFrame."
        )

    df = dataframe.copy()

    print("=" * 70)
    print("PHISHGUARD AI - DATA CLEANING")
    print("=" * 70)

    print("\nOriginal shape:")
    print(df.shape)

    # --------------------------------------------------------
    # Remove completely empty rows
    # --------------------------------------------------------

    df = df.dropna(
        how="all"
    )

    # --------------------------------------------------------
    # Check required columns
    # --------------------------------------------------------

    if "URL" not in df.columns:
        raise ValueError(
            "Required column 'URL' was not found."
        )

    if "label" not in df.columns:
        raise ValueError(
            "Required column 'label' was not found."
        )

    # --------------------------------------------------------
    # Remove missing URLs and labels
    # --------------------------------------------------------

    df = df.dropna(
        subset=["URL", "label"]
    )

    # --------------------------------------------------------
    # Convert URL to string
    # --------------------------------------------------------

    df["URL"] = (
        df["URL"]
        .astype(str)
        .str.strip()
    )

    # --------------------------------------------------------
    # Remove empty URLs
    # --------------------------------------------------------

    df = df[
        df["URL"].str.len() > 0
    ]

    # --------------------------------------------------------
    # Normalize labels
    # --------------------------------------------------------

    df["label"] = pd.to_numeric(
        df["label"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["label"]
    )

    df["label"] = (
        df["label"]
        .astype(int)
    )

    # --------------------------------------------------------
    # Keep only valid binary labels
    # --------------------------------------------------------

    df = df[
        df["label"].isin([0, 1])
    ]

    # --------------------------------------------------------
    # Remove duplicate URLs
    # --------------------------------------------------------

    df = df.drop_duplicates(
        subset=["URL"]
    )

    # --------------------------------------------------------
    # Reset index
    # --------------------------------------------------------

    df = df.reset_index(
        drop=True
    )

    print("\nCleaned shape:")
    print(df.shape)

    print("\nRemaining missing values:")
    print(
        df[["URL", "label"]]
        .isnull()
        .sum()
    )

    print("\nLabel distribution:")
    print(
        df["label"]
        .value_counts()
        .sort_index()
    )

    print("\nData cleaning completed successfully. ✅")

    return df