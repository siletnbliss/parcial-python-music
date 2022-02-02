from model.base_orm import BaseORM


class Album(BaseORM):
    AlbumId:int
    Title: str
    ArtistId:int 