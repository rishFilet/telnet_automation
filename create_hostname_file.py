import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

def generate_file():
    df = pd.DataFrame(columns=["Prod","Dev","Qa","Other"])
    df.to_csv(f"{os.getenv('HOSTS_FILENAME')}", index=False)
    print(f"{os.getenv('HOSTS_FILENAME')} created at {os.getcwd()}")

generate_file()
