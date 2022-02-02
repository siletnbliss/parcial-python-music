from sqlalchemy import Integer,String, Column, ForeignKey
from repository.database import Base

class Tracks(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    Composer = Column(String)
    
class FullTracks(Base):
    extend_existing=True
    __tablename__ = "tracks"
    __table_args__ = {'extend_existing':True}
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(String)
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))

class Genres(Base):
    __tablename__ = 'genres'
    GenreId = Column(Integer, primary_key= True)
    Name = Column(String)

class MediaTypes(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key= True)
    Name = Column(String)