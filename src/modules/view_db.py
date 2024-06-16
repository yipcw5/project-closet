# Handles view of entries and properties for clothing items
import pandas as pd
from constants.errors import ERR_READ_CSV

CSV_PATH = './src/databases/clothing_inventory.csv'

def refresh_db():
    # Instantiate dataframe of clothes objects
    # TODO: perhaps update later to prevent need to instantiate every time

    df = pd.read_csv(CSV_PATH)
    return df

def view_db(df):
    print(df)

    return 0
