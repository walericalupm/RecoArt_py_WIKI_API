from src.app import app
from src.constansts import *
from src.queries import get_wikipedia_descriptions_by_recoart_code
from src.utils import api_resource_response, api_error_response


@app.route('/')
def hello_world():
    return 'Welcome to RecoArt Wikidata Painting extractor!'


@app.route(BASE_URI_V1 + URI_WIKIPEDIA_DESCRIPTIONS + RECOARTCODE_PARAM, methods=[GET])
def get_descriptions_from_wikipedia_api(recoart_code):
    code, wikipedia_descriptions = get_wikipedia_descriptions_by_recoart_code(recoart_code)
    if code is OK:
        return api_resource_response(wikipedia_descriptions, code)
    else:
        return api_error_response(code)

