from flask import Flask


def create_app():
    app = Flask(__name__)

    from .controllers.items_controller import items_bp
    from .controllers.categories_controller import categories_bp
    from .controllers.healthcheck_controller import healthcheck_bp

    app.register_blueprint(items_bp, url_prefix='/items')
    app.register_blueprint(categories_bp, url_prefix='/categories')
    app.register_blueprint(healthcheck_bp, url_prefix='/healthcheck')

    return app
