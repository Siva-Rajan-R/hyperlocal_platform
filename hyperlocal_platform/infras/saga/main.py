from sqlalchemy.ext.asyncio import async_sessionmaker,AsyncSession,create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from core.config import SETTINGS
from icecream import ic



ENGINE=create_async_engine(url=SETTINGS.DATABASE_URL)
BASE=declarative_base()

AsyncLocalSession=async_sessionmaker(ENGINE)


async def init_infra_db():
    try:
        ic("Intializing infra database")
        async with ENGINE.connect() as conn:
            await conn.run_sync(BASE.metadata.create_all)
            await conn.commit()
    except Exception as e:
        ic(f"Intializing databse failed => {e}")


async def get_infra_async_session():
    Session=AsyncLocalSession()
    try:
        yield Session
    finally:
        await Session.close_all()
