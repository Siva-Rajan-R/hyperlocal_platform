from cryptography.fernet import Fernet,InvalidToken
from cryptography.exceptions import InvalidSignature,InvalidKey
from . import SecurityModel,Any
from icecream import ic
import orjson

class SymmetricEncryptionGenerator(SecurityModel):

    def generate(data:Any,secret:str)->str:
        try:
            fernet_obj=Fernet(key=secret)
            data_to_encrypt=orjson.dumps(data)
            encrypted_data=fernet_obj.encrypt(data=data_to_encrypt)
            return encrypted_data.decode()
        
        except Exception:
            raise

    @staticmethod
    def verify(encrypted_data:str,secret:str)->dict | bool:
        try:
            fernet_obj=Fernet(key=secret)
            decrypted_data=fernet_obj.decrypt(token=encrypted_data.encode())
            decoded_data=orjson.loads(decrypted_data.decode())
            return decoded_data
        except (InvalidKey,InvalidSignature,InvalidToken):
            false_reason="A 'False' occur due to these exceptions InvalidKey,InvalidSignature,InvalidToken"
            ic(false_reason)
            return False
        except Exception:
            raise
    
    @staticmethod
    def generate_key()->bytes:
        return Fernet.generate_key()
    

if __name__=='__main__':
    key=b'2pxxaWUx9DUGemE-vfjSX0cGh_D3H_Z6Qi2UI-wWYbs='
    data={'name':'de-buggers'}
    encrypted_data="gAAAAABpRT8nFWALjIOPmQkNHDJuyvfKnUbxiNXvdbCv0oyrMxH1WdndAsjeoxCYZWEQVkCnTjeQywaQXwomcOFI93pqemk5ME_UJoHcQnrK8zJdQ_8ovw4="
    print(SymmetricEncryptionGenerator.generate_key())
    print(SymmetricEncryptionGenerator.generate(data=data,secret=key))
    print(SymmetricEncryptionGenerator.verify(encrypted_data=encrypted_data,secret=key))