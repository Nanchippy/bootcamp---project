import hashlib
  
str = "python is a snake"
  
result = hashlib.md5(str.encode())
 
print("md5 : ", end ="")
print(result.hexdigest())