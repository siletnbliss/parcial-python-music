from fastapi import APIRouter, status, Depends
from typing import List
from model.artists.artist_model import Artist
from model.albums.album_model import Album
from sqlalchemy.orm import Session
from repository.database import get_db
from repository.repo import Repo

router = APIRouter()

@router.get('/', response_model =List[Artist], status_code = status.HTTP_200_OK)
def get_all_artists(db: Session = Depends(get_db)):
    repo = Repo()
    return repo.get_all('Artists', db)

@router.get('/{artist_id}', response_model =List[Album], status_code = status.HTTP_200_OK)
def get_all_albums(artist_id:int,db: Session = Depends(get_db)):
    repo = Repo()
    return repo.get_where('Albums',db, ArtistId = artist_id)