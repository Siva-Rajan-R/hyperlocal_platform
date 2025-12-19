from argon2 import PasswordHasher
from argon2.exceptions import VerificationError,VerifyMismatchError,InvalidHashError
from . import SecurityModel,Any

import orjson
from icecream import ic


PH=PasswordHasher()


class Argon2HashingGenerator(SecurityModel):
    @staticmethod
    def generate(data:Any):
        try:
            data_to_hash=orjson.dumps(data)
            hashed_data=PH.hash(password=data_to_hash)
            return hashed_data
        
        except Exception:
            raise
    @staticmethod
    def verify(hashed_data:str,plain_data:Any):
        try:
            plain_data=orjson.dumps(plain_data)
            verified_data=PH.verify(hash=hashed_data,password=plain_data)
            if verified_data:
                return True
            return False
        except (VerifyMismatchError,VerificationError,InvalidHashError):
            false_reason="A 'False' returned due to the exceptions of VerifyMismatchError,VerificationError,InvalidHashError"
            ic(false_reason)
            return False
        
        except Exception:
            raise

if __name__=='__main__':
    data={"name":"Debuggers"}
    print(Argon2HashingGenerator.generate(data=data))
    print(Argon2HashingGenerator.verify("$argon2id$v=19$m=65536,t=3,p=4$8/dgEDPJl94wsOmWm8+Q0w$t5Rq36BxIJhBFCmKaatFby3NHDIh+bj3quuPRshwh0",data))