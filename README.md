# Checking your connections

As a devops engineer, there comes a time when you might have to change access to certain machines or host ips on various ports. A good example is if you have multiple instances on AWS and security groups with various rules attached to them. As an engineer, it is natural to think of a way to automate this process instead of doing `telnet <host> <port>` for each machine/host.

This is a small script i wrote in python which performs that same telnet command on a list of hostnames (or ips) and the various ports.

## Setup
1. Create a virtual envrionment : `virtualenv venv`
2. Activate the environment: `source venv/bin/activate`
3. Install dependencies: `pip3 install -r requirements.txt`

## Host & Port setup
In the file `.env` you can edit the name of the csv file which contains your hostnames/ips. Change the name of the file saved in this directory to the variable `HOSTS_FILENAME`.
Add as many ports as your like to the list `PORTS` as integers.
```
HOSTS_FILENAME='hostnames.csv'
PORTS=[22, 8000, 9000]
```

For the hostnames csv, you can create a csv on your own with some headers but for this application, since it was quick, the script works with column headers "Prod", "Dev", "Qa", "Other" for testing out the different environments i am checking. You can create a similar file by doing first setting the name of the host file in `.env` and then running `python3 create_hostname_file.py`

In the hostnames file under each column you can include a DNS name eg. something.example.com or an ip address.

There are 5 flags you can run:
- -prod
- -qa
- -dev
- -other
- -all

(Not including a flag will default to all)

Once that is set, run `python3 main.py <flag>` and it will display the connections on each port as well as output this information to a csv names <your_public_ip>_<Environment>.csv eg. 192.168.2.2_Prod.csv

Enjoy!

Welcome any feedback and improvements as this was a quick script i did in an hour i thought i'd share