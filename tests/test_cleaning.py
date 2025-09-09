import pandas as pd
import pytest
from data_doctor.cleaner import DataCleaner


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["Alice", "Bob", None, "Charlie"],
        "age": [25, None, 30, 22],
        "email": ["alice@test.com", "bob@test.com", "invalid_email", None]
    })


def test_drop_duplicates(sample_df):
    df = pd.concat([sample_df, sample_df.iloc[[0]]], ignore_index=True)
    cleaner = DataCleaner(df.copy()).drop_duplicates()
    df_cleaned = cleaner.get_df()
    assert df_cleaned.shape[0] == len(df) - 1
    assert "Alice" in df_cleaned["name"].values


def test_fill_missing(sample_df):
    cleaner = DataCleaner(sample_df.copy()).fill_missing(strategy="mean")
    df_filled = cleaner.get_df()
    numeric_cols = df_filled.select_dtypes(include="number").columns
    for col in numeric_cols:
        assert df_filled[col].isnull().sum() == 0
    # Non-numeric columns remain unchanged
    assert df_filled["name"].isnull().sum() == 1


def test_standardize_strings(sample_df):
    cleaner = DataCleaner(sample_df.copy()).standardize_strings()
    df_standardized = cleaner.get_df()
    string_cols = df_standardized.select_dtypes(include="object").columns
    for col in string_cols:
        # All non-null strings should be lowercase
        assert df_standardized[col].dropna().str.islower().all()
        # All strings should be stripped (no leading/trailing whitespace)
        assert (df_standardized[col].dropna() ==
                df_standardized[col].dropna().str.strip()).all()
