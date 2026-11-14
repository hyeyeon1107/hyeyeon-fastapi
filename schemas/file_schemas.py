from pydantic import BaseModel, ConfigDict

class Fileschemas(BaseModel):
    id : int
    filename : str

    model_config = ConfigDict(from_attributes=True)