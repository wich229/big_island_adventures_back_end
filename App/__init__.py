from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        app.config["Testing"] = True
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)
    from app.models.customer import Customer

    from .customers_routes import customers_bp
    app.register_blueprint(customers_bp)

    from app.models.tour import Tour
    from .tours_routes import tours_bp
    app.register_blueprint(tours_bp)


    from app.models.booking import Booking
    from .bookings_routes import bookings_bp
    app.register_blueprint(bookings_bp)

    CORS(app)
    return app
