import pandas as pd

@staticmethod
def load_xlsx(file_path: str) -> str:
    df = pd.read_excel(file_path)
    return df.to_string(index=False)