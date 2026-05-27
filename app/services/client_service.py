import pandas as pd
from utils.csv_handler import read_csv, save_customer

def register_client(name, birth, type):
    df = read_csv()

    new = pd.DataFrame([{
        "name" : name,
        "birth": birth,
        "type": type
    }])

    df = pd.concat([df,new], ignore_index=True)
    save_customer(df)