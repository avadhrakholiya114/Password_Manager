from django.conf import settings
from cryptography.fernet import Fernet
import base64


def encrypt(password):
    try:
        pass_word = str(password)
        cipher_password = Fernet(settings.ENCRYPT_KEY)
        encode_password = cipher_password.encrypt(password.encode('ascii'))
        return base64.urlsafe_b64encode(encode_password).decode()
    except Exception as e:
        print(e)
