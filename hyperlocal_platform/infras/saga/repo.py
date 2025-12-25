from .main import AsyncSession
from sqlalchemy import select,update,delete
from .models import SagaStates
from core.models.service_repo_base_models import CommonBaseRepoModel
from .schemas import CreatedSagaStatesSchema,UpdateSagaStatesSchema
from core.decorators.db_session_handler_dec import start_db_transaction
from core.enums.saga_state_enum import SagaStatusEnum


class SagaStatesRepo(CommonBaseRepoModel):
    def __init__(self,session:AsyncSession):
        self.session=session
        self.ss_cols=(
            SagaStates.id,
            SagaStates.status,
            SagaStates.type,
            SagaStates.data,
            SagaStates.retry_count,
            SagaStates.created_at
        )

    @start_db_transaction
    async def create(self,data:CreatedSagaStatesSchema):
        ss_toadd=SagaStates(**data.model_dump(mode="json"))
        self.session.add(ss_toadd)
        return True


    @start_db_transaction
    async def update(self,data:UpdateSagaStatesSchema):
        ss_toupdate=update(SagaStates).where(SagaStates.id==data.id).values(**data.model_dump(mode="json",exclude=["id"])).returning(SagaStates.id)
        is_updated=(await self.session.execute(ss_toupdate)).scalar_one_or_none()
        return  is_updated
    
    
    @start_db_transaction
    async def delete(self,saga_id:str):
        ss_todel=delete(SagaStates).where(SagaStates.id==saga_id).returning(SagaStates.id)
        is_deleted=(await self.session.execute(ss_todel)).scalar_one_or_none()
        return is_deleted
    

    @start_db_transaction
    async def update_status(self,status:SagaStatusEnum,saga_id:str):
        is_updated=(await self.session.execute(update(SagaStates).where(SagaStates.id==saga_id).values(status=status).returning(SagaStates.id))).scalar_one_or_none()
        return is_updated
    

    @start_db_transaction
    async def update_retry_count(self,retry_count:int,saga_id:str):
        is_updated=(await self.session.execute(update(SagaStates).where(SagaStates.id==saga_id).values(retry_count=retry_count).returning(SagaStates.id))).scalar_one_or_none()
        return is_updated


    async def get(self):
        saga_states=(
            await self.session.execute(
                select(*self.ss_cols)
            )
        ).mappings().all()

        return saga_states
    

    async def getby_id(self,saga_id:str):
        saga_state=(
            await self.session.execute(
                select(*self.ss_cols)
                .where(SagaStates.id==saga_id)
            )
        ).mappings().one_or_none()

        return saga_state
    

    async def search(self, query, limit = 5):
        "This is just a wrapper method for a ABC CommonBaseRepoModel"
        ...