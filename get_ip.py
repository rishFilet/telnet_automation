from requests import get

def get_external_ip():
    ip = get('https://api.ipify.org').text
    return ip
