import pandas as pd

@staticmethod
def load_csv(file_path: str) -> str:
    df = load_csv(file_path)
    return df.to_string(index=False)
