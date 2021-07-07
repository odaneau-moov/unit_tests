from typing import Dict, List, Optional

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Pandas show all cols and rows
pd.set_option("display.max_rows", 100, "display.max_columns", None)


class ColumnMissingError(Exception):
    pass


COLUMNS = [
    "ID",
    "name",
    "category",
    "main_category",
    "currency",
    "deadline",
    "goal",
    "launched",
    "pledged",
    "state",
    "backers",
    "country",
    "usd pledged",
]

DATE_COLUMNS = ["deadline", "launched"]

COLUMN_TYPES = {
    "ID": "int64",
    "goal": "int64",
    "pledged": "float64",
    "backers": "int64",
    "usd pledged": "float64",
}

RENAMED_COLUMNS = {"ID": "id", "usd pledged": "usd_pledged"}


def read_dataframe(
    file_path: str, columns: Optional[List[str]] = None, encoding: str = None
) -> pd.DataFrame:
    """
    Read the Kickstarter Projects dataset and exclude broken rows
    :param file_path: The local path to the dataset
    :param columns: List of columns to read from file
    :param encoding: The file character encoding
    :return: a dataframe
    """
    header = "infer"
    if columns:
        header = 0

    return pd.read_csv(
        filepath_or_buffer=file_path,
        sep=";",
        names=columns,
        index_col=False,
        header=header,
        encoding=encoding,
        on_bad_lines="warn",
    )


def parse_date_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Parse dates from columns
    :param df: A dataframe with columns to parse
    :param columns: A list of columns to parse
    :return: A dataframe with date-parsed columns
    """
    if not set(columns).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    for column in columns:
        df[column] = pd.to_datetime(df[column], errors="coerce").dt.date
    return df


def scale_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Scale columns to be between zero and one
    :param df: A dataframe with columns to scale
    :param columns: A list of columns to scale
    :return: A dataframe with scaled columns
    """
    if not set(columns).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df


def label_encode_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Encode target labels with value between 0 and N categories -1
    :param df: A dataframe with columns to encode
    :param columns: A list of columns to label-encode
    :return: A dataframe with encoded columns
    """
    if not set(columns).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    encoder = LabelEncoder()
    df[columns].apply(encoder.fit_transform)
    return df


def cast_columns_astype(df, columns_types: Dict[str, str]) -> pd.DataFrame:
    """
    Cast specified columns as types
    :param df: A dataframe with columns to change types
    :param columns_types: a Dict containing column names and their new types
    :return: A dataframe with proper types
    """
    if not set(columns_types.keys()).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    df = df.astype(columns_types)
    return df


def fill_na_columns(df: pd.DataFrame, columns: List[str], value: int = 0):
    """
    Replace missing in columns with specified value
    :param df: A dataframe with missing values
    :param columns: A list of columns to fill
    :param value: a value to fill missings
    :return: a dataframe with filled missing values
    """
    if not set(columns).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    df[columns] = df[columns].fillna(value)
    return df


def rename_columns(df, columns: Dict[str, str]):
    if not set(columns.keys()).issubset(df.columns):
        raise ColumnMissingError("The specified columns do not exist in the dataframe")
    df = df.rename(mapper=columns)
    return df


def preprocess(file_path: str) -> pd.DataFrame:
    """
    Run all pre-processing steps to clean-up the KickStarter dataset
    :param file_path: The local path to the dataset
    :return:
    """
    df = read_dataframe(file_path, COLUMNS, encoding="iso-8859-1")
    df = parse_date_columns(df, columns=DATE_COLUMNS)
    df = fill_na_columns(df, columns=["usd pledged"], value=0)
    df = cast_columns_astype(df, COLUMN_TYPES)
    df = rename_columns(df, RENAMED_COLUMNS)
    df = label_encode_columns(df, ["category", "currency", "country"])
    # TODO: scale_columns
    return df
