from flask import Flask


def init_app():
    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    
    from database.db import init_db
    init_db() 

    with app.app_context():

        from point.routes import point_app
        from position.routes import position_app

        # Register Blueprints
        app.register_blueprint(point_app)
        app.register_blueprint(position_app)

    from database.db import shutdown_session
    app.teardown_appcontext(shutdown_session)
    
    return app