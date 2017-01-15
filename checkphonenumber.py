#!/usr/local/bin/python3.6

def checkphone(phonenumber):
    if len(phonenumber) != 12:
        return False
    for i in range(0,3):
        if not phonenumber[i].isdecimal():
            return False
    if phonenumber[3] != '-':
        return False
    for i in range(4,7):
        if not phonenumber[i].isdecimal():
            return False
    if phonenumber[7] != '-':
        return False
    for i in range(8,12):
        if not phonenumber[i].isdecimal():
            return False
    return True

#print(checkphone('510-123-4567'))
print(checkphone('test-123-4567'))
