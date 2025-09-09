import pandas as pd
import pytest
from data_doctor.cleaner import DataCleaner


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": [" Alice ", "BOB", None],
        "age": [25, None, 30]
    })


def test_drop_duplicates(sample_df):
    df = pd.concat([sample_df, sample_df.iloc[[0]]], ignore_index=True)
    cleaner = DataCleaner(df.copy())
    df_cleaned = cleaner.drop_duplicates().get_df()
    assert df_cleaned.shape[0] == len(df) - 1


def test_fill_missing(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    df_filled = cleaner.fill_missing(strategy="mean").get_df()
    assert df_filled["age"].isnull().sum() == 0


def test_standardize_strings(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    df_standardized = cleaner.standardize_strings().get_df()
    assert df_standardized["name"].dropna().str.islower().all()
