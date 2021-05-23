from flask import render_template, redirect, url_for
from flask_cors import cross_origin
from src.app import app
from flask import request
from src.constants import *
from src.queries import get_wikipedia_descriptions_by_recoart_code
from src.utils import api_resource_response, api_error_response


@app.route(URI_INDEX)
def index():
    return redirect(url_for(GET_API_DOCS_METHOD_NAME))


@app.route(BASE_URI_V1 + URI_API_DOCS)
def get_api_docs():
    return render_template(SWAGGER_TEMPLATE)


@app.route(BASE_URI_V1 + URI_WIKIPEDIA_DESCRIPTIONS + RECOARTCODE_PARAM, methods=[GET])
@cross_origin()
def get_descriptions_from_wikipedia_api(recoart_code):
    language = request.args.get(LANGUAGE_PARAM).split(',')
    code, wikipedia_descriptions = get_wikipedia_descriptions_by_recoart_code(recoart_code, language)
    if code is OK:
        return api_resource_response(wikipedia_descriptions, code)
    else:
        return api_error_response(code)

