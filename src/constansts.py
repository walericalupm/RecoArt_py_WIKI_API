import os

# ROOT Project Path
CURRENT_DIR = 'src'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(CURRENT_DIR, '')
ENV_TEST_DIR = os.path.join(ROOT_DIR, '.env.test')

# API
V1 = '/v1'
BASE_URI_V1 = '/api' + V1
RECOARTCODE_PARAM = '/<string:recoart_code>'
URI_WIKIPEDIA_DESCRIPTIONS = '/wikidescriptions'

JSON_MIME_TYPE = 'application/json'

NOT_FOUND_MESSAGE = 'Resource Not Found'
SERVER_ERROR_MESSAGE = 'Server Error'

# HTTP Response Codes
CREATED = 201
OK = 200
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

# Wikipedia Tool lead text
WPT_LEAD = 'extext'

# Various
MESSAGE = 'message'
