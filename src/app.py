#src/app.py

from flask import Flask, render_template

from .config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint
from .views.PartyView import party_api as party_blueprint
from .views.SongView import song_api as song_blueprint

def create_app(env_name):
    """
    Create app
    """

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    #initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(party_blueprint, url_prefix='/api/v1/parties')
    app.register_blueprint(song_blueprint, url_prefix='/api/v1/songs')

    @app.route('/', methods=['GET'])
    def index():
        """
        homepage endpoint
        """
        return render_template('index.html')

    return app

    @app.route('/signup', methods=['GET'])
    def signup():
        """
        signup page endpoint
        """
        return render_template('signup.html')
