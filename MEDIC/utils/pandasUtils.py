import pandas as pd


def convert_encoding(df: pd.DataFrame, to: str):
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].str.encode('utf-8').str.decode(to)

    return df


def apply_function(func, df: pd.DataFrame, fromColumn: str, toColumn: str, drop: bool = True):
    region_map = pd.DataFrame(df[fromColumn].unique(), columns=[fromColumn])
    region_map[toColumn] = region_map[fromColumn].apply(func)
    df = df.merge(region_map, on=fromColumn, how='outer')

    if drop:
        df = df.drop(fromColumn, axis=1)
        return df[[toColumn] + list(df.columns[:-1])]

    return df[[toColumn] + list(df.columns[:-1])]
