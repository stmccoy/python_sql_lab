import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()

artist_1 = Artist("Taylor Swift")
artist_repository.save(artist_1)

artist_2 = Artist("Ben Howard")
artist_repository.save(artist_2)



pdb.set_trace()
