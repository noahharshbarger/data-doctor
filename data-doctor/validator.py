def check_missing(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_types(df):
    return df.dtypes.to_dict()