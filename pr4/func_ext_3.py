import pandas as pd

def run_pandas():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    return f'Pandas Shape: {df.shape}'
