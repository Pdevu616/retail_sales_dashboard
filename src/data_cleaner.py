import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
        self.report = {}

    # 1. Strip whitespace
    def strip_whitespace(self):
        self.df = self.df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        self.report['whitespace_removed'] = True
        return self

    # 2. Normalize case
    def normalize_case(self, case='lower'):
        for col in self.df.select_dtypes(include='object'):
            if case == 'lower':
                self.df[col] = self.df[col].str.lower()
            elif case == 'upper':
                self.df[col] = self.df[col].str.upper()
        self.report['case_normalized'] = case
        return self

    # 3. Remove special characters
    def remove_special_characters(self):
        for col in self.df.select_dtypes(include='object'):
            self.df[col] = self.df[col].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
        self.report['special_chars_removed'] = True
        return self

    # 4. Cast data types
    def cast_dtypes(self, dtype_map):
        self.df = self.df.astype(dtype_map)
        self.report['dtypes_casted'] = dtype_map
        return self

    # 5. Handle missing values
    def handle_missing(self, strategy='drop', fill_value=None):
        if strategy == 'drop':
            self.df = self.df.dropna()
        elif strategy == 'fill':
            self.df = self.df.fillna(fill_value)
        elif strategy == 'flag':
            self.df['missing_flag'] = self.df.isnull().any(axis=1)
        self.report['missing_strategy'] = strategy
        return self

    # 6. Remove duplicates
    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        self.report['duplicates_removed'] = before - after
        return self

    # 7. Clip outliers
    def clip_outliers(self, columns):
        for col in columns:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            self.df[col] = self.df[col].clip(lower, upper)
        self.report['outliers_clipped'] = columns
        return self

    # 8. Scale columns
    def scale_columns(self, columns):
        for col in columns:
            self.df[col] = (self.df[col] - self.df[col].mean()) / self.df[col].std()
        self.report['scaled_columns'] = columns
        return self

    # 9. Generate report
    def generate_report(self):
        return self.report

    # Final output
    def get_data(self):
        return self.df