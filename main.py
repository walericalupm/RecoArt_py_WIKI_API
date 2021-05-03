from src.api import *
import src.app as app


if __name__ == '__main__':
    app.load_database()
    app.app.debug = True
    app.app.run(port=5001, debug=True, host='0.0.0.0')
