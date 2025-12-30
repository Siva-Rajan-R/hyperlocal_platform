from redis.asyncio import Redis
from icecream import ic
from ...core.configs.settings_config import SETTINGS

redis_client=Redis.from_url(SETTINGS.REDIS_URL,decode_responses=True)


async def check_redis_health():
    try:
        ic("🔃 Performing Redis health check...")
        pong = await redis_client.ping()
        ic(pong)
        if pong:
            ic("✅ Redis is connected and ready.")
            return True
        ic("❌ Redis health check failed: No pong response.")
        return False
    except Exception as e:
        ic(f"❌ Redis health check failed: {e}")
        return False
    

