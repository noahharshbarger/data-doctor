import pandas as pd
import pytest
from data_doctor.cleaner import DataCleaner

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["Alice", "Bob", None, "Charlie", "Alice"],
        "age": [25, None, 30, 22, 25],
        "email": ["alice@test.com", "bob@test.com", "invalid_email", None, "alice@test.com"]
    })

def test_full_pipeline(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    
    # Drop duplicates
    df = cleaner.drop_duplicates()
    assert df.shape[0] == 4  # one duplicate removed

    # Fill missing values
    df = cleaner.fill_missing(strategy="mean")
    assert df["age"].isnull().sum() == 0

    # Standardize strings
    df = cleaner.standardize_strings()
    assert df["name"].str.islower().dropna().all()
    assert df["email"].str.islower().dropna().all()
