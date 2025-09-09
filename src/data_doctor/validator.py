import pandas as pd
import re

def check_missing(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_types(df):
    return df.dtypes.to_dict()

def validate_email(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Validate email addresses in the specified column."""
    email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    df[column] = df[column].apply(lambda x: x if pd.isna(x) or re.match(email_pattern, str(x)) else None)
    return df