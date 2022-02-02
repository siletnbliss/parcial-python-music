from fastapi import APIRouter, status, Depends
from typing import List
from model.tracks.track_model import Track
from sqlalchemy.orm import Session
from repository.database import get_db
from repository.repo import Repo

router = APIRouter()


@router.get('/{album_id}', response_model =List[Track], status_code = status.HTTP_200_OK)
def get_all_albums(album_id:int,db: Session = Depends(get_db)):
    repo = Repo()
    return repo.get_where('Tracks',db, AlbumId = album_id)