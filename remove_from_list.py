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
def remove_ports():
    print("Current list of ports being checked:\n")
    [print(port) for port in ports]
    print("\nType your ports you wish to remove and separate with a comma (,)")
    removals = input(
        f"Please input the ports you would like to remove to be checked for allowed connection\n")
    remove_list = removals.split(',')
    [ports.remove(port) for port in remove_list if port in ports]
    print("New list of ports:")
    [print(port) for port in ports]
    set_key(dotenv_path, "PORTS", str(ports))


while True:
    print("Your current public ip:\n")
    ip = get_external_ip()
    print(f"{ip}\n")
    ans = input(
        f"Would you like to remove [1]Hostnames (NOT AVAILABLE YET) or [2]Ports to be checked for connection from {ip}\nSelect 1 or 2:\n")
    if ans == '1':
        #add_hostnames()
        break
    elif ans == '2':
        remove_ports()
        break
    else:
        print("ERROR: Invalid selection, type 1 or 2")
