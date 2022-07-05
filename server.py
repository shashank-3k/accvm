from src import create_app
import logging
import os

if __name__=="__main__":
    try:
        app = create_app()
        app.run("0.0.0.0", port=5001, debug=False)
    except Exception as e:
        logging.critical("Service Crashed : {e} .".format(e = e))