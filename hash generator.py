import hashlib
name = input('enter a input : ') 
result = hashlib.md5(name.encode())
result1 = hashlib.sha1(name.encode())
result2 = hashlib.sha224(name.encode())
result3 = hashlib.sha256(name.encode())

print('{}: {}'.format('md5',result.hexdigest()))
print ("\n")
print('{}: {}'.format('sha1',result1.hexdigest()))
print ("\n")
print('{}: {}'.format('sha224',result2.hexdigest()))
print ("\n")
print('{}: {}'.format('sha256',result3.hexdigest()))
