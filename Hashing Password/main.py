import bcrypt 

password = '12345678'
bytes = password.encode('utf-8') 
salt = bcrypt.gensalt() 
hash = bcrypt.hashpw(bytes, salt) 

print(hash)
