from sqlalchemy import Integer,String, Column, ForeignKey
from repository.database import Base

class Albums(Base):
    __tablename__ = "albums"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))