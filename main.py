from src.api import *
from src.app import app, load_database


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(port=8080, debug=True, host='0.0.0.0')
