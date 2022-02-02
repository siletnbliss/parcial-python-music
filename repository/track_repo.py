from sqlalchemy.orm import Session
from model.albums.db_model import Albums
from model.artists.db_model import Artists
from model.tracks.db_model import FullTracks, Genres, MediaTypes, Tracks

# repo to make more specific queries about tracks 
class TrackRepo:
    # get all songs of an artist
    def get_all(self, artist_id:int, db:Session):
        # make joins to associate songs with artist
        item_list = db.query(Tracks).join(Albums).join(Artists).filter( Artists.ArtistId == artist_id).all()
        return item_list
    
    # get full song info by id 
    def get_by_id(self, id:int, db: Session):
        # get genre and media type via joins and select and rename attributes
        item = db.query(FullTracks).join(Genres).join(MediaTypes).filter(FullTracks.TrackId ==id).with_entities(FullTracks.TrackId, FullTracks.Name, FullTracks.AlbumId, FullTracks.Bytes, FullTracks.Composer, FullTracks.UnitPrice,(Genres.Name).label("Genre"),(MediaTypes.Name).label("Media") ).one()
        return item
       