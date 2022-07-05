from flask import Flask
from src.api_handlers import APIHandlers
import os, logging

def create_app() -> Flask:
    try:
        app = Flask(__name__)

        #app.add_url_rule("/getFrequency/<domain_name>", methods=["GET"], view_func = PhraseFrequencyAPIHandlers.get_frequency)
        #app.add_url_rule("/getInverseFrequency/<domain_name>", methods=["GET"], view_func = PhraseFrequencyAPIHandlers.get_inverse_frequency)
        #app.add_url_rule("/getPhraseByLength/<domain_name>", methods=["GET"], view_func = PhraseFrequencyAPIHandlers.get_phrase_by_length)
        #app.add_url_rule("/getAcronym/<domain_name>", methods=["GET"], view_func = PhraseFrequencyAPIHandlers.get_acronym)
        app.add_url_rule("/processImage/", methods=["POST"], view_func = APIHandlers.prepare_domain)
    except Exception as e:
        logging.critical("Flask app failed: {e}".format(e = e))
    return app

