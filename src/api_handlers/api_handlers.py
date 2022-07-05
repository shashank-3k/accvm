from src.service_handlers.api_service_handlers import ServiceHandlers
from flask import request, jsonify
import logging, json

class APIHandlers:

    # API handler function for preparing domains for new domain added in UI
    @staticmethod
    def prepare_domain():
        data = request.get_json(force=True)
        
        target = ServiceHandlers.process_image(json.loads(data))
        
        logging.info("Successfully completed tasks")
        return json.dumps({'status': "success"}), 201, {'ContentType':'application/json'}
    
    