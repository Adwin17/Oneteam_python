import re

def validate_mail(email):
    pattern=r'^[a-zA-Z0-9%+._-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
    if re.fullmatch(pattern,email):
        return True
    else:
        return False
def validate_phone(phone):
    if len(phone)==10 and phone.isdigit():
        return True
    else:
        return False

def validate_status(status):
    if status.lower() in ('active','inactive'):
        return True
    else:
        return False

def validate_gender(gender):
    if gender.lower() in ('male','female','other'):
        return True
    else:
        return False