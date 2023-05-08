# imports
from flask import Flask
from flask_cors import CORS

# Here we're gonna import the blueprints
from src.api.v1.api_app_script import api_app_script_bp

# function than create a flask app with CORS
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Here we're gonna register the blueprints
    app.register_blueprint(api_app_script_bp)
    
    return app
