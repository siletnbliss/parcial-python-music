from pydantic import BaseModel as _BaseModel

# base model for pydantic classes that represent a model in database
class BaseORM(_BaseModel):

    class Config:
        orm_mode=True

