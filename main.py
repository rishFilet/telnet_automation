from telnetlib import Telnet
from enum import Enum
import argparse
import pandas as pd
import numpy as np
import os
from os.path import join, dirname
from dotenv import load_dotenv
from prettytable import PrettyTable

from get_ip import get_external_ip
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
# Load file from the path.
load_dotenv(dotenv_path)
hosts_filename = os.getenv("HOSTS_FILENAME")
ports = os.getenv("PORTS").strip('][').split(', ')
ports = [port.strip("'") for port in ports]

class HostEnv(Enum):
    PROD = "prod"
    QA = "qa"
    DEV = "dev"
    OTHER = "other"
    ALL = "all"
def check_empty_list(list_to_check):
    for l in list_to_check:
        if l:
            return True
        else:
            return False
def check_connections(env):
    df_o = pd.read_csv(hosts_filename)
    df = df_o.fillna("None")
    columns = []
    if env == env.PROD:
        columns.append("Prod")
    elif env == env.DEV:
        columns.append("Dev")
    elif env == env.QA:
        columns.append("Qa")
    elif env == env.OTHER:
        columns.append("Other")
    else:
        columns = df.columns.values.tolist()

    for env in columns:
        print(f"\nPorts to check: {str(ports).strip('][')}\nChecking Connection for environment:\n@@@@@@\n{env.upper()}\n@@@@@@@\n")
        data = []
        for host in df[env]:
            host_info = []
            if host != "None":
                host_info.append(host)
                for port in ports:
                    try:
                        #print(f"Host: {host}, Port: {port}")
                        with Telnet(host=host, port=port, timeout=1) as tn:
                            #print("++++\nConnection Established\n++++++\n")
                            host_info.append("GOOD")
                            tn.close()
                    except Exception as e:
                        host_info.append("X")
                        #print("------\nTimed out\n--\n")
            data.append(host_info)
        if check_empty_list(data):
            column_headers = ["Hostname", *ports]
            new_df = pd.DataFrame(data, columns=column_headers)
            ip = get_external_ip()
            new_df.to_csv(f"{ip}_{env}.csv", index=False)
            # Creating a pretty table in terminal
            table = PrettyTable(column_headers)
            for row in new_df.values.tolist():
                if None not in row:
                    table.add_row(row)
            print(table)

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(
        description="Setting the option for hosts to check")
    my_parser.add_argument("-prod", action='store_true')
    my_parser.add_argument("-qa", action='store_true')
    my_parser.add_argument("-dev", action='store_true')
    my_parser.add_argument("-other", action='store_true')
    my_parser.add_argument("-all", action='store_true')
    args = my_parser.parse_args()
    print(f"Your current public ip:\n{get_external_ip()}")
    if vars(args)[HostEnv.PROD.value]:
        check_connections(HostEnv.PROD)
    elif vars(args)[HostEnv.DEV.value]:
        check_connections(HostEnv.DEV)
    elif vars(args)[HostEnv.QA.value]:
        check_connections(HostEnv.QA)
    elif vars(args)[HostEnv.OTHER.value]:
        check_connections(HostEnv.OTHER)
    elif vars(args)[HostEnv.ALL.value]:
        check_connections(HostEnv.ALL)
    else:
        check_connections(HostEnv.ALL)
