# project/__init__.py
from flask import Flask
from .extensions import db, login_manager, migrate, oauth

def create_app():
    app = Flask(__name__)
    app.config.from_object('project.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    oauth.init_app(app)

    # Move User import here after db is initialized to avoid circular dependencies
    from project.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'auth.login'

    # Initialize OAuth clients
    from project.oauth_helpers import init_oauth
    init_oauth(app)

    # Register blueprints
    from project.blueprints.auth import auth_bp
    from project.blueprints.main import main_bp
    from project.blueprints.events import events_bp
    from project.blueprints.profile import profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(profile_bp)

    return app
