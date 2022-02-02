from sqlalchemy.orm import Session
from model.albums.db_model import Albums
from model.artists.db_model import Artists
from model.tracks.db_model import Tracks

table_dict = {'Artists':Artists, 'Albums':Albums, 'Tracks':Tracks}

# generic repository with get methods
class Repo:
    # get all entries of a table by specifying its model name and injecting a connection session
    def get_all(self, table:str, db:Session):
        item_list = db.query(table_dict[table]).all()        
        return item_list
    
    # get a record of the given table by its primary key
    def get_by_id(self, id:int, table:str, db: Session):
        item = db.query(table_dict[table]).get(id)
        return item
       
    # get all records that match keyword clauses   
    def get_where(self, table:str, db:Session, **clauses):
        class_model = table_dict[table]
        item_list = db.query(class_model).filter_by(**clauses).all() 
        return item_list