from peewee import DoesNotExist
from src import models
from tests.base_test_setup import BaseTestCase, get_random_wikipedia_paint_catalog, get_recoart_fake_code


class WikipediaDescriptionsDbIT(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_get_wikipedia_paint_catalog(self):
        recoart_code = get_random_wikipedia_paint_catalog().RecoArtPaintCode
        wikipedia_catalog = models.WikipediaPaintCatalog.select() \
            .where(models.WikipediaPaintCatalog.RecoArtPaintCode == recoart_code)
        self.assertIsNotNone(wikipedia_catalog)

    def test_get_non_existent_wikipedia_paint_catalog(self):
        recoart_code = get_recoart_fake_code()
        non_existent_wikipedia_catalog = models.WikipediaPaintCatalog.select() \
            .where(models.WikipediaPaintCatalog.RecoArtPaintCode == recoart_code)
        self.assertRaises(DoesNotExist, non_existent_wikipedia_catalog.get)
