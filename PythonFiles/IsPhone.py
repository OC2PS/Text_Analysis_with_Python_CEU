
"""
This example can be found in Automate the Boring Stuff
Pattern of the US phone numbers xxx-xxx-xxxx
"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
           return False
        for i in range(4, 7):
           if not text[i].isdecimal():
               return False
           if text[7] != '-':
               return False
        for i in range(8, 12):
           if not text[i].isdecimal():
               return False
    return True


message = 'Call me at home 415-555-1011 tomorrow.  Otherwise, my office number is 415-555-9999.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

