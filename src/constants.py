import os

# ROOT Project Path
CURRENT_DIR = 'src'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(CURRENT_DIR, '')
ENV_TEST_DIR = os.path.join(ROOT_DIR, '.env.test')
TEMPLATE_FOLDER_DIR = os.path.join(ROOT_DIR, 'templates')
STATIC_FOLDER_DIR = os.path.join(ROOT_DIR, 'static')

# API
V1 = '/v1'
BASE_URI_V1 = '/api' + V1
URI_INDEX = '/'
URI_API_DOCS = '/docs'

RECOARTCODE_PARAM = '/<string:recoart_code>'
URI_WIKIPEDIA_DESCRIPTIONS = '/wikidescriptions'

# API methods
GET_API_DOCS_METHOD_NAME = 'get_api_docs'

# Templates
SWAGGER_TEMPLATE ='swaggerui.html'

JSON_MIME_TYPE = 'application/json'

NOT_FOUND_MESSAGE = 'Resource Not Found'
SERVER_ERROR_MESSAGE = 'Server Error'
LANGUAGE_PARAM = 'lang'

# API Language codes
API_ES = '0'
API_EN = '1'
API_FR = '2'
API_IT = '3'


# HTTP Response Codes
CREATED = 201
OK = 200
REDIRECT_FOUND = 302
CONFLICT = 409
NOT_FOUND = 404
SERVER_ERROR = 500

# HTTP Methods
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'


# Wikipedia Language codes
LANG_ES = 'es'
LANG_EN = 'en'
LANG_IT = 'it'
LANG_FR = 'fr'

# Wikipedia Tool request
WPR_CLAIMS = 'claims'
WPR_IMAGE_INFO = 'imageinfo'
WPR_LABELS = 'labels'
WPR_PARSE = 'parse'
WPR_RANDOM = 'random'
WPR_RESTBASE = 'restbase'

# Wikipedia Tool extract plain text
WPT_TEXT = 'exrest'

# Various
MESSAGE = 'message'
FLASK_CONFIG_CORS_HEADERS_KEY = 'CORS_HEADERS'
FLASK_CONFIG_CORS_HEADERS_VALUE = 'Content-Type'
DEFAULT_APP_PORT = 80
DEFAULT_APP_HOST = '0.0.0.0'
PORT = 'PORT'
