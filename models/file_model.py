from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from db.connection import Base

class FileInfo(Base):
    __tablename__="files"
    id : Mapped[int]=mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    filename : Mapped[str]=mapped_column(String(255))
