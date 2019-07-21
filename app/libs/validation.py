import re
from ipaddress import ip_address


def zone_validation(zone):
    pattern = re.compile("^(?!(https:\/\/|http:\/\/|www\.|mailto:|smtp:|ftp:\/\/|ftps:\/\/))(((([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\-]{0,86}[a-zA-Z0-9]))\.(([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\-]{0,73}[a-zA-Z0-9]))\.(([a-zA-Z0-9]{2,12}\.[a-zA-Z0-9]{2,12})|([a-zA-Z0-9]{2,25})))|((([a-zA-Z0-9])|([a-zA-Z0-9][a-zA-Z0-9\-]{0,162}[a-zA-Z0-9]))\.(([a-zA-Z0-9]{2,12}\.[a-zA-Z0-9]{2,12})|([a-zA-Z0-9]{2,25}))))$")
    if pattern.match(zone):
        return False
    else:
        return True

def record_validation(record) :
    if record == '@' or record=='*':
        return False
    else:
        pattern = re.compile("^(([\*a-zA-Z0-9_]|[a-zA-Z0-9_][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[_A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$")
        if pattern.match(record):
            return False
        else:
            return True

def count_character(name):
    if name.find("."):
        spl_name = name.split(".")
        for i in spl_name:
            if len(i) >= 64:
                return True
            else:
                total = total + len(i)
        if total >= 255:
            return True
        else:
            return False
    else:
        return False