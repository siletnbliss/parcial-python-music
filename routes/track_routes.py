from fastapi import APIRouter, status, Depends
from typing import List
from model.tracks.track_model import FullTrack, Track
from model.albums.album_model import Album
from sqlalchemy.orm import Session
from repository.database import get_db
from repository.repo import Repo
from repository.track_repo import TrackRepo

router = APIRouter()

@router.get('/singer/{artist_id}', response_model =List[Track], status_code = status.HTTP_200_OK)
def get_all_Tracks(artist_id:int,db: Session = Depends(get_db)):
    repo = TrackRepo()
    return repo.get_all(artist_id, db)

@router.get('/song/{track_id}', status_code = status.HTTP_200_OK)
def get_all_albums(track_id:int,db: Session = Depends(get_db)):
    repo = TrackRepo()
    return repo.get_by_id(track_id, db)