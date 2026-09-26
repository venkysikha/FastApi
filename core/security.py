from datetime import datetime ,timedelta,timezone
import jwt
from pwdlib import passwordHash
from core.config import settings

password_hash = passwordHash.recommended()

def hash_password(password:str)->str:
    return password_hash.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return password_hash.verify(plain_password,hashed_password)


# creating the access token for the user the access protected routes 
