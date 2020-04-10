def verify(pass1, pass2, name):
    if pass1 != pass2:
        return False
    if name is None or len(name) == 0 or name == 'admin':
        return False
    if len(pass1) < 8:
        return False
    else:
        return True

