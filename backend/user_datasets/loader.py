import pandas as pd

class DatasetLoader:
    @staticmethod
    def load_dataset(path):
        return pd.read_csv(path)  # Assuming CSV format
