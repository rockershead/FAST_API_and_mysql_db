from pydantic import BaseModel
class Pyden_User(BaseModel):
 name: str=None
 age: int=None
 hobby:str=None