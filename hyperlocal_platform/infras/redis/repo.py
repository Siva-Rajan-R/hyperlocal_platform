import orjson
from icecream import ic
from .main import redis_client

class RedisRepo():

    @staticmethod
    async def set(key:str, value, expire:int=None):
        try:
            value=orjson.dumps(value)
            await redis_client.set(name=key, value=value, ex=expire)
            ic(f"✅ Set Redis key: {key} with value: {value} and expire: {expire}")
            return True
        except Exception as e:
            ic(f"❌ Failed to set Redis key: {key}. Error: {e}")
            return False
        
    @staticmethod
    async def get_ttl(key:str):
        try:
            ttl = await redis_client.ttl(name=key)
            ic(f"✅ TTL for Redis key: {key} is {ttl} seconds")
            return ttl
        except Exception as e:
            ic(f"❌ Failed to get TTL for Redis key: {key}. Error: {e}")
            return None
        
    @staticmethod
    async def get(key:str):
        try:
            value = await redis_client.get(name=key)
            value = orjson.loads(value) if value else None
            ic(f"✅ Retrieved Redis key: {key} with value: {value}")
            return value
        except Exception as e:
            ic(f"❌ Failed to get Redis key: {key}. Error: {e}")
            return None
        
    @staticmethod
    async def unlink(keys:list):
        try:
            result = await redis_client.unlink(*keys)
            ic(f"✅ Unlinked Redis keys: {keys}. Result: {result}")
            return result
        except Exception as e:
            ic(f"❌ Failed to unlink Redis key: {keys}. Error: {e}")
            return None