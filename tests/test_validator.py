import pandas as pd
import pytest
from data_doctor.cleaner import DataCleaner


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "email": ["alice@test.com", "invalid_email", None]
    })


def test_validate_email(sample_df):
    cleaner = DataCleaner(sample_df.copy())
    df_valid = cleaner.run_email_validation("email").get_df()
    assert "invalid_email" not in df_valid["email"].values
    assert pd.isnull(df_valid.loc[2, "email"])
