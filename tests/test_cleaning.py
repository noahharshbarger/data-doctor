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
    # duplicate row for testing
    df = pd.concat([sample_df, sample_df.iloc[[0]]], ignore_index=True)
    cleaner = DataCleaner(df.copy())
    df_cleaned = cleaner.drop_duplicates()
    assert df_cleaned.shape[0] == len(df) - 1  # one duplicate removed

def test_fill_missing(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    df_filled = cleaner.fill_missing(strategy="mean")
    # age column should have no nulls
    assert df_filled["age"].isnull().sum() == 0
    # name column remains with None (strings are not filled in current version)
    assert df_filled["name"].isnull().sum() == 1

def test_standardize_strings(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    df_standardized = cleaner.standardize_strings()
    # all string columns should be lowercase and stripped
    assert df_standardized["name"].dropna().str.islower().all()
    assert df_standardized["email"].dropna().str.islower().all()