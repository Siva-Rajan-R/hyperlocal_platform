from jwt import PyJWT
from jwt.exceptions import PyJWTError,InvalidSignatureError,InvalidTokenError,ExpiredSignatureError
from . import SecurityModel,Any,Literal,Optional
import orjson
from datetime import datetime,timedelta,timezone
from icecream import ic


JWT_TOKEN=PyJWT()


class JwtTokenGenerator(SecurityModel):
    @staticmethod
    def generate(data:dict,exp_delta:timedelta,jwt_alg:str,jwt_secret:str,issuer:Optional[str]="De-Buggers")->str:
        try:
            data['iss']=issuer
            data['exp']=datetime.now(tz=timezone.utc)+exp_delta
            jwt_token=JWT_TOKEN.encode(
                payload=data,
                key=jwt_secret,
                algorithm=jwt_alg
            )

            return jwt_token
        
        except Exception:
            raise

    @staticmethod
    def verify(jwt_token:str,jwt_alg:str,jwt_secret:str,verify:Optional[bool]=True)->dict:
        try:
            decoded_jwt:dict=JWT_TOKEN.decode(
                jwt=jwt_token,
                key=jwt_secret,
                algorithms=jwt_alg,
                verify=verify
            )

            return decoded_jwt
        
        except (PyJWTError,InvalidSignatureError,InvalidTokenError,ExpiredSignatureError):
            false_reason="A 'False' returned due to the reason of PyJWTError,InvalidSignatureError,InvalidTokenError,ExpiredSignatureError"
            ic(false_reason)
            return False
        
        except Exception:
            raise


if __name__=="__main__":
    data={
        'id':'1234-5678-90',
        'name':"De-Buggers"
    }
    print(JwtTokenGenerator.generate(data=data,exp_delta=timedelta(seconds=60),jwt_alg="HS256",jwt_secret="1234"))
    print(JwtTokenGenerator.verify(jwt_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEyMzQtNTY3OC05MCIsIm5hbWUiOiJEZS1CdWdnZXJzIiwiaXNzIjoiRGUtQnVnZ2VycyIsImV4cCI6MTc2NjEzOTcxNH0.U8h4DO0JMSAgpqfsAeKO30JDPHh8claNoPjHzC2uJJw",jwt_alg="HS256",jwt_secret="1234"))
