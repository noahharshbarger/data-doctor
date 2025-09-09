from sklearn.preprocessing import StandardScaler, OneHotEncoder

import pandas as pd

def normalize_numeric(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def encode_categorical(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = df.select_dtypes(include="object").columns
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded = encoder.fit_transform(df[cat_cols])
    df = df.drop(columns=cat_cols)
    df = pd.concat([df, pd.DataFrame(encoded, columns=encoder.get_feature_names_out(cat_cols))], axis=1)
    return df