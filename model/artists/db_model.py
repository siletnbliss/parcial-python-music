from sqlalchemy import Integer,String, Column
from repository.database import Base

class Artists(Base):
    __tablename__ = "artists"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)