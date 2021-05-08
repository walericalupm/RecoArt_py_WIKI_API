from src import models
from tests.base_test_setup import BaseTestCase, get_random_wikipedia_paint_catalog, get_wikidata_random_language
from src.wikipedia_extractor import get_info_from_wikidata


class WikipediaDescriptionsWikidataIT(BaseTestCase):
    def setUp(self):
        models.remote_db.close()

    def test_extract_paint_descriptions_from_wikidata(self):
        wikidata_code = get_random_wikipedia_paint_catalog().WikipediaPaintCode
        wikidata_description = get_info_from_wikidata(wikidata_code, get_wikidata_random_language())

        self.assertIsNotNone(wikidata_description)
