from src.api import *
from src.app import *


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(port=5001, debug=True, host='0.0.0.0')
