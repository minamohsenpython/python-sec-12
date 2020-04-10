import hashlib
m = hashlib.sha1()
m.update(b"hello")
print(m.hexdigest())