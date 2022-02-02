from model.base_orm import BaseORM
from typing import Optional

class Track(BaseORM):
    TrackId:int
    Name: str
    AlbumId:int
    Composer:Optional[str]
  
   
class FullTrack(BaseORM):
    TrackId:int
    Name: str
    AlbumId:int
    Composer:Optional[str]
    Milliseconds:int 
    Bytes: int
    UnitPrice: str 
    Media: str 
    Genre: str
    
