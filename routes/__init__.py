from fastapi import APIRouter
from routes.artist_routes import router as artist_router
from routes.album_routes import router as album_router
from routes.track_routes import router as track_roter

router = APIRouter()

# setup al routes with their prefixes
router.include_router(artist_router, prefix = '/singers', tags=['Singers'] )
router.include_router(album_router, prefix = '/albums', tags =['Albums'])
router.include_router(track_roter, tags=['Songs'])