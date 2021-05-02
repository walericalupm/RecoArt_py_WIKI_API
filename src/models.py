from peewee import Model, MySQLDatabase, CharField

remote_db = MySQLDatabase(None)


class BaseModel(Model):
    class Meta:
        database = remote_db


class WikipediaPaintCatalog(BaseModel):
    RecoArtPaintCode = CharField(max_length=10)
    WikipediaPaintCode = CharField(max_length=10)
