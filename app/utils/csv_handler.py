import pandas as pd

CSV_PATH = 'app/data/client.csv'

def read_csv():
    return pd.read_csv(CSV_PATH, encoding="latin1")

def save_costumer(data):
    data.to_csv(CSV_PATH, index=False, encoding="latin1")