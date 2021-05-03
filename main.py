from src.api import *
import src.app as ap


if __name__ == '__main__':
    ap.load_database()
    ap.app.debug = True
    ap.app.run(port=5001, debug=True, host='0.0.0.0')
