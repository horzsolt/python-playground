import re

def ipv4_validator():
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", "127.0.0.1")
    print(match)
    return bool(match)

print(ipv4_validator())