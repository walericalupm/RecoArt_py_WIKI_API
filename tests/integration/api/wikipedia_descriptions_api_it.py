from tests.base_test_setup import BaseTestCase, get_random_wikipedia_paint_catalog, get_recoart_fake_code
import src.models as models
from src.api import get_descriptions_from_wikipedia_api
from src.dtos import DescriptionsDTO
from src.app import app

from src.constansts import BASE_URI_V1, URI_WIKIPEDIA_DESCRIPTIONS, OK, NOT_FOUND


class WikipediaDescriptionApiIT(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_get_descriptions_from_wikipedia(self):
        with app.test_client() as client:
            recoart_code = get_random_wikipedia_paint_catalog().RecoArtPaintCode
            get_descriptions_from_wikipedia_url = BASE_URI_V1 + URI_WIKIPEDIA_DESCRIPTIONS + '/' + recoart_code
            response = client.get(get_descriptions_from_wikipedia_url)
            wikipedia_descriptions_json = response.get_json()
            wikipedia_descriptions = DescriptionsDTO(**wikipedia_descriptions_json)

            self.assertEqual(OK, response.status_code)
            self.assertEqual(4, len(wikipedia_descriptions.Descriptions))

    def test_get_descriptions_from_wikipedia_not_found(self):
        with app.test_client() as client:
            recoart_code = get_recoart_fake_code()
            get_descriptions_from_wikipedia_url = BASE_URI_V1 + URI_WIKIPEDIA_DESCRIPTIONS + '/' + recoart_code
            response = client.get(get_descriptions_from_wikipedia_url)

            self.assertEqual(NOT_FOUND, response.status_code)

