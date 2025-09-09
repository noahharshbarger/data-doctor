from data_doctor import cleaner, validator, transformer

class DataPipeline:
    def __init__(self, df):
        self.df = df

    def run_basic_cleaning(self):
        self.df = cleaner.drop_duplicates(self.df)
        self.df = cleaner.fill_missing(self.df, strategy="mean")
        self.df = cleaner.standardize_strings(self.df)
        return self.df

    def run_transformations(self):
        self.df = transformer.normalize_numeric(self.df)
        self.df = transformer.encode_categorical(self.df)
        return self.df
    
    def validate(self):
        return {
            "missing": validator.check_missing(self.df),
            "duplicates": validator.check_duplicates(self.df),
            "types": validator.check_types(self.df)
        }