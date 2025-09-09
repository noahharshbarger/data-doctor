import pandas as pandas

def drop_duplicates(df: pd.Dataframe) -> pd.DataFrame:
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()

def fill_missing(df: pd.DataFrame, value) -> pd.DataFrame:
    for col in df.select_dtypes(include="number"):
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
    return df

def standardize_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip().str.lower()
    return df