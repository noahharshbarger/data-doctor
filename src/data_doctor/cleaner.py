import pandas as pd
from data_doctor.validator import validate_email

class DataCleaner():
    def __init__(self, df):
        self.df = df

    def drop_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        self.df = self.df.drop_duplicates()
        return self.df

    def fill_missing(self, strategy="mean"):
        """Fill missing values in the DataFrame with a specified value or strategy."""
        for col in self.df.select_dtypes(include="number"):
            if strategy == "mean":
                self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif strategy == "median":
                self.df[col].fillna(self.df[col].median(), inplace=True)
        return self.df

    def standardize_strings(self):
        """Trim and lowercase all string column."""
        for col in self.df.select_dtypes(include="object"):
            self.df[col] = self.df[col].str.strip().str.lower()
        return self.df

    def run_email_validation(self, column):
        """Validate email addresses in the specified column."""
        self.df = validate_email(self.df, column)
        return self.df