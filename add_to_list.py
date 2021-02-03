import pandas as pd
import os
from os.path import join, dirname
from dotenv import load_dotenv, set_key
from get_ip import *
# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
# Load file from the path.
load_dotenv(dotenv_path)
hosts_filename = os.getenv("HOSTS_FILENAME")
ports = os.getenv("PORTS").strip('][').split(', ')
ports = [port.strip("'") for port in ports]

def add_to_list(additions, env_string):
    df = pd.read_csv(hosts_filename)
    for each in additions:
        new_row = {env_string:each}
        df = df.append(new_row, ignore_index=True)
    df.to_csv(hosts_filename, index=False)
    print(f"Added {additions} to {env_string}")


def add_hostnames():
    print("\nAdd your hostnames or ip and separate with a comma (,)")
    additions = input(
        f"Please input the hostnames you would like to add to {hosts_filename}\n")
    while True:
        environment = input(
            f"\nWhich environment to they belong to?\n1.Prod\n2.Dev\n3.Qa\n4.Other\n")
        if environment == '1':
            env_string = "Prod"
            break
        elif environment == '2':
            env_string = "Dev"
            break
        elif environment == '3':
            env_string = "Qa"
            break
        elif environment == '4':
            env_string = "Other"
            break
        else:
            print("\nERROR: That input is invalid please choose a number between 1-4\n")

    additions_list = []
    if ',' in additions:
        additions_list = additions.split(',')
    else:
        additions_list.append(additions)
    add_to_list(additions_list, env_string)


def add_ports():
    print("Current list of ports being checked:\n")
    [print(port) for port in ports]
    print("\nAdd your ports and separate with a comma (,)")
    additions = input(
        f"Please input the ports you would like to add to be checked for allowed connection\n")
    ports.extend(additions.split(','))
    print("New list of ports:")
    [print(port) for port in ports]
    set_key(dotenv_path, "PORTS", str(ports))


while True:
    ans = input(f"Would you like to add [1]Hostnames or [2]Ports to be checked for connection from {get_external_ip()}\nSelect 1 or 2:\n")
    if ans == '1':
        add_hostnames()
        break
    elif ans == '2':
        add_ports()
        break
    else:
        print("ERROR: Invalid selection, type 1 or 2")

