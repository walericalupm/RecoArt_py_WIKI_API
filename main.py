from src.api import *
from src.app import app, load_database


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    load_database()
    app.debug = True
    app.run(port=port, debug=True, host='0.0.0.0')
