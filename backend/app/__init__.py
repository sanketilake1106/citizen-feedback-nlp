from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes import feedback_bp
    app.register_blueprint(feedback_bp, url_prefix='/api')

    return app
