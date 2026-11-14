from schemas.file_schemas import Fileschemas
from sqlalchemy.orm import Session
from models import file_model

async def insert_file(filename : str, db : Session) -> Fileschemas | None:
    exist_file =  ( 
                    db.query(file_model.FileInfo)
                    .filter( file_model.FileInfo.filename == filename )
                    .first()
                  )
    if exist_file:
        return None

    fileTable = file_model.FileInfo(filename=filename)

    db.add(fileTable)
    db.commit()
    db.refresh(fileTable)
    return Fileschemas.model_validate(fileTable)

async def get_files(db:Session):
    fileTable=db.query(file_model.FileInfo).all()
    if len(fileTable)==0:
        return None
    files = [Fileschemas.model_validate(f) for f in fileTable]
    return files

